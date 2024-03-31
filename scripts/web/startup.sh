#!/usr/bin/env bash

echo "Start service"

# migrate database
python scripts/migrate.py

# run app
exec uvicorn webapp.main:create_app --host=$BIND_IP --port=$BIND_PORT
