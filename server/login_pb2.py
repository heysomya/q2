# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: login.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'login.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blogin.proto\x12\x0e\x63om.grpc.first\"2\n\x0cLoginRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x10\n\x08passWord\x18\x02 \x01(\t\"<\n\x0b\x41piResponse\x12\x17\n\x0fresponseMessage\x18\x01 \x01(\t\x12\x14\n\x0cresponseCode\x18\x02 \x01(\x05\"\x07\n\x05\x45mpty2\x89\x01\n\x05Login\x12\x42\n\x05login\x12\x1c.com.grpc.first.LoginRequest\x1a\x1b.com.grpc.first.ApiResponse\x12<\n\x06logout\x12\x15.com.grpc.first.Empty\x1a\x1b.com.grpc.first.ApiResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'login_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOGINREQUEST']._serialized_start=31
  _globals['_LOGINREQUEST']._serialized_end=81
  _globals['_APIRESPONSE']._serialized_start=83
  _globals['_APIRESPONSE']._serialized_end=143
  _globals['_EMPTY']._serialized_start=145
  _globals['_EMPTY']._serialized_end=152
  _globals['_LOGIN']._serialized_start=155
  _globals['_LOGIN']._serialized_end=292
# @@protoc_insertion_point(module_scope)
