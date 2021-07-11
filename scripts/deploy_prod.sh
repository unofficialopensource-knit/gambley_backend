#!/bin/bash

# sudo docker stack deploy --compose-file .docker/stack.yml --orchestrator swarm gambley
cd /tmp

aws s3 cp s3://gambley-test-data/configs/gambley.env .
aws s3 cp s3://gambley-test-data/stack/gambley-stack.yml .

ls -lha
