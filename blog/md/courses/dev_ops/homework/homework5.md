# HW5 Podman Lab Report

*Requirements:*

* Provide a report in word/pdf format with all the screenshots of each step.
  Please do not use my images but use your own one.
* Please include the original questions/steps in your report.

Follow the in-class lab below and submit a lab report covering both parts:

- https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/podman/labs/podman_inclass_lab2.html

Grading breakdown:

* Part 1: Build `Dockerfile.javapython` from a base Ubuntu image, installing OpenJDK 21 and Python 3.12. (40 pts, 10 pts each)
  * Build the `javapython:21-3.12` image successfully. (10 pts)
  * Show `java -version` running successfully in the container. (10 pts)
  * Show `python3.12 --version` running successfully in the container. (10 pts)
  * Use a oneliner to print out the environment variables set by `ENV` in the `Dockerfile` (`JAVA_HOME` and `PATH`), e.g. `podman run --rm javapython:21-3.12 sh -c 'echo "JAVA_HOME=$JAVA_HOME" && echo "PATH=$PATH"'`. (10 pts)

* Part 2: Build `Dockerfile.combined` using the multi-stage build that copies layers from `eclipse-temurin:21-jdk` and `python:3.12-slim`. (40 pts, 10 pts each)
  * Build the `javapython-combined:21-3.12` image successfully. (10 pts)
  * Show `java -version` running successfully in the combined image. (10 pts)
  * Show `python3 --version` running successfully in the combined image. (10 pts)
  * Use a oneliner to print out the environment variables set by `ENV` in the `Dockerfile` (`JAVA_HOME` and `PATH`), e.g. `podman run --rm javapython-combined:21-3.12 sh -c 'echo "JAVA_HOME=$JAVA_HOME" && echo "PATH=$PATH"'`. (10 pts)

* Inspect the base images (`eclipse-temurin:21-jdk` and `python:3.12-slim`) and report which Linux distribution each one is built on (e.g. via `/etc/os-release`), and briefly explain why Part 2 copies only specific layers onto a plain Ubuntu base instead of using either image directly. (20 pts)
