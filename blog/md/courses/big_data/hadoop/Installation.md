# Build Docker Image

In this tutorial or lab we will show you how to play around with docker image and we will use some simple Java code to compile and run to test our docker image.

In the next section of this class, we will directly run a dockerized hadoop image and explore hadoop's feature.

## Install and configure hadoop docker image

**Step 1 Create a java source file**

In intelliJ or VisualStudio Code, create a project, and in your project folder,   make the following file,

```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String args[])
    {
        System.out.println("Hello, World");
    }
}
```

**Step 2 Create a docker file**

Create a docker file  called “Dockerfile”

```docker
FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y openjdk-8-jdk
WORKDIR /app
ADD HelloWorld.java .
RUN javac -source 8 -target 8 HelloWorld.java -d .
FROM ubuntu/jre:8-22.04_edge
WORKDIR /
COPY --from=builder /app/HelloWorld.class .
CMD [ "HelloWorld" ]
```

**Step 3 Build docker image**

Then you will open git bash in your windows, in linux or Mac, just use your terminal, you can type the following command,

`docker build -t  my-hadoop-container:latest .`

Or you put that above command into a bash script, called “build.sh”, and it looks like the following,

```bash
#!/bin/bash
docker build -t my-hadoop-container
```

Now the folder structure looks like the following,

![folders](https://kevinli-webbertech.github.io/blog/images/big_data/hadoop/folders.png)

and then run the script by doing `./build.sh`.

Then the image should be built, and we will check the image is ok or not in the next step,

**Step 4 Test docker container**

To Test your container, and run the container

`docker image ls`

![docker_image](https://kevinli-webbertech.github.io/blog/images/big_data/hadoop/docker_image.png)

Then do the following to test docker image,

`docker run -it my-hadoop-container`

![docker_image](https://kevinli-webbertech.github.io/blog/images/big_data/hadoop/test_docker_image.png)

Once you build the above image, you will go into the image, and do the following,

`docker exec -it container_id  /bin/bash`