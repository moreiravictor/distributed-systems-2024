from typing import List
from protocols import meu_qoelho_mq_pb2_grpc
from protocols import meu_qoelho_mq_pb2

class MeuQoelhoMqServicer(meu_qoelho_mq_pb2_grpc.MeuQoelhoMqServicer):
  queues: List[meu_qoelho_mq_pb2.Queue] = []

  def createQueue(self, request, context):
    print("received request to create queue")

    if ([q for q in self.queues if q.name == request.name ] == []):
      new_queue = meu_qoelho_mq_pb2.Queue(name = request.name, type = request.type)
      self.queues.append(new_queue)

      print("created queue successfully")
      return new_queue

    print("failed to create queue")
    raise Exception("queue already created")

