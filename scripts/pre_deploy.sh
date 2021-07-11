#!/bin/bash

aws s3 cp s3://gambley-infra-data/private_keys/id_gambley .
chmod 400 id_gambley
sed --in-place "s/BACKEND_IMAGE_TAG/$IMAGE_TAG/g" .docker/stack.yml

echo "GAMBLEY_MAIL_USERNAME=$GAMBLEY_MAIL_USERNAME" >> .env
echo "GAMBLEY_MAIL_PASSWORD=$GAMBLEY_MAIL_PASSWORD" >> .env

scp -i id_gambley .env ubunut@3.109.12.202:/tmp/gambley.env
