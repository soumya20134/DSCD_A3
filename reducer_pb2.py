# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reducer.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rreducer.proto\"\x1c\n\x0emessageRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"5\n\rreduce_update\x12\x18\n\x10updated_centroid\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x32\x41\n\x0eReducerService\x12/\n\x0cSendCentroid\x12\x0f.messageRequest\x1a\x0e.reduce_updateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reducer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MESSAGEREQUEST']._serialized_start=17
  _globals['_MESSAGEREQUEST']._serialized_end=45
  _globals['_REDUCE_UPDATE']._serialized_start=47
  _globals['_REDUCE_UPDATE']._serialized_end=100
  _globals['_REDUCERSERVICE']._serialized_start=102
  _globals['_REDUCERSERVICE']._serialized_end=167
# @@protoc_insertion_point(module_scope)
