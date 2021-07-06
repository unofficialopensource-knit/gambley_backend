#!/bin/bash

echo "Created test data directory"
mkdir test-data
cd test-data

echo "Copying test data to test data directory"
aws s3 cp s3://gambley-test-data/backend/email.json .
