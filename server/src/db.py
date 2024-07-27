from typing import Dict
from models import Queue
from io import TextIOWrapper
import json

class DB:
  file_path = "src/db.json"

  def __init__(self):
    try:
      open(self.file_path, "r")
      print("connected to db successfully")
    except:
      print("failed to connect to db")

  def find_queues(self) -> Dict[str, Queue]:
    file = open(self.file_path, "r").read()
    content = dict(json.loads(file))
    return dict([(queue[0], Queue(**queue[1])) for queue in content.items()])


  def update_queues(self, queues: Dict[str, Queue]):
    file = open(self.file_path, "w")
    file.write(json.dumps(queues, default=vars))
