#!/bin/bash

aws s3 cp s3://gambley-infra-data/private_keys/id_gambley .
chmod 400 id_gambley
sed --in-place "s/BACKEND_IMAGE_TAG/$IMAGE_TAG/g" .docker/stack.yml

echo "GAMBLEY_MAIL_USERNAME=$GAMBLEY_MAIL_USERNAME" >> gambley.env
echo "GAMBLEY_MAIL_PASSWORD=$GAMBLEY_MAIL_PASSWORD" >> gambley.env
echo "PORT=8000" >> gambley.env

aws s3 cp gambley.env s3://gambley-app-data/configs/gambley.env
aws s3 cp .docker/stack.yml s3://gambley-app-data/stack/gambley-stack.yml
