# Final Kubernetes Deployment

Please include the original questions in your homework report. Please check out of syllabus for details or you will lose points.

K8s here we can use `minikube`.

## Tasks

Write a springboot helloworld project and that could connect to a mysql database and commit to github. (hint: please go to checkout in spring.io)

* Write a k8s deployment for Jenkins server. (10 pts)
* Write a k8s deployment for Nexus server. (10 pts)
* Write a k8s deployment for MySQL database. (10 pts)
* Write a k8s ConfigMap for MySQL username and password. (10 pts)
* Write a Jenkins file to checkout code, build jar and push it to nexus server. (10 pts)
* Write a k8s webapp deployment file to spin up the pod to run the webapp. And prove that the webapp is running successfully. (10 pts)
* Write a k8s PV deployment file. (10 pts)
* Write a k8s PVC deployment file. (10 pts)
* Write a service file. (10 pts)
* Write a shell script where you can check all your configMap, deployments and services and this is the final script where you can start your minikube cluster and deploy everything automatically. (10 pts)
