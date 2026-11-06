# Reverse proxying your apps to the same port with Nginx

Recall that in the previous session, we learned `podman` to pull `nginx` docker image. 

In the following steps, you will pull the image to your local system, if you haven't.


```shell

$ podman pull docker.io/library/nginx
```

Then you check image exists. 

`$ podman image ls`

Then we create a directory,

`$ mkdir nginx`

Inside this directory, create three different files:

* The default.conf file, which holds the default Nginx configuration
* The syscom.conf file, which holds the configuration for the sysadmin.com application 
* The sysorg.conf file, which holds the configuration for the sysadmin.org application

For each domain, use server_name to define the domain and proxy_pass to map the container, also specifying the IP address of the host machine and the mapped port for each container. Now all of them are going to listen on the 80 port using your reverse proxy as a gateway:

```commandline
$ cat << EOF > default.conf
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

}
EOF

$ cat << EOF > syscom.conf
server {
  listen 80;
  server_name sysadmin.com;

  location / {
    proxy_pass http://192.168.1.30:8080;
  }
}
EOF

$ cat << EOF > sysorg.conf
server {
  listen 80;
  server_name sysadmin.org;

  location / {
    proxy_pass http://192.168.1.30:8081;
  }
}
EOF
```

Making this work requires taking advantage of the include /etc/nginx/conf.d/*.conf parameter of the /etc/nginx/nginx.conf file inside the Nginx container, which allows loading modular configuration files inside from the /etc/nginx/conf.d/ directory. When it runs, these files will be mounted in this directory inside the container.

Now it's time to run the Nginx container with the proper parameters. The first time you run it, however, especially running rootless containers, you may receive the following error message:

```commandline
$ podman run --name=nginx -p 80:80 -v $HOME/nginx:/etc/nginx/conf.d:Z -d docker.io/library/nginx
Error: rootlessport cannot expose privileged port 80, you can add 'net.ipv4.ip_unprivileged_port_start=80' to /etc/sysctl.conf (currently 1024), or choose a larger port number (>= 1024): listen tcp 0.0.0.0:80: bind: permission denied
```

This is a standard and expected security measure. To work around this and allow the Nginx container to run using the low port 80 at runtime, run:

```commandline
$ sudo sysctl net.ipv4.ip_unprivileged_port_start=80
net.ipv4.ip_unprivileged_port_start = 80
```

>Hint:
> Siren alert: Proceed with this setting cautiously, as it could create a vulnerability. After the container runs, you can return this setting to the default value of 1024.

Now run the container again and see what happens:

```commandline
$ podman run --name=nginx -p 80:80 -v $HOME/nginx:/etc/nginx/conf.d:Z -d docker.io/library/nginx
a6575989327eb14b9d980505832e8b5600e17248667feba487c38c1792274b99

$ podman ps
CONTAINER ID  IMAGE                           COMMAND               CREATED         STATUS         PORTS                 NAMES  
a6575989327e  docker.io/library/nginx:latest  nginx -g daemon o...  29 seconds ago  Up 28 seconds  0.0.0.0:80->80/tcp    nginx
```

Nice, it's running! Perform a simple test by trying to curl both of the apps' domains without specifying the higher ports and see if they both respond in port 80, like this:

```commandline
$ curl localhost
<html>
  <header>
    <title>SysAdmin.com</title>
  </header>
  <body>
    <p>This is the SysAdmin website hosted on the .com domain</p>
  </body>
</html>
```
