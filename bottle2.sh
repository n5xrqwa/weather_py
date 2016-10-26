#!/bin/bash

# Does not need to be ran by sudo.

# declare variables

. ./vars.sh

echo "Starting bottle webserver in background"
echo "Supports the weather program"
echo "PYTHON_PATH=$PYTHON_PATH"
echo "BOTTLE_PATH=$BOTTLE_PATH"
nohup  $PYTHON_PATH $BOTTLE_PATH &
