# Deep Learning VM setup

## Takeaway

* In this article we will talk about how to set up a docker image for tensorflow deep learning.

* This docker image would be used in EKS or K8s env.

* We will provide details for the Jenkins job config as well.

![alt text](./tensorflow_dependencies.png.png)

* wget https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda-repo-rhel9-12-6-local-12.6.0_560.28.03-1.x86_64.rpm
* sudo rpm -i cuda-repo-rhel9-12-6-local-12.6.0_560.28.03-1.x86_64.rpm
* sudo dnf clean all
* sudo dnf -y install cuda-toolkit-12-6