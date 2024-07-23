from protocols import meu_qoelho_mq_pb2_grpc
from protocols import meu_qoelho_mq_pb2
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = meu_qoelho_mq_pb2_grpc.MeuQoelhoMqStub(channel)

feature = stub.createQueue(meu_qoelho_mq_pb2.Queue(name="test", type=1))
print(feature)