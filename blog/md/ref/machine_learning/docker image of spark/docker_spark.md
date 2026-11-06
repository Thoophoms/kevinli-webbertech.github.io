# Getting a Docker Image of Apache Spark

## 1. Install Docker

If you haven't installed Docker yet, download and install it from the official Docker website: [Docker Installation Guide]((https://docs.docker.com/desktop/install/windows-install/)).

## 2. Pull the Official Spark Image

You can pull the official Spark image by running the following command in your terminal:

```bash
 docker pull bitnami/spark
```

![docker_image_pull](https://kevinli-webbertech.github.io/blog/md/ref/machine_learning/docker%20image%20of%20spark/docker%20image%20pull.png)

This command pulls the Spark image maintained by **Bitnami**, which is a well-known provider of up-to-date and secure images.

## 3. Verify the Image

Once the image is pulled, you can verify it by listing the Docker images:

```bash
docker images
```

![docker_image](https://kevinli-webbertech.github.io/blog/md/ref/machine_learning/docker%20image%20of%20spark/docker%20image.png)

## 4. Running a Spark Container

```bash
   docker run -it --rm bitnami/spark spark-shell
```

![docker image run](https://raw.githubusercontent.com/kevinli-webbertech/kevinli-webbertech.github.io/refs/heads/main/blog/md/ref/machine_learning/docker%20image%20of%20spark/docker%20image%20run.png)

This will start a Spark shell inside the Docker container.
