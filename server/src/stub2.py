from protocols import meu_qoelho_mq_pb2_grpc
from protocols import meu_qoelho_mq_pb2
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = meu_qoelho_mq_pb2_grpc.MeuQoelhoMqStub(channel)

feature = stub.publishMessage(meu_qoelho_mq_pb2.PublishMessageRequest(queueName="test0", message=meu_qoelho_mq_pb2.MessageType(text_message="EITA")))
print(feature)
