from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("userName", "passWord")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    userName: str
    passWord: str
    def __init__(self, userName: _Optional[str] = ..., passWord: _Optional[str] = ...) -> None: ...

class ApiResponse(_message.Message):
    __slots__ = ("responseMessage", "responseCode")
    RESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    responseMessage: str
    responseCode: int
    def __init__(self, responseMessage: _Optional[str] = ..., responseCode: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
