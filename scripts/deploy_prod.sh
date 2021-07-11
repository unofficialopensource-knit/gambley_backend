#!/bin/bash

# while IFS='=' read -r -d '' SECRET VALUE;
# do
#     if [[ $SECRET == "GAMBLEY_*" ]];
#     then
#         SECRET_NAME=${SECRET/#GAMBLEY_}
#         echo $SECRET_NAME
#         echo "$VALUE" | sudo docker secret create "$SECRET_NAME"
#     fi
# done < <(env -0)

# create_secret 

# sudo docker stack deploy --compose-file .docker/stack.yml --orchestrator swarm gambley

echo $GAMBLEY_MAIL_USERNAME, 123
