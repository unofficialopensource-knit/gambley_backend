#!/bin/bash

cd /tmp

aws s3 cp s3://gambley-app-data/configs/gambley.env .
aws s3 cp s3://gambley-app-data/stack/gambley-stack.yml .

aws ecr get-login-password --region ap-south-1 | sudo docker login --username AWS --password-stdin 783729352349.dkr.ecr.ap-south-1.amazonaws.com
export TAG=`grep image gambley-stack.yml | cut -d':' -f3`

sudo docker image pull 783729352349.dkr.ecr.ap-south-1.amazonaws.com/gambley_backend:"$TAG"

sudo docker stack deploy --compose-file gambley-stack.yml --orchestrator swarm gambley
