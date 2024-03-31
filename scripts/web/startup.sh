#!/usr/bin/env bash

echo "Start service"

# migrate database
python scripts/migrate.py

python scripts/load_data.py fixture/main_db/main_db.robot_stop.json

# run app
exec uvicorn webapp.main:create_app --host=$BIND_IP --port=$BIND_PORT
