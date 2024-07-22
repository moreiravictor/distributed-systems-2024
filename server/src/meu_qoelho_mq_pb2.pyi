from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIMPLE: _ClassVar[QueueType]
    MULTIPLE: _ClassVar[QueueType]
SIMPLE: QueueType
MULTIPLE: QueueType

class Queue(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: QueueType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[QueueType, str]] = ...) -> None: ...
