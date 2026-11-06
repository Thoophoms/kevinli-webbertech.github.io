# Docker Lab1 - Build a Customized Linux Image

## Goal

In this lab, we will learn what is the base image, and how to combine a couple of different base images together and condense into one image.

The need for building a customized image is that a lot of time we would like to have our own tools set in our trustable based images, such as the enterprise-level images, or any images that is safe to use (being scanned or we know what it is) and we put trustable utilities in it and deliver such an image for customers to use. The customer here might be within the same organization or company.

## Step 1 - Prepare the Dockerfile

```dockerfile
FROM ubuntu:latest

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install common networking and system utilities
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    iputils-ping \
    net-tools \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*
```

## Step 2 - Build the docker image locally

```bash
docker build -t ubuntu_vim:24.0.3 .
```

## Step 3 - Test the local image

The following command will get you into the Linux container,

```bash
docker run -it xlics05/ubuntu24.0.3_vim:latest bash
```

For instance, you can do `which vim`, `which ping`, `which ifconfig` to check the utilities have been installed ok.

> **Note:** `xlics05` in the examples above is just my own Docker Hub username/namespace. Replace it with your own Docker Hub username throughout this lab - do not push to or use my namespace.

On the Docker Hub web UI, a repository is always shown as `<your_namespace>/<repository_name>` in the breadcrumb and title, e.g. `bitnami/mysql` where `bitnami` is the namespace:

![Docker Hub namespace example](/blog/images/dev_ops/docker/labs/dockerhub_namespace_example.png)

## Step 4 - Push the image to the docker.io repo

The following command will tag it properly to be able to push to the docker repo.

```bash
docker tag ubuntu_vim:24.0.3 xlics05/ubuntu24.0.3_vim
```

Before you push, you need to do the docker login,

```bash
docker login -u your_username
```

Note: Make sure you use the password and type it correctly or generate a token from the web portal.

Next, you can push your image,

```bash
docker push xlics05/ubuntu24.0.3_vim
```

## Step 5 - Test download and verify the image again

1. Remove the image first

```bash
docker image rm xlics05/ubuntu24.0.3_vim:latest
```

2. Download the image from your repo

```bash
docker pull xlics05/ubuntu24.0.3_vim:latest
```

3. Run into the linux container and test out some commands

```bash
docker run -it xlics05/ubuntu24.0.3_vim:latest bash
```

For instance, you can do `which vim`, `which ping`, `which ifconfig` to check the utilities have been installed ok.

Note: You can always login to your web portal to check your image that has been pushed. Please refer to my other tutorials or videos to check how to use the docker web portal.
