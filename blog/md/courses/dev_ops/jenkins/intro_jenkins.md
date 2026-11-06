# Introduction to Jenkins

## Installing Jenkins

### WAR file installation

>Note: War file is like a zip file.

The Jenkins WAR file was downloaded and executed locally. Please go to the following site to download,

https://www.jenkins.io/download/

We would like to stick to `LTS` (long-term support),

![download_jenkin.png](../../../../images/dev_ops/jenkins/download_jenkin.png)

On different platforms the installations are all different, for instance, I provide the installation in Ubuntu like below.

```
sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version
openjdk version "21.0.3" 2024-04-16
OpenJDK Runtime Environment (build 21.0.3+11-Debian-2)
OpenJDK 64-Bit Server VM (build 21.0.3+11-Debian-2, mixed mode, sharing)
```

>Note: If you are using windows, please use the windows installation guide.
> If you are using M chip Mac, please use podman to replace docker to avoid platform issues.
> 

* Long Term Support release

```commandline
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins
```

![jenkin_ubuntu.png](../../../../images/dev_ops/jenkins/jenkin_ubuntu.png)

## How to start Jenkins

Please follow instruction in the following tutorial page,

https://www.jenkins.io/doc/book/installing/linux/#debianubuntu

>Note: Due to the volatile content, we would like to stick to the most up2date information in the official document, 
> thus I do not provide anything on my own.

![war_jenkin_process.png](../../../../images/dev_ops/jenkins/war_jenkin_process.png)

and when we start it in the browser it shows something like the following,

![war_jenkin_process1.png](../../../../images/dev_ops/jenkins/war_jenkin_process1.png)

### Start Jenkins

You can enable the Jenkins service to start at boot with the command:

`sudo systemctl enable jenkins`

You can start the Jenkins service with the command:

`sudo systemctl start jenkins`

You can check the status of the Jenkins service using the command:

`sudo systemctl status jenkins`

If everything has been set up correctly, you should see an output like this:

```
Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
Active: active (running) since Tue 2018-11-13 16:19:01 +03; 4min 57s ago
```

### Docker Solution

#### Download and Run a Dockerized Jenkin

Documentation: https://github.com/jenkinsci/docker/blob/master/README.md

* The command to run Jenkins was.

`docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts`

![docker_jenkin1.png](../../../../images/dev_ops/jenkins/docker_jenkin1.png)

#### Get Jenkin Admin Password

For instance, I did the following to get the password,

```cmd
docker exec 2bb12f0da95749caad0682538148a540 cat /var/jenkins_home/secrets/initialAdminPassword
```

![docker_jenkin2.png](../../../../images/dev_ops/jenkins/docker_jenkin2.png)

After setting the password that appeared in the logs see above commands, you will see the next screen,

![docker_jenkin3.png](../../../../images/dev_ops/jenkins/docker_jenkin3.png)

Next screen,

![docker_jenkin4.png](../../../../images/dev_ops/jenkins/docker_jenkin4.png)

Click "continue as admin" and do not create the first admin, 

![docker_jenkin5.png](../../../../images/dev_ops/jenkins/docker_jenkin5.png)

Click "Save and Finish", and next screen,

![docker_jenkin6.png](../../../../images/dev_ops/jenkins/docker_jenkin6.png)

Then click "Start using Jenkins",

![docker_jenkin7.png](../../../../images/dev_ops/jenkins/docker_jenkin7.png)

#### Create a Freestyle Job

After finishing the initial setup, I created my first Jenkins job, which was a freestyle project that simply echoed a message.

Then follow the steps below and see how it works,

### Step 1

![docker_jenkin8.png](../../../../images/dev_ops/jenkins/docker_jenkin8.png)

### Step 2

![docker_jenkin9.png](../../../../images/dev_ops/jenkins/docker_jenkin9.png)

### Step 3

![docker_jenkin10.png](../../../../images/dev_ops/jenkins/docker_jenkin10.png)

### Step 4

![docker_jenkin11.png](../../../../images/dev_ops/jenkins/docker_jenkin11.png)

### Step 5

![docker_jenkin12.png](../../../../images/dev_ops/jenkins/docker_jenkin12.png)

Congratulations, your installation is working properly!

## Resources

Jenkins: <https://www.jenkins.io/doc>

Docker Hub Jenkins Image: <https://hub.docker.com/r/jenkins/jenkins>

Sample Project: <https://github.com/jenkins-docs/simple-java-maven-app>

GitHub Repo: <https://github.com/iiamolu/simple-java-maven-app>

---