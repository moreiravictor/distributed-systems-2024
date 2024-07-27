from protocols import meu_qoelho_mq_pb2_grpc
from protocols import meu_qoelho_mq_pb2
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = meu_qoelho_mq_pb2_grpc.MeuQoelhoMqStub(channel)

# feature = stub.createQueue(meu_qoelho_mq_pb2.Queue(name="test3", type=1))
# print(feature)

# feature = stub.publishMessage(meu_qoelho_mq_pb2.PublishMessageRequest(queueName="test", message=meu_qoelho_mq_pb2.MessageType(text_message="eaeeee")))
# print(feature)

# stub.removeQueue(meu_qoelho_mq_pb2.RemoveQueueRequest(name="test"))

res = stub.listQueues(meu_qoelho_mq_pb2.Empty())
print(res.queues)