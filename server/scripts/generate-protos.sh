python3 -m grpc_tools.protoc -I. --python_out=./protocols --pyi_out=./protocols --grpc_python_out=./protocols ./meu-qoelho-mq.proto

for file_name in $(find protocols -name '*.py' -printf "%f "); do
        package=${file_name%.*}
        echo "Found package ${package}. Beginning replacement"
        find protocols/. -name '*.py' -exec sed -i -e "s/import ${package}/from protocols import ${package}/g" {} \;
done