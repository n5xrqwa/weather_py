#!/bin/bash

# Does not need to be ran by sudo.

echo "Starting bottle webserver in background"
nohup  python3 $HOME/py/bottle2.py &
echo "Done"
