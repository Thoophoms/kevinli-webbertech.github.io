# What is a ConfigMap and Why Does It Matter?

In real-world applications, it's common to separate configuration from the application code. For example:

- A web app may need different database URLs for dev, test, and production.
- You shouldn't have to rebuild your app every time you change a setting.

Kubernetes ConfigMap is designed for this exact purpose. It lets your store configuration in a key-value format
and inject it into your app at runtime -- either as environment variables or files inside the container.

### Real-World Analogy

Think of a ConfigMap as a notebook of environment settings your app reads from:

- Instead of baking this notebook inside your app, Kubernetes lets you deliver it next to your app, making everything more modular, reusable, and secure.

# Step 0: Set Up Your Environment

Install Prerequisites on macOS

1. Install Homebrew (if you don't already have it)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

![Installation of Homebrew](/blog/images/dev_ops/k8s_configmap/Install_Homebrew.png)


2. Install kubectl (Kubernetes CLI)

```
brew install kubectl
```

![Installation of kubectl](/blog/images/dev_ops/k8s_configmap/Install_kubectl.png)


✅ Verify:

```
kubectl version --client
```

![Verify installation of kubectl](/blog/images/dev_ops/k8s_configmap/Verify_kubectl.png)


3. Install minikube (Local K8s Cluster)

```
brew install minikube
```

![Installation of minikube](/blog/images/dev_ops/k8s_configmap/Install_minikube%20.PNG)


✅ Start a cluster:

```
minikube start
```

![Starting a minikube cluster](/blog/images/dev_ops/k8s_configmap/Start_cluster.png)


# Step 1: Create Your First ConfigMap (Key-Value Style)

We'll create a ConfigMap that holds some basic configuration for a web application.

```
kubectl create configmap app-config \
  --from-literal=ENV=production \
  --from-literal=VERSION=1.0.0
```

![Creation of ConfigMap](/blog/images/dev_ops/k8s_configmap/Create_ConfigMap%20.PNG)

### Explanation:

- kubectl create configmap --> creates a ConfigMap resource
- --from-literal --> sets a key-value pair directly
- app-config --> name of the ConfigMap

✅ View the config map:

```
kubectl get configmap app-config -o yaml
```

![View of the ConfigMap](/blog/images/dev_ops/k8s_configmap/View_ConfigMap%20.PNG)

# Step 2: Use ConfigMap as Environment Variables in a Pod

Create a YAML file called env-pod.yaml:

```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-env-pod
spec:
  containers:
  - name: test-container  # <- THIS NAME IS IMPORTANT
    image: busybox
    command: [ "sh", "-c", "env && sleep 3600" ]
    envFrom:
    - configMapRef:
        name: app-config
```

![Create a YAML file called env-pod.yaml](/blog/images/dev_ops/k8s_configmap/Creation_env-pod%20.PNG)

Save this file, then apply it:

```
kubectl aply -f env-pod.yaml
```

✅ Check the environment inside the pod:

```
kubectl exec -it configmap-env-pod -- env | grep ENV
```

![Saving the file and applying the changes and checking the environment inside the pod](/blog/images/dev_ops/k8s_configmap/Save+Apply_Check_inside.PNG)


# Step 3: Use ConfigMap as Mounted Files

Let's simulate a config file like settings.properties

Create the file locally:

```
echo "PORT=8080" > settings.properties
echo "DEBUG=true" >> settings.properties
```

Create a ConfigMap from this file:

```
kubectl create configmap file-config --from-file=settings.properties
```

![Creating a file locally and then creating a ConfigMap from it](/blog/images/dev_ops/k8s_configmap/Config_file.PNG)


Now use it in a Pod with this file: volume-pod.yaml

```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-volume-pod
spec:
  containers:
  - name: app
    image: busybox
    command: [ "sh", "-c", "cat /config/settings.properties && sleep 3600" ]
    volumeMounts:
    - name: config-volume
      mountPath: /config
  volumes:
  - name: config-volume
    configMap:
      name: file-config
```

![Using the ConfigMap in a Pod with the file volume-pod.yaml](/blog/images/dev_ops/k8s_configmap/volume-pod_ConfigMap.png)


Apply it:

```
kubectl apply -f volume-pod.yaml
```

✅ Check logs:

```
kubectl logs configmap-volume-pod
```

You'll see the contents of settings.properties printed out.

![Applying the changes and checking the logs](/blog/images/dev_ops/k8s_configmap/Apply+CheckLogs_vvolume-pod.png)

# Step 4: Update a ConfigMap

Let's change the value of ENV from production to staging.

```
kubectl edit configmap app-config
```

This opens a text editor. Change:

```
ENV: production
```

![Changing the value of ENV from production](/blog/images/dev_ops/k8s_configmap/Update_ConfigMap_1.png)

to

```
ENV: staging
```

![From production to staging](/blog/images/dev_ops/k8s_configmap/Update_ConfigMap_2.png)

To save and exit simply press the Esc key and type out :wq and press Enter
- :w = write (save)
- q = quit

Important: Existing pods won't pick up this change automatically. You would need to restart the pod or redeploy it.

# Clean-Up

```
kubectl delete pod configmap-env-pod
kubectl delete pod configmap-volume-pod
kubectl delete configmap app-config
kubectl delete configmap file-config
```

And to stop the cluster (optional):

```
minikube stop
```

![Cleaning up the created files](/blog/images/dev_ops/k8s_configmap/CleanUp.png)
