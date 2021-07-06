#!/bin/bash

mkdir test-data
cd test-data
aws s3 cp s3://gambley-test-data/backend/email.json .
