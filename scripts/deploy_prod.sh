#!/bin/bash

# sudo docker stack deploy --compose-file .docker/stack.yml --orchestrator swarm gambley
cd /tmp

aws s3 cp s3://gambley-app-data/configs/gambley.env .
aws s3 cp s3://gambley-app-data/stack/gambley-stack.yml .

ls -lha
