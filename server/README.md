# Server

## How to install dependencies

To setup your virtual env firstly run:

```
virtualenv venv
source venv/bin/activate
```

and then run following to install dependencies:

```
cd ./server
pip install -r requirements.txt
```

## How to setup grpc

To generate protocol files run:

```
cd ./protos
./generate-python-protos.sh
```

And then to run server:

```
python3 ./src/server.py
```

To tryout test stub use:

```
python3 ./src/stub.py
```

