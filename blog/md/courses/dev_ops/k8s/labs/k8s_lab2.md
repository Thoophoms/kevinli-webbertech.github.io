# Lab 2 Deploy an app and use Load Balancer

## Step 1: Create a Deployment

A **Deployment** in Kubernetes ensures that a specified number of pod replicas are running at all times.

Use the following command to deploy a simple Node.js web application using the `kubectl` CLI:

- `kubectl create deployment hello-node --image=kicbase/echo-server:1.0`

This creates a Deployment named hello-node using the previous docker image.

## Step 2: View the Deployment

Check the status of your deployment:

- `kubectl get deployments`

You should see output showing your deployment and the number of replicas.

## Step 3: View the Pod

Check the pods created by the Deployment:

- `kubectl get pods`

This command displays the pods that are running as part of your hello-node deployment.

## Step 4: Expose the Deployment

Expose the deployment as a Kubernetes Service so that it can be accessed externally:

- `kubectl expose deployment hello-node --type=LoadBalancer --port=8080`

This command creates a Service of type LoadBalancer and maps it to port 8080 of the deployment.

If you are using **Minikube**, use the following command to open the service in your default browser:

- `minikube service hello-node`

This will return a URL where you can access the application locally.

## Step 5: View the Application

To verify that your application is running, you can access it in a browser or use a command-line tool.

If you are using **Minikube**, run:

- `minikube service hello-node`

This will open the service URL in your browser and display the response from the echo server.

Alternatively, you can use `curl` to send a request to the application:

- `curl $(minikube service hello-node --url)`

This will output the HTTP headers returned by the application, confirming that it is running correctly.

## Step 6: Scale the Application

You can scale your application by increasing the number of pod replicas in the deployment.

Scaling is useful for improving availability and handling more user traffic. Running multiple replicas ensures that if one pod fails, others can continue to serve requests.

To scale the deployment to 4 replicas, run:

- `kubectl scale deployment hello-node --replicas=4`

To confirm that the new pods are running, use:

- `kubectl get pods`

You should see four pods listed, all managed by the same deployment.


## Ref

- https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/