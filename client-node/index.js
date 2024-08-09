var PROTO_PATH = __dirname + '/../protos/meu-qoelho-mq.proto';

var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var stub = grpc.loadPackageDefinition(packageDefinition);
var minimist = require('minimist');

var client = new stub.MeuQoelhoMq('localhost:50051',
  grpc.credentials.createInsecure());

var types = ['SIMPLE', 'MULTIPLE'];

var args = minimist(process.argv.slice(2));
switch (args._[0]) {
  case 'create': 
    var name = args.name;
    var type = args.type;

    if (!name) {
      console.error('name param is required')
      return;
    }

    if (!type) {
      console.error('type param is required')
      return;
    }
    
    if (!types.includes(type)) {
      console.error('type must be ' + types.join('or '))
      return;
    }

    var queueData = {
      name,
      type,
    };

      
    client.createQueue(queueData, function(err, response) {
      if (err) {
        console.error('Error creating queue:', err);
        return;
      }

      console.log('Queue created successfully:', response);
    });
  case 'publish': 
    var name = args.name;
    var message = args.message;

    if (!name) {
      console.error('name param is required')
      return;
    }

    if (!message) {
      console.error('message param is required')
      return;
    }

    const messageData = {
      queueName: 'channel1',
      message: {
        text_message: message // or use `bytes_message` for sending bytes
      }
    };
      
    client.publishMessage(messageData, function(err, response) {
      if (err) {
        console.error('error publishing message:', err);
        return;
      }

      console.log('message published:', response);
    });
    
  default:
    console.error('Method does not exists');
    break;
}

