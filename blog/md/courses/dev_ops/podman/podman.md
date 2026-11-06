# Podman

## Intro

This is a basic introduction of `Podman`.
You should read more from the reference url of its official website in the bottom of this page.
If you are familiar with the Docker Container Engine the commands in Podman should be quite familiar. If you are brand new to containers, take a look at our Introduction.

### **What is Podman?**
Podman (short for **Pod Manager**) is an open-source, daemonless container engine developed by Red Hat as an alternative to Docker. It allows users to **create, run, and manage containers** in a manner similar to Docker but without requiring a long-running background daemon (`dockerd`).

### **Key Features of Podman**
1. **Daemonless Architecture**  
   - Unlike Docker, Podman does not rely on a central daemon (`dockerd`), making it more lightweight and secure.
   - Containers are run directly by the user (rootless mode is fully supported).

2. **Rootless Containers**  
   - Users can run containers without `sudo` privileges, improving security by reducing attack surfaces.

3. **Docker-Compatible CLI**  
   - Podman uses a command-line interface (CLI) similar to Docker (`podman run` instead of `docker run`), making it easy for Docker users to switch.

4. **Supports Pods (Like Kubernetes)**  
   - Inspired by Kubernetes, Podman can manage **pods** (groups of containers sharing resources like networking and storage).

5. **OCI-Compliant**  
   - Podman follows the **Open Container Initiative (OCI)** standards, meaning it can run Docker images (`docker.io`, `quay.io`) without modification.

6. **Systemd Integration**  
   - Containers can be managed as system services using `systemd`.

7. **No Need for Docker Daemon**  
   - Eliminates risks associated with a constantly running daemon (e.g., security vulnerabilities, crashes).

### **Podman vs. Docker**
| Feature          | Podman                     | Docker                     |
|------------------|----------------------------|----------------------------|
| **Daemon**       | No daemon (`daemonless`)   | Requires `dockerd`         |
| **Rootless**     | Fully supported            | Limited support            |
| **CLI**          | Docker-like commands       | Docker-native commands     |
| **Pods**         | Yes (Kubernetes-style)     | No (requires Docker Swarm) |
| **Systemd**      | Native integration         | Requires workarounds       |
| **Security**     | More secure (rootless)     | Depends on daemon          |

### **Basic Podman Commands**
```sh

# make sure you init a vm

  rm -rf ~/.local/share/containers/podman
  rm -rf ~/.config/containers/
  podman machine init

or you do the following,

# To cleanup
  podman machine rm
  podman machine init

# To start and stop

  podman machine stop
  podman machine start

# Manage pods
podman pod create --name mypod
podman pod start mypod
```

> See [Podman Installation](https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/podman/podman_installation.html) for a hands-on example of testing Podman with an `nginx` container.

### **Use Cases for Podman**
- **Developers** looking for a Docker alternative with better security.
- **Kubernetes users** who want local pod management.
- **System administrators** preferring rootless containers.
- **CI/CD pipelines** where daemonless operation is beneficial.

### **Conclusion**

Podman is a powerful, Docker-compatible container engine that improves security and flexibility by removing the need for a daemon. 
It’s particularly useful for rootless containers, Kubernetes-style pods, and environments where Docker’s architecture is considered a risk.


## Useful links

- https://docs.podman.io/en/latest/Commands.html


## Ref

https://docs.podman.io/en/latest/Tutorials.html