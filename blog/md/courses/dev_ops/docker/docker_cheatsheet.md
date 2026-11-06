# Docker Cheatsheet

## Tag, push and pull images

Tag syntax,

```bash
docker tag <source_image>[:tag] <target_repo>/<image_name>[:tag]
```

Example, tagging a local image for your Docker Hub / private registry,

```bash
docker tag python:3.12-slim myrepo/python:3.12-slim
docker push myrepo/python:3.12-slim
docker pull myrepo/python:3.12-slim
```

Login to a registry first if it is private,

`docker login <registry_url>`

## Building image

`docker build --tag python:3.12-slim .`

`docker build --no-cache --tag python:3.12-slim .`

### Building with [Multiple]parameter[s]

A complete example,

To use it in another docker file, write a docker file,

```bash
ARG DCK_URL
ARG IMG_DIR
FROM ${DCK_URL}/${IMG_DIR}/python3:3.0.7
ENTRYPOINT ["/bin/bash"]
```

Build it with multiple params, you will need multiple `--build-arg`,

```bash
docker build -t python3:ml 
    --build-arg DCK_URL=$DCK_URL
    --build-arg IMG_DIR=$IMG_DIR
.
```

In reality, the url is your nexus url and the image dir is the repo you created.
In docker.io, it is url is `docker.io` and image is `/library/`.
For example, https://hub.docker.com/_/python

Run and test it,

```bash
xiaofengli@xiaofenglx:~/code/docker_image/ml$ docker run -it python:3.12-slim
[pythonuser@2507a4a1f071 ~]$ python --version
Python 3.11.7
```

## Running with container deletion upon exit

`docker run --rm -it python:3.12-slim`

## Running with inline entrypoint

`docker run --entrypoint bash jdk21:latest -c "ls"`

## Getting into docker container

`docker exec -it <container_name> bash`

## Run an image and mount local drive

`docker run -v /tmp/test:/opt/test --rm -it python:3.12-slim`

`docker run -v $PWD:/opt/test --rm -it python:3.12-slim`

### Volume mounting syntax

```bash
docker run -v <host_path_or_volume_name>:<container_path>:<options> <image>
```

* `host_path_or_volume_name` - an absolute path on the host, `$PWD`-relative path, or a named volume (e.g. `mydata`)
* `container_path` - the path inside the container where it should be mounted
* `options` - optional, comma separated, e.g. `ro` for read-only

Example using a named volume so data persists across container restarts,

```bash
docker volume create mydata
docker run -v mydata:/var/lib/mysql --rm -it mysql:8
```

## Delete a particular image

`docker image rm $(docker image ls |grep xvfb| awk '{print $3}')`

## Inspecting and managing containers

List running containers,

`docker ps`

List all containers (including stopped),

`docker ps -a`

View container logs,

`docker logs -f <container_name>`

Stop / start / restart a container,

```bash
docker stop <container_name>
docker start <container_name>
docker restart <container_name>
```

Inspect low-level details (IP, mounts, env vars) of a container or image,

`docker inspect <container_name_or_id>`

Copy files between host and container,

```bash
docker cp <container_name>:/opt/test/file.txt ./file.txt
docker cp ./file.txt <container_name>:/opt/test/file.txt
```

## Remove dangling images in Docker

`sudo docker image prune`

or you can do,

`sudo docker rmi $(sudo docker images -f "dangling=true" -q)`

If it is not working, then try,

`sudo sh -c 'docker rmi $(docker images -f "dangling=true" -q)'`

## Kill/remove all containers and images

Stop all running containers,

`docker kill $(docker ps -q)`

Stop and remove all containers (running and stopped),

`docker rm -f $(docker ps -aq)`

Remove all images,

`docker rmi -f $(docker images -aq)`

Nuke everything at once (containers, images, networks, build cache),

`docker system prune -a --volumes -f`

## CMD[] vs Entrypoint[]

* CMD spawn off new process
* Entrypoint uses the same process