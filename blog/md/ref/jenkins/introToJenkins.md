# Introduction to Jenkins

## Day 1 – Installing Jenkins and Creating My First Job

The Jenkins WAR file was downloaded and executed locally.

Started by setting up Jenkins using Docker:

![Jenkins setup screenshot](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*3vqP5FoKp1rr_wfS)

The command I used to run Jenkins was:

docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

After pulling the image and starting the Jenkins server, I accessed Jenkins through the browser using the localhost URL.

![Getting started: Instance configuration](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*fEjtkre6udi1mYIa)

### Create a Freestyle Project

After finishing the initial setup, I created my first Jenkins job, which was a freestyle project that simply echoed a message.

“Hello from Jenkins!”

![Console output](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*3DTBdONl-XruyZ_V)

The console output confirmed success. This was my first working Jenkins job!

## Day 2 – Maven Pipeline Configuration & GitHub Integration

On Day 2, I used a Maven-based Java project from GitHub to go from freestyle jobs to scripted pipelines.

In Jenkins, a `Spring Boot Hello World` project was used as the base for creating a Pipeline job.

GitHub Repo: <https://github.com/spring-guides/gs-spring-boot>


![Console output](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*gYw7oxetIpz8N9rf)

Created a Jenkinsfile and added it to my repo. It contained three main stages: Build, Test, and Deliver.

```
pipeline {
agent any
options {
skipStagesAfterUnstable()
}
tools {
maven ‘Maven 3.9.6’
}
stages {
stage(‘Build’) {
steps {
sh ‘mvn clean compile’
}
}
stage(‘Test’) {
steps {
sh ‘mvn test’
}
post {
always {
junit ‘target/surefire-reports/*.xml’
}
}
}
stage(‘Package’) {
steps {
sh ‘mvn package’
}
}
stage(‘Deliver’) {
steps {
sh ‘./jenkins/scripts/deliver.sh’
}
}
}
}
```

![My three failed attempts...](https://miro.medium.com/v2/resize:fit:786/format:webp/1*h2sBSI_hZms6VdAukapTfg.png)

After some troubleshooting (including fixing naming and Maven version issues), I successfully built the project and produced a .jar file.

![Build #4 status](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*enVxCjmZfr0agSH0YqS5-g.png)

## Day 3 – Testing, Debugging & Final Pipeline

Concentrated on incorporating automated testing into the pipeline on day three. There was already a JUnit-written test class in my Maven project. I modified the Jenkinsfile to execute `mvn test` and use the JUnit plugin to report the outcomes.

![Jenkinsfile](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*WA-EZCYSJfyeN0YDNFNcpg.png)

![Jenkinsfile2](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*q7PnUlyYrLEPGRtGvXR91g.png)

Here is the test stage I added to my Jenkinsfile:

stage(‘Test’) {
steps {
sh ‘mvn test’
}
post {
always {
junit ‘target/surefire-reports/TEST-*.xml’
}
}
}

After building the pipeline, I verified that the test results were collected and displayed under my Jenkins job.

![Test results](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*qUZ4fNd2kH_puksI)

Explored test result locations, checked the contents of `target/surefire-reports`, and validated my XML and TXT outputs.

Confirmed the JUnit plugin was properly installed:

![Installed plugins](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*jMIwJDM5GkxZlhQ1)

Both test cases passed, and Jenkins displayed a green success badge.

Also double-checked the status and artifacts for each pipeline build.

![Build #11 status](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*nqzS9s1xpn7KuQGu)

I was now aware of the connections between builds, tests, artifacts, and outputs. Jenkins has a lot of capability, but learning pipelines and test reporting takes effort. It’s important to consider console output rather than visual tabs for everything. Have patience; most issues are the result of small naming or syntax mistakes.

## Reflections

This three-day trip was both difficult and rewarding, as I went from being a complete newbie to using a Maven project in Jenkins to execute builds and tests.
I asked questions, made mistakes, and gained knowledge at every turn. Jenkins no longer seems so menacing.

I didn’t just learn Jenkins; I gained knowledge about DevOps workflows! Starting with code, testing automatically, and seeing results all in one tool has been eye-opening.

## Resources
**Oluchi Njoku's article:** <https://medium.com/@njokuol/learning-jenkins-my-3-day-adventure-as-a-beginner-devops-engineer-aacb1519ddba>

Jenkins: <https://www.jenkins.io/doc>

Docker Hub Jenkins Image: <https://hub.docker.com/r/jenkins/jenkins>

Sample Project: <https://github.com/jenkins-docs/simple-java-maven-app>

GitHub Repo: <https://github.com/iiamolu/simple-java-maven-app>

---