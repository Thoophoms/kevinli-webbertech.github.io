# Podman Installation

## **For Linux Distributions:**

* Ubuntu (20.10+) or Kaili.
```
sudo apt update
sudo apt install -y podman
```

* Arch Linux & Manjaro Linux. 

`sudo pacman -S podman`

* Alpine Linux. 

`sudo apk add podman`

* CentOS Stream (9+). 

`sudo dnf -y install podman`


## For macOS 

* Install Homebrew if not already installed and Install Podman. 
    
`brew install podman`

• Initialize and start the Podman machine (Podman on macOS relies on a Linux virtual machine): 

```
podman machine init
podman machine start
```

## For Windows: 

Podman on Windows utilizes the Windows Subsystem for Linux (WSL2). 

* Use your VM. (If you already had it.)
* Enable WSL2: Ensure WSL2 is enabled on your Windows system. 
* Install Podman Desktop: Download and run the installer from the official Podman Desktop website. This will set up Podman within a WSL2 environment. 
* Alternatively, you can install Podman using package managers like Chocolately, Scoop, or Winget if preferred. 

## Verification (after installation): 

You can verify the installation and check the Podman version using: [1]  

```
podman --version
podman info
podman pull nginx # this will download an image for you. If you see the download is going ok, then you are fine.
```

## Troubleshooting

### Kali Linux (VM Image)

The `unqualified-search-registries` setting in Podman defines a list of container registries that Podman will search when an image is referenced by a "short name" (i.e., without a fully qualified domain name and registry path). This setting is configured in the registries.conf file, which can be found at either 
`$HOME/.config/containers/registries.conf` (for user-specific configuration) or 

`/etc/containers/registries.conf` (for system-wide configuration).

If you try to pull a Kali image using a short name, such as podman pull kali, Podman will consult the unqualified-search-registries list in your registries.conf file. It will then search these registries in the order they are specified to find an image named "kali".

*Example configuration:*

To configure Podman to search `docker.io` and `quay.io` for unqualified image names, you would add or modify the unqualified-search-registries line in your registries.conf file as follows:

*Code*

Using `VIM`, press `ESC` on your keyboard and type `/` in the bottom commandline, and search for 'unqualified-search-registries', enabled that line, and add the following urls into it.

`unqualified-search-registries = ["docker.io", "quay.io"]`

### Ubuntu Linux (VM Image)

* gvproxy issue

If you run into the issues after you run the following commands,

```
podman machine init
podman machine start
```

Sometimes you will encounter issues starting a Podman machine, especially related to `gvproxy`, you might need to manually install or update `gvproxy `as detailed in some online resources.

*Solution:* Manually installing `gvproxy`.

You can install the latest version like this:

```
curl -s https://api.github.com/repos/containers/gvisor-tap-vsock/releases/latest | awk 'BEGIN { FS = "\"\\s*:\\s*" } /browser_download_url/ && /linux-amd64/ {print $2}' | xargs wget -O gvproxy-linux-amd64
chmod +x ./gvproxy-linux-amd64
mkdir -p /usr/local/lib/podman/
sudo mv gvproxy-linux-amd64 /usr/local/lib/podman/gvproxy
```

Then you should be able to init and start podman:

`sudo podman machine init --root=true`

or on newer versions:

`sudo podman machine init --rootful=true`

`sudo podman machine start`


### Ref

[1] https://www.youtube.com/watch?v=VdbjFgqPPE8
## Testing Podman with Nginx

Once Podman is installed, you can confirm everything works end-to-end by pulling and running a simple `nginx` container:

```
# Pull an image
podman pull nginx

# Run a container
podman run -d --name mynginx nginx

# List running containers
podman ps

# Stop a container
podman stop mynginx

# Remove a container
podman rm mynginx
```
