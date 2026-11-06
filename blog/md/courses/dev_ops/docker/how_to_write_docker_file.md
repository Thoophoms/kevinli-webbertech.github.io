# Learning to write docker file

## Reviews

What we have learned previously, were the following topics,

* `docker pull` (download a docker image from docker.io)
* `docker run -d ...`, this is a command to run a docker image, if the image was not found in your local computer, it will go to do a `docker pull`.
* In the previous `Python App Deployment with Docker` we learn how to write a `flask` app in python and it is a simple web service deployed in docker.

We created a small python app in a few lines and built a docker image. And we run the docker image and we were able to see the following two goals,

* the website running
* using the `curl` command to query that the site is working and no 404 page.

## Today's goal

We will retrospect and inspect the docker file we provided earlier and see how that works.

`Dockerfile` used by python project

```Dockerfile
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```Dockerfile
# Stage 1: Build the application
FROM maven:3.8.7-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
# Download dependencies first (leverages Docker cache)
RUN mvn dependency:go-offline
COPY src ./src
# Package the application
RUN mvn clean package -DskipTests

# Stage 2: Create the runtime image
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Copy the built JAR from the builder stage
COPY --from=builder /app/target/*.jar app.jar

# Expose the port Spring Boot runs on
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
```
