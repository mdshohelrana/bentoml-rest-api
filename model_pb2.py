# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\"\x07\n\x05\x45mpty\"Z\n\x08\x44\x61taHead\x12!\n\x04head\x18\x01 \x03(\x0b\x32\x13.DataHead.HeadEntry\x1a+\n\tHeadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x12PredictionResponse\x12\x0b\n\x03mse\x18\x01 \x01(\x01\x12\x13\n\x0bpredictions\x18\x02 \x03(\x01\x32Z\n\x0e\x46inancialModel\x12 \n\x0bGetDataHead\x12\x06.Empty\x1a\t.DataHead\x12&\n\x07Predict\x12\x06.Empty\x1a\x13.PredictionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DATAHEAD_HEADENTRY']._loaded_options = None
  _globals['_DATAHEAD_HEADENTRY']._serialized_options = b'8\001'
  _globals['_EMPTY']._serialized_start=15
  _globals['_EMPTY']._serialized_end=22
  _globals['_DATAHEAD']._serialized_start=24
  _globals['_DATAHEAD']._serialized_end=114
  _globals['_DATAHEAD_HEADENTRY']._serialized_start=71
  _globals['_DATAHEAD_HEADENTRY']._serialized_end=114
  _globals['_PREDICTIONRESPONSE']._serialized_start=116
  _globals['_PREDICTIONRESPONSE']._serialized_end=170
  _globals['_FINANCIALMODEL']._serialized_start=172
  _globals['_FINANCIALMODEL']._serialized_end=262
# @@protoc_insertion_point(module_scope)
