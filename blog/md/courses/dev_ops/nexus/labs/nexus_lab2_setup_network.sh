#!/bin/bash
#
# nexus_lab2_setup_network.sh
#
# Consolidates the docker commands from Nexus Lab2 (Steps 1, 3, 4):
#   - Start the Jenkins container (name: jenkins)
#   - Start the Nexus container (name: nexus)
#   - Create a shared Docker network (ci-network)
#   - Connect both containers to it, so Jenkins can reach Nexus at http://nexus:8081
#
# See: nexus_lab2_jenkins_integration.md
#
# Usage: ./nexus_lab2_setup_network.sh

set -e

NETWORK_NAME="ci-network"

start_container_if_missing() {
  local name="$1"
  shift
  if docker ps -a --format '{{.Names}}' | grep -qx "$name"; then
    echo "==> Container '$name' already exists, skipping 'docker run'."
  else
    echo "==> Starting container '$name'..."
    docker run "$@"
  fi
}

echo "=== Step 1: Start Jenkins ==="
start_container_if_missing jenkins \
  -d -p 8080:8080 -p 50000:50000 --name jenkins jenkins/jenkins:lts

echo
echo "=== Step 3: Start Nexus ==="
docker volume create nexus-data >/dev/null
start_container_if_missing nexus \
  -d -p 8081:8081 --name nexus -v nexus-data:/nexus-data sonatype/nexus3

echo
echo "=== Step 4: Create ci-network and connect both containers ==="
if docker network inspect "$NETWORK_NAME" >/dev/null 2>&1; then
  echo "==> Network '$NETWORK_NAME' already exists, skipping 'docker network create'."
else
  docker network create "$NETWORK_NAME"
fi

for c in jenkins nexus; do
  if docker network inspect "$NETWORK_NAME" --format '{{range .Containers}}{{.Name}} {{end}}' | grep -qw "$c"; then
    echo "==> '$c' is already connected to '$NETWORK_NAME'."
  else
    docker network connect "$NETWORK_NAME" "$c"
    echo "==> Connected '$c' to '$NETWORK_NAME'."
  fi
done

echo
echo "=== Verify ==="
docker network inspect "$NETWORK_NAME" --format '{{range .Containers}}{{.Name}} - {{.IPv4Address}}{{"\n"}}{{end}}'

echo
echo "Jenkins UI: http://localhost:8080"
echo "Nexus UI:   http://localhost:8081"
echo "Get the Jenkins admin password: docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword"
echo "Get the Nexus admin password:   docker exec nexus cat /nexus-data/admin.password"
echo "From inside Jenkins, Nexus is reachable at: http://nexus:8081"
