from typing import Dict
from protocols import meu_qoelho_mq_pb2_grpc
from protocols import meu_qoelho_mq_pb2
from models import Queue
from db import DB
import json

class MeuQoelhoMqServicer(meu_qoelho_mq_pb2_grpc.MeuQoelhoMqServicer):
  queuesMap: Dict[str, Queue] = {}
  db: DB

  def __init__(self):
    self.db = DB()
    self.queuesMap = self.db.find_queues()
    print("loaded queues from file")

  def createQueue(self, request, context):
    print("received request to create queue " + request.name)
    new_queue = meu_qoelho_mq_pb2.Queue(name = request.name, type = request.type)

    if (self.queuesMap.get(new_queue.name) ==  None):
      self.queuesMap[new_queue.name] = Queue(new_queue.name, new_queue.type, [])
      self.db.update_queues(self.queuesMap)

      print("created queue successfully")
      return new_queue

    print("queue already created")
    raise Exception("queue already created")

  def publishMessage(self, request, context):
    print("received request to publish a message to queue " + request.queueName)
    create_queue_request = meu_qoelho_mq_pb2.PublishMessageRequest(message = request.message, queueName = request.queueName)

    queue = self.queuesMap.get(create_queue_request.queueName)

    if (queue == None):
      print("tried to publish message to queue that does not exist")
      raise Exception("queue does not exist")

    queue.messages.append(create_queue_request.message.text_message or create_queue_request.message.bytes_message)

    self.db.update_queues(self.queuesMap)
    # TODO implement message publish to clients
    print("published message successfully")

    return meu_qoelho_mq_pb2.Empty()

  def removeQueue(self, request, context):
    print("received request to remove a queue")
    request = meu_qoelho_mq_pb2.RemoveQueueRequest(name=request.name)

    try:
      self.queuesMap.pop(request.name)
      self.db.update_queues(self.queuesMap)
    except:
      print("tried to delete queue that does not exist")
      raise Exception("queue does not exist")

    print("deleted queue successfully")
    return meu_qoelho_mq_pb2.Empty()

  def listQueues(self, request, context):
    print("received request to list queues")
    queues = [meu_qoelho_mq_pb2.Queue(name=queue.name, type=queue.type, pendingMessages=len(queue.messages))
              for queue in self.queuesMap.values()]

    return meu_qoelho_mq_pb2.ListQueueResponse(queues=queues)



