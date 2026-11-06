#!/bin/bash

scp -i "kltutor.com.pem" ./*.py ./run.sh ubuntu@ec2-18-221-239-84.us-east-2.compute.amazonaws.com:/home/ubuntu/encryption

echo "files deployment is done"

echo "logging to EC2 via ssh"

ssh -i "kltutor.com.pem" ubuntu@ec2-18-221-239-84.us-east-2.compute.amazonaws.com

# copy and run the following, it might not chain properly
nohup python3 course_authentication.py > output.log &
