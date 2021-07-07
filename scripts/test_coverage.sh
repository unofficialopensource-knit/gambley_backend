#!/bin/bash


pytest -c config/pyproject.toml

curl https://deepsource.io/cli | sh

./bin/deepsource report --analyzer test-coverage --key python --value-file /app/coverage.xml
