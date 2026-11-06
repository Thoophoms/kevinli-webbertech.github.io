#!/bin/bash
#
# nexus_lab2_test_network.sh
#
# Verifies the Jenkins <-> Nexus Docker network setup from Nexus Lab2 (Step 4):
#   - the "jenkins" and "nexus" containers exist and are running
#   - both are connected to the "ci-network" Docker network
#   - Jenkins can resolve "nexus" by name (DNS) and reach it over HTTP
#
# Each check prints OK or FAIL. On the first failure, the script prints an
# actionable error message to stderr and exits with a non-zero status, so it
# can also be used as a CI/pipeline health check (e.g. before "mvn deploy").
#
# Usage: ./nexus_lab2_test_network.sh

set -u

NETWORK_NAME="ci-network"
JENKINS_CONTAINER="jenkins"
NEXUS_CONTAINER="nexus"

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

check_running() {
  local name="$1"
  echo -n "Checking container '$name' is running... "
  if [ "$(docker inspect -f '{{.State.Running}}' "$name" 2>/dev/null)" = "true" ]; then
    echo "OK"
  else
    echo "FAIL"
    fail "Container '$name' is not running. Start it with nexus_lab2_setup_network.sh, or 'docker start $name'."
  fi
}

check_network_membership() {
  local name="$1"
  echo -n "Checking '$name' is connected to '$NETWORK_NAME'... "
  if docker network inspect "$NETWORK_NAME" --format '{{range .Containers}}{{.Name}} {{end}}' 2>/dev/null \
       | grep -qw "$name"; then
    echo "OK"
  else
    echo "FAIL"
    fail "'$name' is not connected to '$NETWORK_NAME'. Run: docker network connect $NETWORK_NAME $name"
  fi
}

check_dns_resolution() {
  echo -n "Checking Jenkins can resolve '$NEXUS_CONTAINER' by name... "
  if docker exec "$JENKINS_CONTAINER" getent hosts "$NEXUS_CONTAINER" >/dev/null 2>&1; then
    echo "OK"
  else
    echo "FAIL"
    fail "Jenkins cannot resolve '$NEXUS_CONTAINER'. Confirm both containers are on '$NETWORK_NAME' (see checks above)."
  fi
}

check_http_connectivity() {
  echo -n "Checking Jenkins can reach Nexus over HTTP... "

  local code=""
  local status_url="http://${NEXUS_CONTAINER}:8081/service/rest/v1/status"

  if docker exec "$JENKINS_CONTAINER" sh -c 'command -v curl' >/dev/null 2>&1; then
    code=$(docker exec "$JENKINS_CONTAINER" curl -s -o /dev/null -w '%{http_code}' "$status_url" 2>/dev/null)
  elif docker exec "$JENKINS_CONTAINER" sh -c 'command -v wget' >/dev/null 2>&1; then
    code=$(docker exec "$JENKINS_CONTAINER" sh -c \
      "wget -S -O /dev/null '$status_url' 2>&1 | awk '/HTTP\\// {print \$2; exit}'")
  else
    echo "FAIL"
    fail "Neither curl nor wget is available inside the '$JENKINS_CONTAINER' container to test connectivity."
  fi

  if [ -n "$code" ] && [ "$code" -ge 200 ] 2>/dev/null && [ "$code" -lt 500 ] 2>/dev/null; then
    echo "OK (HTTP $code)"
  else
    echo "FAIL"
    fail "Jenkins could not reach $status_url (got '${code:-no response}'). Check 'docker logs $NEXUS_CONTAINER' and confirm Nexus has finished starting."
  fi
}

echo "=== Verifying Nexus Lab2 Docker network setup ==="
check_running "$JENKINS_CONTAINER"
check_running "$NEXUS_CONTAINER"
check_network_membership "$JENKINS_CONTAINER"
check_network_membership "$NEXUS_CONTAINER"
check_dns_resolution
check_http_connectivity

echo
echo "All checks passed: '$JENKINS_CONTAINER' and '$NEXUS_CONTAINER' are both on '$NETWORK_NAME' and can talk to each other."
