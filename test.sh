#!/bin/bash

# Navigate to the directory containing the requirements.txt file

python3 ./server/src/server.py &

sleep 10

python3 ./server/src/stub2.py &

sleep 5

echo "All tasks completed successfully."
