# Jenkins Image Troubleshooting

## Fix your Jenkinsfile

```
bash-3.2$ docker container ls
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                                              NAMES
0d27b7a9ce30   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   11 minutes ago   Up 11 minutes   0.0.0.0:8080->8080/tcp, 0.0.0.0:50000->50000/tcp   beautiful_kare
bash-3.2$ docker exec 0d27b7a9ce30 /bin/bash
bash-3.2$ ls
Applications			Movies				Virtual Machines.localized	minikube-darwin-amd64
Desktop				Music				VirtualBox VMs			ntws
Documents			Pictures			code				opt
Downloads			Postman				hawaii.sqlite			templates
Library				Public				linux_test			thinkorswim
Lightworks			PycharmProjects			linux_test2			videos
bash-3.2$ docker exec -it 0d27b7a9ce30 /bin/bash
```