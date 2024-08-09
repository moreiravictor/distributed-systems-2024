#!/bin/bash
# Navigate to the directory containing the requirements.txt file
cd ./server

# Install the requirements
pip install -r requirements.txt

# Navigate to the directory containing the generate-python-protos.sh script
cd ../protos

# Make sure the script is executable
chmod +x generate-python-protos.sh

# Run the generate-python-protos.sh script
./generate-python-protos.sh

cd ../client-node

npm install

echo "All tasks completed successfully."
