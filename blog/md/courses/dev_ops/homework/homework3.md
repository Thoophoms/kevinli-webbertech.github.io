# HW3 Docker

Please include the original questions in your homework report. Please check out of syllabus for details or you will lose points.

1. Register an account in Docker.io (15 pts)
2. 
You need to provide your account info, not your password in your homework report.

2. Build a docker image and push to docker.io. (15 pts)

Follow the link of the following link, and read "Webapps with Docker".

https://docker-curriculum.com/#webapps-with-docker

Try to provide a `dockerfile` of your own. Submit this as part of your homework. This should be besides your pdf homework report.

3. Run your docker image in local. (15 pts)

4. Show your docker image is running. Please show both your docker image and your running container. (10 pts, each is 5 pts).

5. Show you can `exec` it is like ssh into your docker image. (10 pts)

6. Show you can delete your running container. (10 pts)

7. Show you can delete your image. (10 pts)

8. Try to reproduce pulling down the mysql docker image, and try to login to the image,

https://hub.docker.com/r/mysql/mysql-server/

```shell
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```

and prove that you can show some tables after you connect to the mysql instance running in the container. (15 pts)

