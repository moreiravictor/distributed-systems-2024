from db import DB
from models import Queue, QueueType
import random

class QueueService:
  db: DB

  def __init__(self, db: DB):
    self.db = db

  def start_queue(self, queue: Queue):
    while(True):
      if (len(queue.messages)):
        message = queue.messages.pop()
        queues_map = self.db.find_queues()
        queues_map[queue.name] = queue
        self.db.update_queues(queues_map)
        match queue.type:
          case QueueType.SIMPLE:
            sub = random.choice(queue.subscribers)
            print("queue " + queue.name + " notified " + sub.ip)
            sub.receive_message(message)
          case QueueType.MULTIPLE:
            for sub in queue.subscribers:
              print("queue " + queue.name + " notified " + sub.ip)
              sub.receive_message(message)