# Springboot deployment with Kubernetes - Topic 3 Deploy Springboot to k8s

## Docker Container

A Docker container is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, libraries, dependencies, and configuration files. Docker containers are based on Docker technology, which allows developers to package their applications and all of their dependencies into a single container that can run consistently across different environments.

Key features of Docker containers include:

Isolation: Docker containers provide process and filesystem isolation, allowing applications to run in a sandboxed environment without interfering with other applications running on the same host.

Portability: Docker containers are portable and can run on any system that supports the Docker runtime, including laptops, servers, virtual machines, and cloud platforms. This portability makes it easy to develop, test, and deploy applications across different environments.

Efficiency: Docker containers are lightweight and use OS-level virtualization to share the host operating system's kernel, which reduces overhead and improves performance compared to traditional virtual machines.

Consistency: Docker containers encapsulate all of the dependencies and configuration required to run an application, ensuring consistent behavior across different environments and reducing the likelihood of "it works on my machine" issues.

Scalability: Docker containers are designed to be scalable and can be easily deployed and managed using container orchestration platforms like Kubernetes. This allows applications to scale up or down based on demand and ensures high availability and reliability.

Overall, Docker containers have revolutionized the way applications are packaged, distributed, and deployed, making it easier for developers to build, ship, and run software in a consistent and efficient manner.

## What is Kubernetes

Kubernetes is an open-source platform designed to automate deploying, scaling, and operating application containers. Originally developed by Google and now maintained by the Cloud Native Computing Foundation (CNCF), Kubernetes aims to provide a platform for automating the deployment, scaling, and operations of application containers across clusters of hosts. It provides a container-centric management environment and orchestrates computing, networking, and storage infrastructure on behalf of user workloads.

Kubernetes abstracts away the underlying infrastructure, allowing developers to deploy applications without worrying about the specific hardware or cloud provider details. It helps manage containerized applications by providing mechanisms for deployment, scaling, and resource management, ensuring that applications run consistently and reliably across different environments.

Key features of Kubernetes include:

1. **Container Orchestration**: Kubernetes automates the deployment, scaling, and management of containerized applications.

2. **Service Discovery and Load Balancing**: Kubernetes provides built-in mechanisms for service discovery and load balancing, allowing containers to communicate with each other and distributing traffic across multiple instances of an application.

3. **Self-healing**: Kubernetes automatically restarts containers that fail, replaces containers that become unresponsive, and kills containers that don't respond to user-defined health checks.

4. **Scaling**: Kubernetes can automatically scale the number of containers running an application based on CPU usage, memory consumption, or custom metrics.

5. **Rolling updates and Rollbacks**: Kubernetes supports rolling updates, allowing new versions of applications to be deployed with minimal downtime, and provides the ability to rollback to a previous version if needed.

6. **Resource Management**: Kubernetes allows users to specify the CPU and memory requirements for containers, ensuring that applications have access to the necessary resources while maximizing resource utilization.

7. **Storage Orchestration**: Kubernetes provides support for different types of storage solutions and allows users to mount storage volumes to containers.

Overall, Kubernetes has become the de facto standard for container orchestration in the cloud-native ecosystem, enabling organizations to build, deploy, and manage modern applications at scale.

## Installation of minikube (Linux version)

Note: For Mac and windows installation, please refer to the bottom of this tutorial and there is a link to 
[minikube](https://github.com/kubernetes/minikube).

* Download

`curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`

* Installation

`sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64`

![start minikube](https://kevinli-webbertech.github.io/blog/images/springboot/minikube.png)

* Run minikube

![start minikube](https://kevinli-webbertech.github.io/blog/images/springboot/minikube_dashboard.png)

Check dashboard

![start minikube](https://kevinli-webbertech.github.io/blog/images/springboot/minikube_dashboard_ui.png)

* Verify the pods/cluster information with `kubectl`

![start minikube](https://kevinli-webbertech.github.io/blog/images/springboot/kubectl.png)


* Check cluster info with `kubectl`

` kubectl cluster-info`

Then you will see the following,

![cluster info](https://kevinli-webbertech.github.io/blog/images/springboot/cluster_info.png)

## Operate your cluster

Run the following command,

```
$ kubectl cluster-info
Kubernetes master is running at https://127.0.0.1:46253
KubeDNS is running at https://127.0.0.1:46253/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

## Deploy Springboot Project in Docker

* Build your project

First, we create a Spring Boot application. Let us use our first example of the first class,

```

`git clone https://github.com/spring-guides/gs-spring-boot.git`

`cd into gs-spring-boot/complete`
```

You can then build the application:

`./mvnw clean install`

Then you can see the result of the build. If the build was successful, you should see a JAR file similar to the following:

```
ls -l target/*.jar
-rw-r--r-- 1 root root 19463334 Nov 15 11:54 target/spring-boot-complete-0.0.1-SNAPSHOT.jar
```

The JAR is executable:

`$ java -jar target/*.jar`

Then check your project,

`$ curl localhost:8080/actuator`

* Containerize the Application

There are multiple options for containerizing a Spring Boot application. As long as you are already building a Spring Boot jar file, you only need to call the plugin directly. The following command uses Maven:

`$ ./mvnw spring-boot:build-image`

The following command uses Gradle:

`$ ./gradlew bootBuildImage`

Here I use maven,

![build_docker_image](https://kevinli-webbertech.github.io/blog/images/springboot/build_docker_image.png)

Other than what the splash screen shows you about the docker image build was done. You could also use the following docker command to check it,

`docker image ls | grep spring-boot-complete`

Next, you can run the container locally:

`$ docker run -p 8080:8080 spring-boot-complete:0.0.1-SNAPSHOT`

It should look like below,

![run_docker_image](https://kevinli-webbertech.github.io/blog/images/springboot/run_docker_image.png)

Then you can check that it works in another terminal:

`$ curl localhost:8080/actuator/health`

You should see the following,

![test_docker_image](https://kevinli-webbertech.github.io/blog/images/springboot/test_docker_image.png)

* Push your image to docker, Nexus or JFrog

Note: Docker, Nexus, JFrog or Amazon ECR are the popular image repositories. Different companies use different solutions. As a student, you can use docker for now,

You **cannot** push the image unless you authenticate with Dockerhub (docker login), but there is already an image there that should work. Please register one yourself on docker.io. If you were authenticated, you could do the following,

```
$ docker tag spring-boot-complete:0.0.1-SNAPSHOT spring-boot-complete-0.0.1-SNAPSHOT
$ docker push spring-boot-complete:0.0.1-SNAPSHOT
```

## Deploy Docker Image to Kubernetes (Linux version)

* Creating configuration yaml file

```
$ kubectl create deployment demo --image=spring-boot-complete:0.0.1-SNAPSHOT --dry-run=client -o=yaml > deployment.yaml

$ echo --- >> deployment.yaml

$ kubectl create service clusterip demo --tcp=8080:8080 --dry-run=client -o=yaml >> deployment.yaml
```

* Deploying configuration

```
$ kubectl apply -f deployment.yaml
deployment.apps/demo created
service/demo created
```

* Testing the service is deployed

```
$ kubectl get all
NAME                       READY   STATUS             RESTARTS   AGE
pod/demo-cdc44c655-9sgvx   0/1     ImagePullBackOff   0          10s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/demo         ClusterIP   10.109.170.178   <none>        8080/TCP   10s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    5d3h

NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/demo   0/1     1            0           10s

NAME                             DESIRED   CURRENT   READY   AGE
replicaset.apps/demo-cdc44c655   1         1         0       10s
```

When you see the above `ImagePullBackOff` that means your image is not running. There is something wrong with it. It must be in `run` state to work.


![deploy_docker_image](https://kevinli-webbertech.github.io/blog/images/springboot/k8s_deployment.png)


Troubleshooting:

- For the image in the deployment.yaml to work, it has to pull from an image container.
- You will need to register a docker hub account, and push your docker image to the docker hub.

To push to your docker hub,

```
docker tag firstimage YOUR_DOCKERHUB_NAME/firstimage
docker push YOUR_DOCKERHUB_NAME/firstimage
```

firstimage: in my case, see the following command,
YOUR_DOCKERHUB_NAME: your login username of docker hub

```
docker tag spring-boot-complete:0.0.1-SNAPSHOT xlics05/spring-boot-complete:0.0.1-SNAPSHOT

docker push xlics05/spring-boot-complete:0.0.1-SNAPSHOT
```
See the following for detail,

![push docker image](https://kevinli-webbertech.github.io/blog/images/springboot/push_docker_image.png)

After I pushed the image, let us check the image is there,

![push docker image](https://kevinli-webbertech.github.io/blog/images/springboot/dockerhub_image.png)

Then change your image name in the `deployment.yaml`,

![deployment.yaml](https://kevinli-webbertech.github.io/blog/images/springboot/deployment_yaml.png)

Then re-run the following two commands to deploy it and check the pods,

```
kubectl apply -f deployment.yaml
kubectl get all
```

![check running pod](https://kevinli-webbertech.github.io/blog/images/springboot/check_running_pod.png)

Run the port-forwarding again,

![check running pod](https://kevinli-webbertech.github.io/blog/images/springboot/port_forwarding.png)

```
$ kubectl port-forward svc/demo 8080:8080
```

Now check the webservice's accurator with `curl`, let us open another terminal window,
and run the following command,

```
$ curl localhost:8080/actuator/health
{"status":"UP"}
```

![check running pod](https://kevinli-webbertech.github.io/blog/images/springboot/curl_testing.png)

## REF

- https://spring.io/guides/gs/spring-boot-kubernetes
- https://github.com/kubernetes/minikube
- https://minikube.sigs.k8s.io/docs/start/