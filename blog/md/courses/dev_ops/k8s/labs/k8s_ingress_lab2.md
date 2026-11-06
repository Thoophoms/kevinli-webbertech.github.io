## K8s Ingress Lab2: Deploy Sample Apps

**Why?**

We'll simulate a **multi-service app** (e.g., a website with a blog and a store).

First we need to deploy the two apps we'll be using.

`kubectl create deployment webapp1 --image=xlics05/blog-shop`

`kubectl create deployment webapp2 --image=xlics05/blog-shop`

![Deploying the apps](/blog/images/dev_ops/k8s_ingress/deploy_apps.PNG)


* Make sure the ingress service is on

`minikube addons enable ingress`

`minikube addons list`

We then have to expose them internally.

`kubectl expose deployment webapp1 --port=8080 --target-port=8080`

`kubectl expose deployment webapp2 --port=8080 --target-port=8080`

![Exposing the apps](/blog/images/dev_ops/k8s_ingress/expose_apps.PNG)

**Key Points**
- expose creates ClusterIP Services (internal DNS names webapp 1 and webapp 2).
- Without Ingress, these are only accessible inside the cluster.

## Configure Ingress

**Why?**

We'll define rules like:
- myapp.local/blog -> webapp1
- myapp.local/shop -> webapp2

This is how companies route paths/subdomains to different teams' services.

![Entering the configuration](/blog/images/dev_ops/k8s_ingress/nano_ingress.PNG)

`touch ingress.yaml`

Paste:

```buildoutcfg
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  rules:
  - host: "myapp.local"  # Fake domain for testing
    http:
      paths:
      - path: /blog      # Route /blog to webapp1
        pathType: Prefix
        backend:
          service:
            name: webapp1
            port:
              number: 8080
      - path: /shop      # Route /shop to webapp2
        pathType: Prefix
        backend:
          service:
            name: webapp2
            port:
              number: 8080
```

![Inside of ingress](/blog/images/dev_ops/k8s_ingress/ingress_inside.PNG)

Make sure to then apply the settings.

`kubectl apply -f ingress.yaml`

![Applying the changes of ingress](/blog/images/dev_ops/k8s_ingress/nano_ingress_apply.PNG)

Lastly verify if everything went through.

![Verification](/blog/images/dev_ops/k8s_ingress/verify_ingress.PNG)

Checking services and IPs,

```buildoutcfg
bash-3.2$ kubectl get services
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP    6h36m
webapp1      ClusterIP   10.110.1.103   <none>        8080/TCP   54s
webapp2      ClusterIP   10.99.91.237   <none>        8080/TCP   47s
```

And ingress,

```buildoutcfg
bash-3.2$ kubectl get ingress
NAME              CLASS   HOSTS         ADDRESS        PORTS   AGE
example-ingress   nginx   myapp.local   192.168.49.2   80      63m
```

For every K8s object, you can use `describe`

```buildoutcfg
bash-3.2$ kubectl describe ingress
Name:             example-ingress
Labels:           <none>
Namespace:        default
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host         Path  Backends
  ----         ----  --------
  myapp.local  
               /blog   webapp1:8080 (10.244.0.13:8080)
               /shop   webapp2:8080 ()
Annotations:   nginx.ingress.kubernetes.io/proxy-connect-timeout: 30
               nginx.ingress.kubernetes.io/proxy-read-timeout: 3600
               nginx.ingress.kubernetes.io/proxy-send-timeout: 3600
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    47m (x4 over 64m)  nginx-ingress-controller  Scheduled for sync
```
## Step 4: Test Routing

**Why?**

We need to confirm traffic is routed correctly (just like debugging a real website).

Get the Ingress IP (Minikube)

![Ingress IP](/blog/images/dev_ops/k8s_ingress/ingress_ip.PNG)

Add to /etc/hosts (simulate DNS)

`echo "$(minikube ip) myapp.local" |sudo tee -a /etc/hosts`

![Simulate DNS](/blog/images/dev_ops/k8s_ingress/simulate_DNS.PNG)

**Test**

![Testing](/blog/images/dev_ops/k8s_ingress/ingress_test.PNG)

**Key Points**
- /etc/hosts trick your computer into thinking myapp.local points to Minikube
- Ingress reads the Host header and path to route requests (like a web server's virtual hosts).

## Part 5: Add HTTPS (TLS)

**Why?** 

Production apps **must** use HTTPS. Ingress centralizes TLS termination (no certs in Pods).

* Generate a self-signed cert (real apps use Let's Encrypt)

Copy the following commands and you will see the cert and key generated.

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048  -keyout tls.key -out tls.crt -subj “/CN=myapp.local”
```

Output is like the following,

```
kevinli@kevinli:~/git/k8s$ openssl req -x509 -nodes -days 365 -newkey rsa:2048  -keyout tls.key -out tls.crt -subj “/CN=myapp.local”
........+......+...+.........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+..............+......+.+...........+....+......+...+.....+......+.+.....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*..............+..........+........+.+............+.....+...+....+..+...+.+.....+......+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
......+...+...........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*......+..+.+......+......+..+...+....+......+...............+.....+.......+..+.........+.........+...+.............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*....+...+......+....+..+.......+..+....+.....+....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-----
req: subject name is expected to be in the format /type0=value0/type1=value1/type2=... where characters may be escaped by \. This name is not in that format: '“/CN=myapp.local”'
kevinli@kevinli:~/git/k8s$ ls
demo-app  ingress.yaml  -keyout  tls.key  webapp

```


* Store cert in kubernetes 

`
kubectl create secret tls myapp-tls --key ./tls.key --cert ./tls.crt
`

Output would be,

```
kevinli@kevinli:~/git/k8s$ kubectl create secret tls myapp-tls --key ./tls.key --cert ./tls.crt
secret/myapp-tls created
```

* Update the ingress.yaml to use TLS

![Update of ingress.yaml](/blog/images/dev_ops/k8s_ingress/nano_ingress_update.PNG)

```
Add:
spec:
  tls:
  - hosts:
    - myapp.local
    secretName: myapp-tls
```

![Updated version of ingress.yaml](/blog/images/dev_ops/k8s_ingress/ingress_inside_update.PNG)

* Apply the changes

`kubectl apply -f ingress.yaml`

![Application of changes](/blog/images/dev_ops/k8s_ingress/nano_ingress_apply_update.PNG)

### Test HTTPS

![Testing https](/blog/images/dev_ops/k8s_ingress/test_https.PNG)

 -k ignores self-signed cert warnings

## Part 6: Clean Up

**Why?**

Avoid leaving resources running (especially in cloud environments where they cost money).

![Cleanup](/blog/images/dev_ops/k8s_ingress/cleanup.PNG)


## Real-World Summary

Ingress = Traffic router (like NGINX for Kubernetes).
Why Use it?
- Path-based routing (/api, /app).
- Host-based routing (blog.example.com, shop.example.com).
- Centralized TLS (no cert management in Pods).
  - Used by companies like Spotify, Airbnb to manage microservices.
