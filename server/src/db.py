from typing import Dict, List
from models import Queue, Subscriber, QueueType
import json
import os
from dataclasses import asdict, is_dataclass
import enum


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        if isinstance(obj, enum.Enum):
            return obj.value
        return super().default(obj)

class DB:
  dirname = os.path.dirname(__file__)
  file_path = os.path.join(dirname, "./db.json")

  def __init__(self):
    try:
      open(self.file_path, "r")
      print("connected to db successfully")
    except:
      print("failed to connect to db")

  def __from_json_to_subscriber(self, data: dict) -> Subscriber:
    return Subscriber(ip=data['ip'], current_message=data['current_message'])

  def __from_json_to_queue(self, data: dict) -> Queue:
    subscribers: List[Subscriber] = [self.__from_json_to_subscriber(sub) for sub in data["subscribers"]]
    queue_type = QueueType(data["type"])
    return Queue(name=data["name"], type=queue_type, messages=data['messages'], subscribers=subscribers)

  def find_queues(self) -> Dict[str, Queue]:
    file = open(self.file_path, "r").read()
    data = dict(json.loads(file))
    return dict([(queue[0], self.__from_json_to_queue(queue[1])) for queue in data.items()])


  def update_queues(self, queues: Dict[str, Queue]):
    file = open(self.file_path, "w")
    file.write(json.dumps(queues, cls=CustomJSONEncoder))
