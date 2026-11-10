# Time Series Database

This is a lab to introduce you a new type of database, which is time-series database and it is built on top of relational database "Postgresql".

## TimescaleDB

![timescaledb_1](../../../../../images/dev_ops/k8s/timescaledb_1.png)

![timescaledb_2](../../../../../images/dev_ops/k8s/timescaledb_2.png)

### What is TimescaleDB

TimescaleDB is an extension for PostgreSQL that enables time-series workloads, increasing ingest, query, storage and analytics performance.

Best practice is to run TimescaleDB in a Timescale Service, but if you want to self-host you can run TimescaleDB yourself.

There are two versions of timescaledb,

* Cloud version - Commercial

* Community version - Open source version

In this tutorial, we would focus on the opensource/community version.

## Install TimescaleDB

There are two ways of using/installing the community version timescaled database,

* Install native version on your operating system. Please refer to the following url for guidance to install it.

- https://docs.timescale.com/self-hosted/latest/install/

* Use docker. Docker is a headless VM, and the pre-installed docker image would give us more flexibility and convenient to quickly put together the db without much configuration.

The tutorial in this document is based on the linux machine.

You can also use Mac or Windows machine and before the lab, we would like to.

### Container types

There are two container types store PostgreSQL data dir in different places, make sure you select the correct one to mount:

|Container|PGDATA location |
|---|---|
|timescaledb-ha|/home/postgres/pgdata/data|
|timescaledb|/var/lib/postgresql/data|

In this tutorial, we would use the `timescaledb-ha`.

### Docker running image

Before we start, we would like to make sure that `docker` or `docker desktop` is installed on your computer. For the detailed guidance on the installation, please refer to the following url,

https://docs.docker.com/engine/install/



* Download the TimescaleDB Docker image

```shell
docker pull timescale/timescaledb-ha:pg17
```

* Run the container

```shell
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg17
```

On UNIX based systems, Docker modifies Linux IP tables to bind the container. If your system uses Linux Uncomplicated Firewall (UFW), Docker may override your UFW port binding settings. To prevent this, add DOCKER_OPTS="--iptables=false" to /etc/default/docker.

* Connect to a database on your PostgreSQL instance

```commandline
psql -d "postgres://postgres:password@localhost/postgres"
```

* Check that TimescaleDB is installed

```commandline
\dx
```

Then we will see,

```commandline
List of installed extensions
Name         | Version |   Schema   |                                      Description
---------------------+---------+------------+---------------------------------------------------------------------------------------
plpgsql             | 1.0     | pg_catalog | PL/pgSQL procedural language
timescaledb         | 2.17.2  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition)
timescaledb_toolkit | 1.19.0  | public     | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
(3 rows)
```

If you want to access the container from the host but avoid exposing it to the outside world, you can bind to 127.0.0.1 instead of the public interface, using this command:

```shell
docker run -d --name timescaledb -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg17
```

If you don't want to install psql and other PostgreSQL client tools locally, or if you are using a Microsoft Windows host system, you can connect using the version of psql that is bundled within the container with this command:

```shell
docker exec -it timescaledb psql -U postgres
```

## Other docker usage

Existing containers can be stopped using `docker stop` and started again with `docker start` while retaining their volumes and data.

When you create a new container using the docker run command, by default you also create a new data volume. When you remove a Docker container with `docker rm` the data volume persists on disk until you explicitly delete it.

You can use the `docker volume ls` command to list existing docker volumes. If you want to store the data from your Docker container in a host directory, or you want to run the Docker image on top of an existing data directory, you can specify the directory to mount a data volume using the -v flag.

### Logs in docker container

If you have TimescaleDB installed in a Docker container, you can view your logs using Docker, instead of looking in /var/lib/logs or /var/logs.

### Ref

https://docs.timescale.com/self-hosted/latest/install/installation-docker/

## Install from source in linux

- Ubuntu

https://docs.timescale.com/self-hosted/latest/install/installation-linux/#add-the-timescaledb-extension-to-your-database

- Fedora

https://docs.timescale.com/self-hosted/latest/install/installation-linux/#add-the-timescaledb-extension-to-your-database

## Amazon AWS EC2

It is desirable to run a docker image on the EC2 instance, and we need to have a docker on it too.

### Install Docker (if not already installed)

`sudo yum install -y docker`

### Start a sample Docker image (e.g., a simple web server)

`docker run -d -p 80:8080 <image_name>:<tag>`

### Ref

https://aws.plainenglish.io/deploy-docker-image-to-aws-ec2-in-5-minutes-4cd7518feacc