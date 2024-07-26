from pydantic import BaseModel
from enum import Enum
from typing import List, Union
from dataclasses import dataclass


class QueueType(Enum):
  SIMPLE = 1
  MULTIPLE = 2

@dataclass
class Queue:
  name: str
  type: QueueType
  messages: List[Union[str, bytes]]