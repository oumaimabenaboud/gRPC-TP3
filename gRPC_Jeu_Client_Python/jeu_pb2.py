# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jeu.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tjeu.proto\"/\n\x0cGuessRequest\x12\r\n\x05guess\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\")\n\x06Result\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06winner\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2e\n\x03Jeu\x12\x1c\n\x05Start\x12\x06.Empty\x1a\x07.Result\"\x00\x30\x01\x12%\n\x05Guess\x12\r.GuessRequest\x1a\x07.Result\"\x00(\x01\x30\x01\x12\x19\n\x04Stop\x12\x06.Empty\x1a\x07.Result\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'jeu_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GUESSREQUEST._serialized_start=13
  _GUESSREQUEST._serialized_end=60
  _RESULT._serialized_start=62
  _RESULT._serialized_end=103
  _EMPTY._serialized_start=105
  _EMPTY._serialized_end=112
  _JEU._serialized_start=114
  _JEU._serialized_end=215
# @@protoc_insertion_point(module_scope)
