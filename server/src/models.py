from pydantic import BaseModel
from enum import Enum
from typing import List, Union
from dataclasses import dataclass
import random


class QueueType(Enum):
  SIMPLE = 1
  MULTIPLE = 2

Message = str | bytes

@dataclass
class Subscriber:
    ip: str
    current_message: Message | None

    def receive_message(self, message: Message):
      self.current_message = message

@dataclass
class Queue:
  name: str
  type: QueueType
  messages: List[Message]
  subscribers: List[Subscriber]

  def notify(self, message: Message):
    print("will notify")
    print(self.type == QueueType.MULTIPLE.value)
    if (self.type == QueueType.MULTIPLE.value):
      for sub in self.subscribers:
        print("notified" + sub.ip)
        sub.receive_message(message)
    elif (self.type == QueueType.SIMPLE.value):
      print("notified" + sub.ip)
      sub = random.choice(self.subscribers)
      sub.receive_message(message)

  def subscribe(self, subscriber_id: str):
    self.subscribers.append(subscriber_id)