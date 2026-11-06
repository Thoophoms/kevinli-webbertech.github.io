# What is NGINX in DevOps?

Nginx is mostly commonly known as a high-performance web server, but in DevOps, it's **frequently used as a reserver proxy and a load balancer.**
When we say "load balancer," we mean it takes traffic from clients (like user's browsers or mobile aps)
and forwards it to one of several backend servers running your application.

This helps with scaling, reliability, and availability. You don't want all users hitting a single
backend server -- that's a bottleneck and a single point of failure. NGINX helps solve that.

### Why is Load Balancing Important?

In today's world of microservices, containerization, and CI/CD pipelines,
you rarely have a single server running your application. You probably have:
- Multiple containers across several machines
- Dynamic service scaling (more instances during high traffic)
- A need to update code without downtime

**NGINX steps in as the gateway**, distributing traffic intelligently so that no single server is overloaded,
failed servers are skipped, and rolling deployments can happen without users noticing.

### How it Works (Conceptually)

Let's say you have three application instances:
- App Server 1 -> 192.168.1.101:3000
- App Server 2 -> 192.168.1.102:3000
- App Server 3 -> 192.168.1.103:3000

Instead of users going directly to one of those servers, they go to NGINX at https://yourdomain.com.
NGINX receives the request and forwards it to one of the backend servers using a rule like:
- Round Robin (rotate through the list)
- Least Connections (send to the server with the fewest active connections)
- IP Hash (same client always goes to the same server)

### Real-World Scenarios

1. **Microservices in Kubernetes**

When you have multiple services (auth, payment, users), you don't want each service exposed directly.
Instead, you use an **NGINX Ingress Controller** to:
- Termine SSL
- Route /login to the auth service, /checkout to the billing service
- Load balance across multiple pods per service

2. **Rolling Deployments (Blue-Green or Canary)**

You deploy a new version of your appy to just a fraction of traffic list:

upstream backend {
    server 192.168.1.10 weight=9; # old version
    server 192.168.1.11 weight=1; # new version
}

That means 10% of users hit the new version. If all goes well, you increase the weight.

3. **Failover and Redundancy**

NGINX can detect if one of your servers is down and reroute traffic to the backup:

upstream my_app {
    server 192.168.1.100;
    server 192.168.1.101 backup;
}

4. **Edge Routing in Global Applications**

If your app has servers in multiple regions, NGIXN can route users to the **nearest** one bassed on IP.
This reduces latency and improves user experience.

## How to Install and Use NGINX as a Load Balancer

### Step 1: Install NGINX

sudo apt update
sudo apt install nginx -y

![System Update](/blog/images/dev_ops/NGINX2/System_Update.PNG)

![NGINX Installation](/blog/images/dev_ops/NGINX2/NGINX_Installation.PNG)

Start it:

sudo systemctl start nginx
sudo systemctl enable nginx

![Starting NGINX](/blog/images/dev_ops/NGINX2/Powering_On_NGINX.PNG)

### Step 2: Create a Load Balancer Config

Edit or create the config file:

sudo nano /etc/nginx/conf.d/load-balancer.conf

![Creating the Config](/blog/images/dev_ops/NGINX2/Create_ConfigFile.PNG)

Here's a basic example:

upstream backend_servers {
    server 192.168.1.101:3000;
    server 192.168.1.102:3000;
    server 192.168.1.103:3000;
}

server {
    listen 80;

    location / {
        proxy_pass http://backend_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}


![Editing the Config File](/blog/images/dev_ops/NGINX2/Config_FIle.PNG)

Save and close the file.

### Step 3: Test and Reload

Check the config is valid

sudo nginx -t

![Check the config](/blog/images/dev_ops/NGINX2/Check_Valid_Config.PNG)

Reload:

sudo systemctl reload nginx

![Reload to save the changes](/blog/images/dev_ops/NGINX2/Reload.PNG)

**Why reload?** 

Whenever you modify NGINX configuration files --like adding/removing backend servers,
updating routing rules, or changing ports--you need to **reload** NGINX so it reads and applies the new config

Without a reload:
- NGINX will **keep running with the old config**
- Your changes won't take effect

But that's it. Your load balancer is now forwarding incoming requests to all your backend servers.

## Final Thought

NGINX is so widely used in DevOps because it strikes a great balance between simplicity,
power, and performance. Whether you're serving APIs to millions or just managing internal
tools for your team, NGINX as a load balancer is a rock-solid tool that plays nicely with
modern infrastructure, containers, and clout platforms.
