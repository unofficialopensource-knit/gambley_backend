#!/bin/bash

apt-get update
apt-get install --assume-yes curl

curl https://deepsource.io/cli | sh

./bin/deepsource report --analyzer test-coverage --key python --value-file coverage.xml
