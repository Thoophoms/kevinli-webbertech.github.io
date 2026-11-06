#!/bin/bash

# K8s Local setup script

function cleanup() {
  kubectl delete configmap postgres-secret
  kubectl delete deployment postgres
  kubectl delete service postgres
  kubectl delete pvc postgres-volume-claim
  kubectl delete pv postgres-volume
}

function create_config() {
  kubectl apply -f ./postgres-configmap.yaml
  kubectl apply -f ./psql-pv.yaml
  kubectl apply -f ./psql-claim.yaml
  kubectl apply -f ./ps-deployment.yaml
  kubectl apply -f ./ps-service.yaml
}

function monitor() {
  echo "checking PV..."
  kubectl get pv

  echo "checking PVC..."
  kubectl get pvc

  echo "checking pods..."
  kubectl get deployments

  echo "checking services..."
  kubectl get svc

  echo "checking pods..."
  kubectl get pods
}

function check_db_pod() {
  pod_name=`kubectl get pods|grep postgres|awk {'print $1'}`

  echo "Checking pod name..."
  echo $pod_name

  status=$(kubectl get pods $pod_name --no-headers -o custom-columns=":status.phase"|awk {'print $1'})

  while [ $status != 'Running' ]
  do
    echo "pod is starting..."
    sleep 1
    status=$(kubectl get pods $pod_name --no-headers -o custom-columns=":status.phase"|awk {'print $1'})
  done 

  echo $status
}


minikube stop
minikube start
cleanup
create_config
monitor
check_db_pod




