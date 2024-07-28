import grpc
from concurrent import futures
from protocols import meu_qoelho_mq_pb2_grpc
from servicer import MeuQoelhoMqServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meu_qoelho_mq_pb2_grpc.add_MeuQoelhoMqServicer_to_server(MeuQoelhoMqServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("running server")
    server.wait_for_termination()

serve()
