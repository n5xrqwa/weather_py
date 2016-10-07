#!/bin/bash

# Does not need to be ran by sudo.

# declare variables

PYTHON_PATH=python3
BOTTLE_PATH=$HOME/weather_py/bottle2.py

echo "Starting bottle webserver in background"
nohup  $PYTHON_PATH $BOTTLE_PATH &
echo "Done"
