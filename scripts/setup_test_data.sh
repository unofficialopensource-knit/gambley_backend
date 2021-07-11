#!/bin/bash

echo "Created test data directory"
mkdir -p test/data
cd test/data

echo "Copying test data to test data directory"
aws s3 cp s3://gambley-app-data/test/backend/email.json .
