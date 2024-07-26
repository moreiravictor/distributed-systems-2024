#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
result_path="$parent_path/../server/src/protocols"

python3 -m grpc_tools.protoc -I. --python_out="$result_path" --pyi_out="$result_path" --grpc_python_out="$result_path" ./meu-qoelho-mq.proto

find "$result_path" -name '*.py' | while read -r file_path; do
        file_name=$(basename "$file_path")
        package=${file_name%.*}
        echo "Found package ${package}. Beginning replacement"
        # Detect the operating system
        if [[ "$OSTYPE" == "darwin"* ]]; then
                # macOS
                find "$result_path" -name '*.py' -exec sed -i '' -e "s/import ${package}/from protocols import ${package}/g" {} \;
        else
                # Assuming Linux (Ubuntu)
                find "$result_path" -name '*.py' -exec sed -i -e "s/import ${package}/from protocols import ${package}/g" {} \;
        fi
done