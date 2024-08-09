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

function main() {
  var client = new stub.MeuQoelhoMq('localhost:50051',
                                       grpc.credentials.createInsecure());
  var queueData = {
    name: 'my-queue', // Set your desired queue name
    type: 'SIMPLE' // Set the appropriate queue type (SIMPLE or MULTIPLE)
  };
  
  client.createQueue(queueData, function(err, response) {
    if (err) {
      console.error('Error creating queue:', err);
    } else {
      console.log('Queue created successfully:', response);
    }
  });
}

main();
