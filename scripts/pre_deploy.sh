#!/bin/bash

aws s3 cp s3://gambley-infra-data/private_keys/id_gambley .
chmod 400 id_gambley
sed --in-place "s/BACKEND_IMAGE_TAG/$IMAGE_TAG/g" .docker/stack.yml

cat .docker/stack.yml | grep -C 3 image
