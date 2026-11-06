# Docker Development Best Practices

* Start with an appropriate base image. For instance, if you need a JDK, consider basing your image on the official openjdk image, rather than starting with a generic ubuntu image and installing openjdk as part of the Dockerfile.

* Use multistage builds. For instance, you can use the maven image to build your Java application, then reset to the tomcat image and copy the Java artifacts into the correct location to deploy your app, all in the same Dockerfile. This means that your final image doesn’t include all of the libraries and dependencies pulled in by the build, but only the artifacts and the environment needed to run them.

If you need to use a version of Docker that does not include multistage builds, try to reduce the number of layers in your image by minimizing the number of separate RUN commands in your Dockerfile. You can do this by consolidating multiple commands into a single RUN line and using your shell’s mechanisms to combine them together. Consider the following two fragments. The first creates two layers in the image, while the second only creates one.

```dockerfile
RUN apt-get -y update
RUN apt-get install -y python
```

Do it in one liner,

```dockerfile
RUN apt-get -y update && apt-get install -y python
```

* If you have multiple images with a lot in common, consider creating your own base image with the shared components, and basing your unique images on that. Docker only needs to load the common layers once, and they are cached. This means that your derivative images use memory on the Docker host more efficiently and load more quickly.

* To keep your production image lean but allow for debugging, consider using the production image as the base image for the debug image. Additional testing or debugging tooling can be added on top of the production image.

* When building images, always tag them with useful tags which codify version information, intended destination (prod or test, for instance), stability, or other information that is useful when deploying the application in different environments. Do not rely on the automatically-created latest tag.

## Where and How to Persist Application Data

* Don’t use drives, use volume in production and use bind mounts in development image.

* For production, use secrets to store sensitive application data used by services, and use configs for non-sensitive data such as configuration files. If you currently use standalone containers, consider migrating to use single-replica services, so that you can take advantage of these service-only features.

## CICD

When push commits, integrate building docker image and push to the repository. Take this even further by requiring your development, testing, and security teams to sign images before they are deployed into production. This way, before an image is deployed into production, it has been tested and signed off by, for instance, development, quality, and security teams.

## Twelve-factor App Methodology

```dockerfile
docker build -t myimage:latest -<<EOF
FROM busybox
RUN echo "hello world"
EOF
```

Can be written as,

```sh
echo -e 'FROM busybox\nRUN echo "hello world"' | docker build -
```

## Build from a Local Build Context, Using a Dockerfile from stdin

```sh
docker build [OPTIONS] PATH | URL | -
```

Eg:

```sh
docker build .
docker build - < Dockerfile
docker build [OPTIONS] -f- PATH
```

## Create a Directory to Work In

```sh
mkdir example
cd example
touch somefile.txt
```

## Build an Image Using the Current Directory as Context, and a Dockerfile Passed Through stdin

```dockerfile
docker build -t myimage:latest -fs- . <<EOF
FROM busybox
COPY somefile.txt ./
RUN cat /somefile.txt
EOF
```

## Build from a Remote Build Context, Using a Dockerfile from stdin

```dockerfile
docker build -t myimage:latest -f- https://github.com/docker-library/hello-world.git <<EOF
FROM busybox
COPY hello.c ./
EOF
```

## Exclude with .dockerignore

To exclude files not relevant to the build, without restructuring your source repository, use a .dockerignore file.

## Use Multi-Stage Builds

A Dockerfile for a Go application could look like:

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.16-alpine AS build
# Install tools required for project
# Run `docker build --no-cache .` to update dependencies
RUN apk add --no-cache git
RUN go get github.com/golang/dep/cmd/dep
# List project dependencies with Gopkg.toml and Gopkg.lock
# These layers are only re-built when Gopkg files are updated
COPY Gopkg.lock Gopkg.toml /go/src/project/
WORKDIR /go/src/project/
# Install library dependencies
RUN dep ensure -vendor-only
# Copy the entire project and build it
# This layer is rebuilt when a file changes in the project directory
COPY . /go/src/project/
RUN go build -o /bin/project
# This results in a single layer image
FROM scratch
COPY --from=build /bin/project /bin/project
ENTRYPOINT ["/bin/project"]
CMD ["--help"]
```

You can use multiple FROM statements in your Dockerfile, and you can use a different base image for each FROM. You can also selectively copy artifacts from one stage to another, leaving behind things you don’t need in the final image. This can result in a concise final image.

## Decouple Applications

* Each container should have only one concern.
* Decoupling applications into multiple containers makes it easier to scale horizontally and reuse containers. For instance, a web application stack might consist of three separate containers, each with its own unique image, to manage the web application, database, and an in-memory cache in a decoupled manner.

## Minimize the Number of Layers

* Only the instructions RUN, COPY, ADD create layers. Other instructions create temporary intermediate images and don’t increase the size of the build.

## Sort Multi-Line Arguments

Whenever possible, ease later changes by sorting multi-line arguments alphanumerically. This helps to avoid duplication of packages and makes the list much easier to update. This also makes PRs a lot easier to read and review. Adding a space before a backslash (\) helps as well.

```dockerfile
RUN apt-get update && apt-get install -y \
    bzr \
    cvs \
    git \
    mercurial \
    subversion \
    && rm -rf /var/lib/apt/lists/*
```

## Leverage Build Cache

* Docker has cache and looks for images during build.
* To build off searching in cache. If you don’t want to use the cache at all, you can use the --no-cache=true option on the docker build command.

## Commands

**FROM**  
**RUN**  
**EXPOSE**  
**COPY**  
**WORKDIR**  
**ENTRYPOINT**  
**CMD**  
**ADD**  
**USER**

## FROM

Whenever possible, use current official images as the basis for your images. Docker recommends the Alpine image as it is tightly controlled and small in size (currently under 6 MB), while still being a full Linux distribution.

## RUN (External Commands)

Always combine RUN apt-get update with apt-get install in the same RUN statement. For example:

```dockerfile
RUN apt-get update && apt-get install -y \
    package-bar \
    package-baz \
    package-foo \
    && rm -rf /var/lib/apt/lists/*
```

Using apt-get update alone in a RUN statement causes caching issues and subsequent apt-get install instructions fail. For example, the issue will occur in the following Dockerfile:

```dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y curl
```

Using RUN apt-get update && apt-get install -y ensures your Dockerfile installs the latest package versions with no further coding or manual intervention. This technique is known as cache busting.

To get into the container, you can do `docker run -t -i --rm ubuntu bash`. In addition, when you clean up the apt cache by removing /var/lib/apt/lists it reduces the image size since the apt cache isn’t stored in a layer. Since the RUN statement starts with apt-get update, the package cache is always refreshed prior to apt-get install.

Official Debian and Ubuntu images automatically run `apt-get clean`, so explicit invocation is not required.

## Using Pipes

```dockerfile
RUN wget -O - https://some.site | wc -l > /number
RUN set -o pipefail && wget -O - https://some.site | wc -l > /number
```

## EXPOSE

The EXPOSE instruction indicates the ports on which a container listens for connections. Consequently, you should use the common, traditional port for your application. For example, an image containing the Apache web server would use EXPOSE 80, while an image containing MongoDB would use EXPOSE 27017 and so on.

## ENV

To make new software easier to run, you can use ENV to update the PATH environment variable for the software your container installs. For example:

```dockerfile
ENV PATH=/usr/local/nginx/bin:$PATH
```

ensures that `CMD ["nginx"]` just works.

Eg:

```dockerfile
ENV PG_MAJOR=9.3
ENV PG_VERSION=9.3.4
RUN curl -SL https://example.com/postgres-$PG_VERSION.tar.xz | tar -x

JC /usr/src/postgres && …
ENV PATH=/usr/local/postgres-$PG_MAJOR/bin:$PATH
```

Each ENV line creates a new intermediate layer, just like RUN commands. This means that even if you unset the environment variable in a future layer, it still persists in this layer and its value can be dumped. You can test this by creating a Dockerfile like the following, and then building it.

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
ENV ADMIN_USER="mark"
RUN echo $ADMIN_USER > ./mark
RUN unset ADMIN_USER
```

```sh
docker run --rm test sh -c 'echo $ADMIN_USER'
```

Output:

```
Mark
```

To prevent this, and really unset the environment variable, use a RUN command with shell commands, to set, use, and unset the variable all in a single layer. You can separate your commands with ; or &&.

This is usually a good idea. Using \ as a line continuation character for Linux Dockerfiles improves readability. You could also put all of the commands into a shell script and have the RUN command just run that shell script.

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN export ADMIN_USER="mark" \
    && echo $ADMIN_USER > ./mark \
    && unset ADMIN_USER
CMD sh
```

```sh
docker run --rm test sh -c 'echo $ADMIN_USER'
```

## ADD or COPY

Although ADD and COPY are functionally similar, generally speaking, COPY is preferred.

COPY only supports the basic copying of local files into the container, while ADD has some features (like local-only tar extraction and remote URL support) that are not immediately obvious. Consequently, the best use for ADD is local tar file auto-extraction into the image, as in ADD rootfs.tar.xz /.

```dockerfile
ADD https://example.com/big.tar.xz /usr/src/things/
RUN tar -xJf /usr/src/things/big.tar.xz -C /usr/src/things
RUN make -C /usr/src/things all
```

And instead, do something like:

```dockerfile
RUN mkdir -p /usr/src/things \
    && curl -SL https://example.com/big.tar.xz \
    | tar -xJC /usr/src/things \
    && make -C /usr/src/things all
```

For other items, like files and directories, that don’t require the tar auto-extraction capability of ADD, you should always use COPY.

## ENTRYPOINT

The best use for ENTRYPOINT is to set the image’s main command, allowing that image to be run as though it was that command, and then use CMD as the default flags. The following is an example of an image for the command line tool s3cmd:

```dockerfile
ENTRYPOINT ["s3cmd"]
CMD ["--help"]
```

You can use the following command to run the image and show the command’s help:

```sh
docker run s3cmd
```

Or, you can use the right parameters to execute a command, like in the following example:

```sh
docker run s3cmd ls s3://mybucket
```

The ENTRYPOINT instruction can also be used in combination with a helper script, allowing it to function in a similar way to the command above, even when starting the tool may require more than one step.

For example, the Postgres Official Image uses the following script as its ENTRYPOINT:

```bash
#!/bin/bash
set -e
if [ "$1" = 'postgres' ]; then
    chown -R postgres "$PGDATA"
    if [ -z "$(ls -A "$PGDATA")" ]; then
        gosu postgres initdb
    fi
    exec gosu postgres "$@"
fi
exec "$@"
```

This script uses the `exec` Bash command so that the final running application becomes the container’s PID 1. This allows the application to receive any Unix signals sent to the container. In the following example, the helper script is copied into the container and run via ENTRYPOINT on container start:

```dockerfile
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["postgres"]
```

It can simply start Postgres:

```sh
docker run postgres
```

Or, it can be used to run Postgres and pass parameters to the server:

```sh
docker run postgres postgres --help
```

## USER

If a service can run without privileges, use USER to change to a non-root user. Start by creating the user and group in the Dockerfile with something like the following example:

```dockerfile
RUN groupadd -r postgres && useradd --no-log-init -r -g postgres postgres
```

Avoid installing or using sudo as it has unpredictable TTY and signal-forwarding behavior that can cause problems. If you absolutely need functionality similar to sudo, such as initializing the daemon as root but running it as non-root, consider using “gosu”. Lastly, to reduce layers and complexity, avoid switching USER back and forth frequently.

## ONBUILD

An ONBUILD command executes after the current Dockerfile build completes. ONBUILD executes in any child image derived FROM the current image. Think of the ONBUILD command as an instruction that the parent Dockerfile gives to the child Dockerfile. A Docker build executes ONBUILD commands before any command in a child Dockerfile.

## WORKDIR

For clarity and reliability, you should always use absolute paths for your WORKDIR. Also, you should use WORKDIR instead of proliferating instructions like `RUN cd … && do-something`, which are hard to read, troubleshoot, and maintain.

## Rebuild Images

Avoid the following and get a version tag,

```dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu:latest
RUN apt-get -y update && apt-get install -y python
```

Recommended using --no-cache

```sh
docker build --no-cache -t myImage:myTag myPath/
```

## VOLUME

The VOLUME instruction should be used to expose any database storage area, configuration storage, or files and folders created by your Docker container. You are strongly encouraged to use VOLUME for any combination of mutable or user-serviceable parts of your image.

```sh
docker volume create todo-db
docker run -dp 3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started
```

Start the todo app container, but add the --mount option to specify a volume mount. We will give the volume a name and mount it to /etc/todos in the container, which will capture all files created at the path.

Dive into the volume:

```sh
docker volume inspect command

docker volume inspect todo-db
```

```json
[
    {
        "CreatedAt": "2019-09-26T02:18:36Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/todo-db/_data",
        "Name": "todo-db",
        "Options": {},
        "Scope": "local"
    }
]
```

## Quick Volume Type Comparisons

The following table outlines the main differences between volume mounts and bind mounts.

|                                                  | Named volumes                                      | Bind mounts                                          |
|--------------------------------------------------|----------------------------------------------------|------------------------------------------------------|
| **Host location**                                | Docker chooses                                     | You decide                                           |
| **Mount example** (using `--mount`)              | `type=volume,src=my-volume,target=/usr/local/data` | `type=bind,src=/path/to/data,target=/usr/local/data` |
| **Populates new volume with container contents** | Yes                                                | No                                                   |
| **Supports Volume Drivers**                      | Yes                                                | No                                                   |



Eg:

```sh
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash
```

The --mount option tells Docker to create a bind mount, where src is the current working directory on your host machine (getting-started/app), and target is where that directory should appear inside the container (/src).

--mount is equivalent to -v(--volume)

```sh
docker run -d \
  -it \
  --name devtest \
  -v "$(pwd)"/target:/app \
  nginx:latest
```

Is equivalent to,

```sh
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app \
  nginx:latest
```

* **--mount**: Consists of multiple key-value pairs, separated by commas and each consisting of a `<key>=<value>` tuple. The --mount syntax is more verbose than -v or --volume, but the order of the keys is not significant, and the value of the flag is easier to understand.
    * The type of the mount, which can be bind, volume, or tmpfs. This topic discusses bind mounts, so the type is always bind.
    * The source of the mount. For bind mounts, this is the path to the file or directory on the Docker daemon host. May be specified as source or src.
    * The destination takes as its value the path where the file or directory is mounted in the container. May be specified as destination, dst, or target.
    * The readonly option, if present, causes the bind mount to be mounted into the container as read-only.
    * The bind-propagation option, if present, changes the bind propagation. May be one of rprivate, private, rshared, shared, rslave, slave.
    * The --mount flag does not support z or Z options for modifying selinux labels.
    * If you use -v or --volume to bind-mount a file or directory that does not yet exist on the Docker host, -v creates the endpoint for you. It is always created as a directory.
    * If you use --mount to bind-mount a file or directory that does not yet exist on the Docker host, Docker does not automatically create it for you but generates an error.

After running the command, Docker starts an interactive bash session in the root directory of the container’s filesystem.

```sh
root@ac1237fad8db:/# pwd
root@ac1237fad8db:/# ls
bin   dev  home  media  opt   root 

 sbin  srv  tmp  var
boot  etc  lib   mnt    proc  run   src   sys  usr
```

Now, change directory in the src directory. This is the directory that you mounted when starting the container. Listing the contents of this directory displays the same files as in the getting-started/app directory on your host machine.

```sh
root@ac1237fad8db:/# cd src
root@ac1237fad8db:/src# ls
```

Create a new file named myfile.txt.

```sh
root@ac1237fad8db:/src# touch myfile.txt
root@ac1237fad8db:/src# ls
Dockerfile  myfile.txt  node_modules  package.json  spec  src  yarn.lock
```

Then check in hosting os. Now if you open this directory on the host, you’ll see the myfile.txt file has been created in the directory.

## Run Your App in a Development Container

* Mount our source code into the container
* Install all dependencies
* Start nodemon to watch for filesystem changes

```sh
docker run -dp 3000:3000 \
    -w /app --mount type=bind,src="$(pwd)",target=/app \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"
```

```sh
docker logs <container-id>
```

# Container Networking

## Start MySQL

### Create the Network

```sh
$ docker network create todo-app
```

```sh
docker run -d \
  --network todo-app --network-alias mysql \
  -v todo-mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=todos \
  mysql:8.0
```

### SSH to the Docker MySQL Image

```sh
docker exec -it <mysql-container-id> mysql -u root -p
```

Inside the container, you’re going to use the `dig` command, which is a useful DNS tool. You’re going to look up the IP address for the hostname `mysql`.

```sh
dig mysql
docker run -it --network todo-app nicolaka/netshoot
```

Specify each of the environment variables above, as well as connect the container to your app network

```sh
docker run -dp 3000:3000 \
  -w /app -v "$(pwd):/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:18-alpine \
  sh -c "yarn install && yarn run dev"
```

Start a MySQL container and attach it to the network.

## Docker Compose

Docker Compose is a tool that was developed to help define and share multi-container applications. With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.

At the root of the `/getting-started/app` folder, create a file named `docker-compose.yml`.

In the compose file, we’ll start off by defining the list of services (or containers) we want to run as part of our application.

### Install Docker Compose

To install Docker Compose and check the version info:

```sh
docker compose version
```

We’ll migrate both the working directory (`-w /app`) and the volume mapping (`-v "$(pwd):/app"`) by using the `working_dir` and `volumes` definitions. Volumes also have a short and long syntax. One advantage of Docker Compose volume definitions is we can use relative paths from the current directory.

### Multiple Services in Docker Compose

#### Define the App Service

```sh
docker run -dp 3000:3000 \
  -w /app -v "$(pwd):/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:18-alpine \
  sh -c "yarn install && yarn run dev"
```

Convert to the following:

```yaml
services:
  app:
    image: node:18-alpine
    command: sh -c "yarn install && yarn run dev"
    ports:
      - 3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos
```

#### Define the MySQL Service

```sh
docker run -d \
  --network todo-app --network-alias mysql \
  -v todo-mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=todos \
  mysql:8.0
```

Convert to the following:

```yaml
services:
  mysql:
    image: mysql:8.0
    volumes:
      - todo-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: todos
volumes:
  todo-mysql-data:
```

### Run the Application Stack

Start up the application stack using the `docker compose up` command. We’ll add the `-d` flag to run everything in the background.

```sh
docker compose up -d
```

When we run this, we should see output like this:

```sh
Creating network "app_default" with the default driver
Creating volume "app_todo-mysql-data" with default driver
Creating app_app_1   ... done
Creating app_mysql_1 ... done
```

### Commands

```sh
docker compose up -d
docker compose logs -f
docker compose down
```

## Image Layering

```sh
docker image history getting-started
```

You’ll notice that several of the lines are truncated. If you add the `--no-trunc` flag, you’ll get the full output.

```sh
docker image history --no-trunc getting-started
```

Once a layer changes, all downstream layers have to be recreated as well.

```dockerfile
# syntax=docker/dockerfile:1
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
```

To improve the layer, then, we only recreate the yarn dependencies if there was a change to the package.json. Make sense?

```dockerfile
# syntax=docker/dockerfile:1
FROM node:18-alpine
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --production
COPY . .
CMD ["node", "src/index.js"]
```

Create a file named `.dockerignore` in the same folder as the Dockerfile with the following contents.

```
node_modules
```

Build a new image using docker build.

```sh
$ docker build -t getting-started .
```

Now, make a change to the `src/static/index.html` file (like change the `<title>` to say “The Awesome Todo App”).

Build the Docker image now using `docker build -t getting-started .` again. This time, your output should look a little different.

```sh
[+] Building 1.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 37B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/node:18-alpine
 => [internal] load build context
 => => transferring context: 450.43kB
 => [1/5] FROM docker.io/library/node:18-alpine
 => CACHED [2/5] WORKDIR /app
 => CACHED [3/5] COPY package.json yarn.lock ./
 => CACHED [4/5] RUN yarn install --production
 => [5/5] COPY . .
 => exporting to image
 => => exporting layers
 => => writing image sha256:91790c87bcb096a83c2bd4eb512bc8b134c757cda0bdee4038187f98148e2eda
 => => naming to docker.io/library/getting-started
```

### Build and Run

```sh
docker build -t getting-started .
docker run -dp 3000:3000 getting-started
```

You use the `-d` flag to run the new container in “detached” mode (in the background). You also use the `-p` flag to create a mapping between the host’s port 3000 to the container’s port 3000. Without the port mapping, you wouldn’t be able to access the application.

```sh
docker ps
docker stop <the-container-id>
docker rm <the-container-id>
```

### Lab 1: Create Image and Run Locally

```sh
git clone https://github.com/docker/getting-started.git
touch Dockerfile
```

Dockerfile:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
```

### Lab 2: Share Application

1. Create a Repo

To push an image, you first need to create a repository on Docker Hub. Sign up or Sign in to Docker Hub.

2. Push the Image

```sh
docker push docker/getting-started
```

Why did it fail? The push command was looking for an image named `docker/getting-started`, but didn’t find one. If you run `docker image ls`, you won’t see one either.

To fix this, you need to “tag” your existing image you’ve built to give it another name.

3. Login to Docker Hub

```sh
docker login -u YOUR-USER-NAME
```

4. Tag and Push the Image

```sh
$ docker tag getting-started YOUR-USER-NAME/getting-started
docker push YOUR-USER-NAME/getting-started
```

Visit [Play with Docker](https://labs.play-with-docker.com/).

Select Login and then select Docker from the drop-down list.

Add New Instance:

```sh
$ docker run -dp 3000:3000 YOUR-USER-NAME/getting-started
```

### Lab 3: Container File System

```sh
docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"
```

Use `docker ps` to get it.

```sh
docker exec <container-id> cat /data.txt
docker run -it ubuntu ls /
```

### Multi-Stage Builds (Maven/Tomcat Example)

```dockerfile
# syntax=docker/dockerfile:1
FROM maven AS build
WORKDIR /

app
COPY . .
RUN mvn package
FROM tomcat
COPY --from=build /app/target/file.war /usr/local/tomcat/webapps
```

In this example, we use one stage (called build) to perform the actual Java build using Maven. In the second stage (starting at `FROM tomcat`), we copy in files from the build stage. The final image is only the last stage being created (which can be overridden using the `--target` flag).

```dockerfile
# syntax=docker/dockerfile:1
FROM node:18 AS build
WORKDIR /app
COPY package* yarn.lock ./
RUN yarn install
COPY public ./public
COPY src ./src
RUN yarn run build
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
```

## Docker, Docker Compose, and ECS

AWS uses a fine-grained permission model, with specific roles for each resource type and operation.

To ensure that Docker ECS integration is allowed to manage resources for your Compose application, you have to ensure your AWS credentials grant access to the following AWS IAM permissions:

* application-autoscaling:*
* cloudformation:*
* elasticloadbalancing:*
* servicediscovery:*
* iam:Full
* ec2:Full
* logs:Full
* route53:Full

### Create AWS Context

Run the `docker context create ecs myecscontext` command to create an Amazon ECS Docker context named `myecscontext`.

If you have already installed and configured the AWS CLI, the setup command lets you select an existing AWS profile to connect to Amazon.

Finally, you can configure your ECS context to retrieve AWS credentials by AWS_* environment variables, which is a common way to integrate with third-party tools and single-sign-on providers.

After you have created an AWS context, you can list your Docker contexts by running the `docker context ls` command:

```sh
NAME                TYPE                DESCRIPTION                               DOCKER ENDPOINT               KUBERNETES ENDPOINT   ORCHESTRATOR
myecscontext        ecs                 credentials read from environment
default *           moby                Current DOCKER_HOST based configuration   unix:///var/run/docker.sock                         swarm
```

### Run a Compose Application

Ensure you are using your ECS context. You can do this either by specifying the `--context myecscontext` flag with your command, or by setting the current context using the command `docker context use myecscontext`.

```sh
docker compose --file mycomposefile.yaml up
```

Fetch logs for the application in the current working directory:

```sh
$ docker compose logs
```

Specify compose project name:

```sh
$ docker compose --project-name PROJECT logs
```

Specify compose file:

```sh
$ docker compose --file /path/to/docker-compose.yaml logs
```

The Compose file model does not define any attributes to declare auto-scaling conditions. Therefore, we rely on `x-aws-autoscaling` custom extension to define the auto-scaling range, as well as cpu or memory to define target metric, expressed as resource usage percent.

```yaml
services:
  foo:
    deploy:
      x-aws-autoscaling:
        min: 1
        max: 10 # required
        cpu: 75
        # mem: - mutually exclusive with cpu
```

### IAM Roles

Your ECS Tasks are executed with a dedicated IAM role, granting access to AWS Managed policies `AmazonECSTaskExecutionRolePolicy` and `AmazonEC2ContainerRegistryReadOnly`. In addition, if your service uses secrets, IAM Role gets additional permissions to read and decrypt secrets from the AWS Secret Manager. You can grant additional managed policies to your service execution by using `x-aws-policies` inside a service definition:

```yaml
services:
  foo:
    x-aws-policies:
      - "arn:aws:iam::aws:policy/AmazonS3FullAccess"
```

You can also write your own IAM Policy Document to fine-tune the IAM role to be applied to your ECS service and use `x-aws-role` inside a service definition to pass the yaml-formatted policy document.

```yaml
services:
  foo:
    x-aws-role:
      Version: "2012-10-17"
      Statement:
        - Effect: "Allow"
          Action:
            - "some_aws_service"
          Resource:
            - "*"
```

### Install the Docker Compose CLI on Linux

```sh
curl -L https://raw.githubusercontent.com/docker/compose-cli/main/scripts/install/install_linux.sh | sh
```

## Appendix

### Deploy Java Program

```dockerfile
FROM openjdk:11
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN javac Main.java
CMD ["java", "Main"]
```

```sh
$ docker build -t my-java-app .
$ docker run -it --rm --name my-running-app my-java-app
```

* `--rm`: Automatically remove the container when it exits.
* `--workdir , -w`: Working directory inside the container.
* `--tty , -t`: Allocate a pseudo-TTY.
* `--rm`: Automatically remove the container when it exits.

### Volumes Example

Dockerfile:

```dockerfile
FROM ubuntu:18.04
RUN apt-get update && \
apt-get install -y curl
```

```sh
docker run -it -v “$pwd”:/tmp/test -w /tmp/test ubuntu ls
```

### References

* [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
* [Entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint)
* [Docker ECS Integration](https://docs.docker.com/cloud/ecs-integration/)