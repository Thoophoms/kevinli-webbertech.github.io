# PyTorch Intro

## What is PyTorch and its history 

PyTorch is an open source machine learning library for Python and is completely based on Torch. It is primarily used for applications such as natural language processing. PyTorch is developed by Facebook's artificial-intelligence research group along with Uber's "Pyro" software for the concept of in-built probabilistic programming.

## Features

The major features of PyTorch are mentioned below −

Easy Interface − PyTorch offers easy to use API; hence it is considered to be very simple to operate and runs on Python. The code execution in this framework is quite easy.

Python usage − This library is considered to be Pythonic which smoothly integrates with the Python data science stack. Thus, it can leverage all the services and functionalities offered by the Python environment.

Computational graphs − PyTorch provides an excellent platform which offers dynamic computational graphs. Thus a user can change them during runtime. This is highly useful when a developer has no idea of how much memory is required for creating a neural network model.

PyTorch is known for having three levels of abstraction as given below −

`Tensor` − Imperative n-dimensional array which runs on GPU.

`Variable` − Node in computational graph. This stores data and gradient.

`Module` − Neural network layer which will store state or learnable weights.

## Installation

### Package Manager

To install the PyTorch binaries, you will need to use one of two supported package managers: Anaconda or pip. Anaconda is the recommended package manager as it will provide you all of the PyTorch dependencies in one, sandboxed install, including Python. My following tutorial across my site would be using ubuntu or debian Linux system.

**Install Conda**

```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

**Install PyTorch with Conda**

Please see detail at: [PyTorch Installation](https://pytorch.org/get-started/locally/)

**Install Python and PIP**

```bash
sudo apt install python
sudo apt install python3-pip
```

**Install PyTorch with CUDA**

https://developer.nvidia.com/cuda-zone

**Install PyTorch with rocm**

https://rocm.docs.amd.com/en/latest/
https://rocm.docs.amd.com/en/latest/what-is-rocm.html

### PyTorch Github

https://github.com/pytorch/pytorch#from-source
https://pytorch.org/tutorials/beginner/pytorch_with_examples.html
https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html