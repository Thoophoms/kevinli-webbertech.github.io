# Docker Lab4 - Python App Deployment with Docker

## Dockerfile, syntax and more

Docker is a simple tool and its syntax is very easy. However, if you following a tutorial of the following site will show you more examples you can try after the class,

https://docker-curriculum.com/#webapps-with-docker

In this class, we would learn to deploy a simple Python flask webserver app into a docker, so you get a feel of what
the container is and what a containerized image is.

Here is a practical example of writing a `Dockerfile` for a simple Python application, with a detailed explanation of each step.
The reason we choose `python` instead of `java` is to avoid complex installation of JDK in your operating system, especially for Mac.

### Example Project Structure

Imagine you have a simple Python web application using the Flask framework. Your project folder looks like this:

```
my-python-app/
├── app.py
├── requirements.txt
└── Dockerfile  <-- We will create this
```

**`app.py`** (Your application code):
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker World!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
*Note: `host='0.0.0.0'` is crucial. It makes the server available outside the container.*

**`requirements.txt`** (Your Python dependencies):
```
Flask==2.3.3
```

---

### The Dockerfile

Create a new file named **`Dockerfile`** (no file extension) in the same directory as `app.py`.

```Dockerfile
# Step 1: Choose the base image. This provides the foundation.
# We use an official Python runtime with a specific version and a slim OS (Debian).
FROM python:3.9-slim-buster

# Step 2: Set the working directory inside the container.
# All subsequent commands (COPY, RUN, CMD) will be run from this directory.
WORKDIR /app

# Step 3: Copy the requirements file first.
# We do this separately from the app code to leverage Docker's cache layer.
# If requirements.txt doesn't change, Docker won't reinstall dependencies on subsequent builds.
COPY requirements.txt requirements.txt

# Step 4: Install the Python dependencies defined in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code from the host to the container's working directory.
COPY . .

# Step 6: Inform Docker that the container listens on port 5000 at runtime.
# This is mostly documentation; the actual mapping is done at `docker run`.
EXPOSE 5000

# Step 7: Define the command to run the application when the container starts.
# This is the process that will keep the container alive.
# We use the "list" form (CMD ["executable", "param1", "param2"]) for best results.
CMD ["python", "app.py"]
```

---

### Building the Image and Running the Container

Now that you have your `Dockerfile`, follow these steps:

1.  **Open a terminal** and navigate to your `my-python-app` directory.

2.  **Build the Docker Image.** The `-t` flag tags your image with a name (`my-python-app`) and the `.` tells Docker to look for the `Dockerfile` in the current directory.
    ```bash
    docker build -t my-python-app .
    ```

3.  **Run the Container from your Image.** The `-p` flag maps your local machine's port 5000 to the container's internal port 5000 (which we exposed with `EXPOSE`). The `-d` flag runs the container in "detached" mode (in the background).
    ```bash
    docker run -d -p 5000:5000 --name my-running-app my-python-app
    ```

4.  **Test it!** Open your web browser and go to `http://localhost:5000`. You should see the message "Hello, Docker World!".

5.  **See your running container:**
    ```bash
    docker ps
    ```

6.  **Stop the container when you're done:**
    ```bash
    docker stop my-running-app
    ```

---

### Key Dockerfile Instructions Explained

| Instruction | Purpose | Example |
| :--- | :--- | :--- |
| **`FROM`** | **Mandatory first instruction.** Sets the base image to build upon. | `FROM python:3.9-slim-buster` |
| **`WORKDIR`** | Sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions that follow. | `WORKDIR /app` |
| **`COPY`** | Copies files or directories from the host machine (your computer) to the container's filesystem. | `COPY . .` |
| **`RUN`** | Executes a command in a new layer *on top of the current image* and commits the result. Used for installing packages. | `RUN pip install -r requirements.txt` |
| **`EXPOSE`** | Documents which port the container application listens on. This is informational. | `EXPOSE 5000` |
| **`CMD`** | Provides the default command to run when the container starts. There can only be one `CMD` in a Dockerfile. | `CMD ["python", "app.py"]` |

### Best Practices Demonstrated

1.  **Use a `.dockerignore` file:** Create a file called `.dockerignore` in the same directory to prevent copying unnecessary files (like local virtual environments, `__pycache__`, etc.), which makes your build faster and your image smaller.
    ```
    __pycache__
    *.pyc
    .env
    venv/
    Dockerfile
    .git
    .gitignore
    ```

2.  **Leverage Cache:** Copying `requirements.txt` and installing dependencies *before* copying the application code allows Docker to use its build cache. If your app code changes but your dependencies don't, it won't waste time re-running the `pip install` step.

3.  **Choose Small Base Images:** Using `python:3.9-slim-buster` instead of the default `python:3.9` results in a much smaller and more secure image, as it contains only the minimal packages needed to run Python.

This is the fundamental workflow for containerizing an application with Docker. You define your environment in a `Dockerfile`, build it into an image, and then run instances of that image as containers.

## The whole transcript

```commandline
kevinli@gpulx:/tmp/python_app$ ls
app.py  Dockerfile  requirements.txt
kevinli@gpulx:/tmp/python_app$ vi Dockerfile 
kevinli@gpulx:/tmp/python_app$ docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED        SIZE
nginx                              latest    5cdef4ac3335   11 days ago    161MB
mongodb/mongodb-community-server   latest    042afea05610   2 months ago   1.34GB
gcr.io/k8s-minikube/kicbase        v0.0.48   c6b5532e987b   5 months ago   1.31GB
hello-world                        latest    1b44b5a3e06a   6 months ago   10.1kB
kevinli@gpulx:/tmp/python_app$ docker build -t my-python-app .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon   5.12kB
Step 1/7 : FROM python:3.9-slim-buster
3.9-slim-buster: Pulling from library/python
8b91b88d5577: Pulling fs layer
824416e23423: Pulling fs layer
8d53da260408: Pulling fs layer
84c8c79126f6: Pulling fs layer
2e1c130fa3ec: Pulling fs layer
84c8c79126f6: Waiting
2e1c130fa3ec: Waiting
824416e23423: Download complete
8d53da260408: Verifying Checksum
8d53da260408: Download complete
84c8c79126f6: Verifying Checksum
84c8c79126f6: Download complete
2e1c130fa3ec: Verifying Checksum
2e1c130fa3ec: Download complete
8b91b88d5577: Verifying Checksum
8b91b88d5577: Download complete
8b91b88d5577: Pull complete
824416e23423: Pull complete
8d53da260408: Pull complete
84c8c79126f6: Pull complete
2e1c130fa3ec: Pull complete
Digest: sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d76dc5c0f01cac9b53990
Status: Downloaded newer image for python:3.9-slim-buster
 ---> c84dbfe3b8de
Step 2/7 : WORKDIR /app
 ---> Running in 28664a7123c4
 ---> Removed intermediate container 28664a7123c4
 ---> 536686c5ecfa
Step 3/7 : COPY requirements.txt requirements.txt
 ---> b3d95510a0c9
Step 4/7 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Running in fb1c5b40b398
Collecting Flask==2.3.3
  Downloading flask-2.3.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.1/96.1 kB 10.1 MB/s eta 0:00:00
Collecting blinker>=1.6.2
  Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting click>=8.1.3
  Downloading click-8.1.8-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.2/98.2 kB 10.3 MB/s eta 0:00:00
Collecting Werkzeug>=2.3.7
  Downloading werkzeug-3.1.5-py3-none-any.whl (225 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 225.0/225.0 kB 15.0 MB/s eta 0:00:00
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting Jinja2>=3.1.2
  Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 95.9 MB/s eta 0:00:00
Collecting importlib-metadata>=3.6.0
  Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
Collecting zipp>=3.20
  Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Collecting MarkupSafe>=2.0
  Downloading markupsafe-3.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (20 kB)
Installing collected packages: zipp, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, importlib-metadata, Flask
Successfully installed Flask-2.3.3 Jinja2-3.1.6 MarkupSafe-3.0.3 Werkzeug-3.1.5 blinker-1.9.0 click-8.1.8 importlib-metadata-8.7.1 itsdangerous-2.2.0 zipp-3.23.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
 ---> Removed intermediate container fb1c5b40b398
 ---> c562146a88c1
Step 5/7 : COPY . .
 ---> e9407ccfb359
Step 6/7 : EXPOSE 5000
 ---> Running in 67006595fdec
 ---> Removed intermediate container 67006595fdec
 ---> 6fa1e5fb3025
Step 7/7 : CMD ["python", "app.py"]
 ---> Running in d274a3a01469
 ---> Removed intermediate container d274a3a01469
 ---> 2c13aa205653
Successfully built 2c13aa205653
Successfully tagged my-python-app:latest
kevinli@gpulx:/tmp/python_app$ docker image ls
REPOSITORY                         TAG               IMAGE ID       CREATED          SIZE
my-python-app                      latest            2c13aa205653   32 seconds ago   127MB
nginx                              latest            5cdef4ac3335   11 days ago      161MB
mongodb/mongodb-community-server   latest            042afea05610   2 months ago     1.34GB
gcr.io/k8s-minikube/kicbase        v0.0.48           c6b5532e987b   5 months ago     1.31GB
hello-world                        latest            1b44b5a3e06a   6 months ago     10.1kB
python                             3.9-slim-buster   c84dbfe3b8de   2 years ago      116MB
```

The docker `Expose` port is controlling the right-side `5000`, in my case, I set it to map to my local `5002` port,

```
kevinli@gpulx:/tmp/python_app$ docker run -d -p 5002:5000 --name my-running-app my-python-app
81bdad9fbc27320e44f3568d0752922072d48d1dbc47ceeed5247b4408182f52
```

The next command is to confirm the container id,

```
kevinli@gpulx:/tmp/python_app$ docker container ls
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                         NAMES
81bdad9fbc27   my-python-app   "python app.py"          13 seconds ago   Up 11 seconds   0.0.0.0:5002->5000/tcp, [::]:5002->5000/tcp   my-running-app
11f9560a3cc8   nginx           "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp       my-webserver
```

Since the dockerfile copied everything into the `/app` dir in the container, so we would like to double-check it,
In order to get into the running container, we would use the `exec` directive to get in,

```
kevinli@gpulx:/tmp/python_app$ docker exec -it 81bdad9fbc27 /bin/bash
root@81bdad9fbc27:/app# ls
Dockerfile  app.py  requirements.txt
```

In the above section, we talk about the fact that in reality we would want to avoid copying the Dockerfile as well to reduce the
size of the image.