#!/bin/bash


uvicorn \
    --factory \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 2 \
    --log-config config/log_config.json \
    --access-log \
    --loop uvloop \
    --http httptools \
    --ws none \
    src.app:create_app
