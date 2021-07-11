#!/bin/bash

hostname -i

while IFS='=' read -r -d '' SECRET VALUE;
do
    if [[ $SECRET == "GAMBLEY_*" ]];
    then
        SECRET_NAME=${SECRET/#GAMBLEY_}
        echo $SECRET_NAME
        echo "$VALUE" | sudo docker secret create "$SECRET_NAME"
    fi
done < <(env -0)

sed --in-place "s/BACKEND_IMAGE_TAG/$IMAGE_TAG/g" .docker/stack.yml

sudo docker stack deploy --compose-file .docker/stack.yml --orchestrator swarm
