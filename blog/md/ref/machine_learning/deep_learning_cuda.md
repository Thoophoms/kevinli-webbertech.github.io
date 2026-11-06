# CUDA

## CentOS notes

Red Hat Enterprise Linux (RHEL) 9 is the first major release built using CentOS Stream, an open source development platform for RHEL. CentOS Stream is where community members can collaborate with Red Hat developers to create, test, and contribute to future versions of RHEL. CentOS Stream 9 is the upstream for the next minor release of RHEL 9. 
CentOS Linux is a community-supported distribution of Linux that's derived from Red Hat's source code. CentOS Linux is similar to RHEL in terms of functionality, compatibility, and bug fixes, and historically each version of CentOS Linux reflected a major version of RHEL. However, Red Hat discontinued updates to CentOS Linux between 2021 and 2024, and its end-of-support date is June 30, 2024.

## Intro of CUDA

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/

## Installation of drivers, toolkits and cuDNN

* https://www.tensorflow.org/install/pip#software_requirements

**Nvidia driver**

`wget https://us.download.nvidia.com/tesla/550.90.07/nvidia-driver-local-repo-rhel9-550.90.07-1.0-1.x86_64.rpm`

* https://www.nvidia.com/en-us/drivers/details/226775/

**gcc**

`gcc --version`

**cuda toolkit(driver)**

`RUN wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda-repo-rhel9-12-3-local-12.3.2_545.23.08-1.x86_64.rpm && \
    rpm -i cuda-repo-rhel9-12-3-local-12.3.2_545.23.08-1.x86_64.rpm && dnf clean all && dnf -y install cuda-toolkit-12-3`

* https://developer.nvidia.com/cuda-toolkit-archive (12.3, this is the one I am using)

* https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=RHEL&target_version=9 (cuda 12.6)

**Troubleshooting**

```shell
yum -y install pciutils
lspci | grep -e VGA -ie NVIDIA
export CUDA_HOME=/usr/local/cuda-10.1
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
nano /home/UserName/.bash_profile
CUDA_HOME=/usr/local/cuda-10.1
LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
export CUDA_HOME
export LD_LIBRARY_PATH
```

* https://www.dell.com/support/kbdoc/en-us/000216077/how-to-install-nvidia-driver-in-rhel

* https://medium.com/analytics-vidhya/installing-cuda-on-red-hat-linux-and-ubuntu-dda69cd5ab9c

**cuDNN lib**

`RUN wget https://developer.download.nvidia.com/compute/cudnn/9.3.0/local_installers/cudnn-local-repo-rhel9-9.3.0-1.0-1.x86_64.rpm && \
    rpm -i cudnn-local-repo-rhel9-9.3.0-1.0-1.x86_64.rpm && dnf clean all && dnf -y install cudnn-cuda-12`

**OpenGL** (optional)

This is the dependencies stack based on the RHEL 9, and we will need to install from the bottom.

```shell
wget https://dl.rockylinux.org/pub/rocky/9/devel/x86_64/os/Packages/l/libglvnd-1.3.4-1.el9.x86_64.rpm (working)

wget https://rpmfind.net/linux/centos-stream/9-stream/AppStream/x86_64/os/Packages/libglvnd-opengl-1.3.4-1.el9.x86_64.rpm (working)

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-renderutil-0.3.9-20.el9.0.1.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/l/libxcb-1.13.1-9.el9.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/l/libXau-1.0.9-8.el9.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-wm-0.4.1-22.el9.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-image-0.4.0-19.el9.0.1.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-0.4.0-19.el9.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/BaseOS/x86_64/os/Packages/g/glibc-2.34-100.el9_4.2.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-keysyms-0.4.0-17.el9.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/l/libxkbcommon-x11-1.0.3-4.el9.x86_64.rpm

wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/l/libxkbcommon-1.0.3-4.el9.x86_64.rpm

wget https://bootstrap9.releng.rockylinux.org/build_results_s390x/xkeyboard-config/xkeyboard-config-2.33-2.el9/s390x/xkeyboard-config-2.33-2.el9.noarch.rpm

```

If you have anything missing, you will get something like the below, you need to figure out what your linux distribution is and grab all the libraries to install.

```shell
bash-5.1# dnf -y install cuda-toolkit-12-3
Last metadata expiration check: 0:19:44 ago on Sat Aug 10 04:08:34 2024.
Error: 
 Problem: package cuda-tools-12-3-12.3.2-1.x86_64 from cuda-rhel9-12-3-local requires cuda-visual-tools-12-3 >= 12.3.2, but none of the providers can be installed
  - package cuda-visual-tools-12-3-12.3.2-1.x86_64 from cuda-rhel9-12-3-local requires cuda-nsight-systems-12-3 >= 12.3.2, but none of the providers can be installed
  - package cuda-toolkit-12-3-12.3.2-1.x86_64 from cuda-rhel9-12-3-local requires cuda-tools-12-3 >= 12.3.2, but none of the providers can be installed
  - package cuda-nsight-systems-12-3-12.3.2-1.x86_64 from cuda-rhel9-12-3-local requires nsight-systems >= 2023.3.3.42, but none of the providers can be installed
  - conflicting requests
  - nothing provides libxcb-image.so.0()(64bit) needed by nsight-systems-2023.3.3-2023.3.3.42_233333266658v0-0.x86_64 from cuda-rhel9-12-3-local
  - nothing provides libxcb-keysyms.so.1()(64bit) needed by nsight-systems-2023.3.3-2023.3.3.42_233333266658v0-0.x86_64 from cuda-rhel9-12-3-local
  - nothing provides libxkbcommon-x11.so.0()(64bit) needed by nsight-systems-2023.3.3-2023.3.3.42_233333266658v0-0.x86_64 from cuda-rhel9-12-3-local
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```

**Test the Nvidia Installation**

* After the Nvidia drivers are installed, you can test the installation by running the command:

`nvcc -V`
Type `nvcc --version` and press Enter.

or

`cat /usr/local/cuda/version.txt`

`nvidia-smi`

ERROR: Unable to find the module utility `modprobe`; please make sure you have the package 'module-init-tools' or 'kmod' installed.  If you do have 'module-init-tools' or 'kmod' installed, then please check that `modprobe` is in your PATH.

## Troubleshooting

The good tensorflow docker image is: 

`docker pull tensorflow/tensorflow:latest-gpu`

`docker run -it tensorflow/tensorflow:latest-gpu`

The following urls are where you would find the docker file of the above images,

* https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/Dockerfile.rbe.gpu

* https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/Dockerfile.gpu

`Dockerfile.rbe.cuda12.3-cudnn9.1-ubuntu20.04-manylinux2014-multipython`

In the above images, we can check dll by doing this,

They are,

```shell
root@6a8e90e9439e:/usr/lib/x86_64-linux-gnu# ldconfig -p|grep libcuda*
	libcudnn_ops_train.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn_ops_train.so.8
	libcudnn_ops_infer.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8
	libcudnn_cnn_train.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8
	libcudnn_cnn_infer.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8
	libcudnn_adv_train.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn_adv_train.so.8
	libcudnn_adv_infer.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8
	libcudnn.so.8 (libc6,x86-64) => /lib/x86_64-linux-gnu/libcudnn.so.8
	libcudart.so.12 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcudart.so.12
	libcudart.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcudart.so
	libcuda.so.1 (libc6,x86-64) => /usr/local/cuda/lib64/stubs/libcuda.so.1
```

### Ref

* https://developer.nvidia.com/cuda-toolkit-archive

* https://developer.nvidia.com/cudnn

* https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=RHEL&target_version=9&target_type=rpm_local