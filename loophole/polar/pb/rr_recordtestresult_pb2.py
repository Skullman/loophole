# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rr_recordtestresult.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rr_recordtestresult.proto',
  package='data',
  serialized_pb=_b('\n\x19rr_recordtestresult.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"\x93\x01\n\x17PbRRRecordingTestResult\x12$\n\nstart_time\x18\x01 \x02(\x0b\x32\x10.PbLocalDateTime\x12\"\n\x08\x65nd_time\x18\x02 \x02(\x0b\x32\x10.PbLocalDateTime\x12\x0e\n\x06hr_avg\x18\x03 \x02(\r\x12\x0e\n\x06hr_min\x18\x04 \x02(\r\x12\x0e\n\x06hr_max\x18\x05 \x02(\r')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBRRRECORDINGTESTRESULT = _descriptor.Descriptor(
  name='PbRRRecordingTestResult',
  full_name='data.PbRRRecordingTestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='data.PbRRRecordingTestResult.start_time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='data.PbRRRecordingTestResult.end_time', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hr_avg', full_name='data.PbRRRecordingTestResult.hr_avg', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hr_min', full_name='data.PbRRRecordingTestResult.hr_min', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hr_max', full_name='data.PbRRRecordingTestResult.hr_max', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=196,
)

_PBRRRECORDINGTESTRESULT.fields_by_name['start_time'].message_type = types_pb2._PBLOCALDATETIME
_PBRRRECORDINGTESTRESULT.fields_by_name['end_time'].message_type = types_pb2._PBLOCALDATETIME
DESCRIPTOR.message_types_by_name['PbRRRecordingTestResult'] = _PBRRRECORDINGTESTRESULT

PbRRRecordingTestResult = _reflection.GeneratedProtocolMessageType('PbRRRecordingTestResult', (_message.Message,), dict(
  DESCRIPTOR = _PBRRRECORDINGTESTRESULT,
  __module__ = 'rr_recordtestresult_pb2'
  # @@protoc_insertion_point(class_scope:data.PbRRRecordingTestResult)
  ))
_sym_db.RegisterMessage(PbRRRecordingTestResult)


# @@protoc_insertion_point(module_scope)
