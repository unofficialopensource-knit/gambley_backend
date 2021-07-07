#!/bin/bash

cd /app

pytest -c config/pyproject.toml

apt-get update
apt-get install curl

curl https://deepsource.io/cli | sh

./bin/deepsource report --analyzer test-coverage --key python --value-file /app/coverage.xml
