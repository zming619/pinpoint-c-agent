# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import ThreadDump_pb2 as ThreadDump__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Cmd.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n!com.navercorp.pinpoint.grpc.traceB\010CmdProtoP\001'),
  serialized_pb=_b('\n\tCmd.proto\x12\x02v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x10ThreadDump.proto\"w\n\x0bPCmdMessage\x12\x34\n\x10handshakeMessage\x18\x01 \x01(\x0b\x32\x18.v1.PCmdServiceHandshakeH\x00\x12\'\n\x0b\x66\x61ilMessage\x18\x02 \x01(\x0b\x32\x10.v1.PCmdResponseH\x00\x42\t\n\x07message\"8\n\x14PCmdServiceHandshake\x12 \n\x18supportCommandServiceKey\x18\x01 \x03(\x05\"a\n\x0cPCmdResponse\x12\x12\n\nresponseId\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12-\n\x07message\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"k\n\x12PCmdStreamResponse\x12\x12\n\nresponseId\x18\x01 \x01(\x05\x12\x12\n\nsequenceId\x18\x02 \x01(\x05\x12-\n\x07message\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x97\x02\n\x0bPCmdRequest\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12$\n\x0b\x63ommandEcho\x18\xc6\x05 \x01(\x0b\x32\x0c.v1.PCmdEchoH\x00\x12>\n\x18\x63ommandActiveThreadCount\x18\xda\x05 \x01(\x0b\x32\x19.v1.PCmdActiveThreadCountH\x00\x12<\n\x17\x63ommandActiveThreadDump\x18\xe4\x05 \x01(\x0b\x32\x18.v1.PCmdActiveThreadDumpH\x00\x12\x46\n\x1c\x63ommandActiveThreadLightDump\x18\xee\x05 \x01(\x0b\x32\x1d.v1.PCmdActiveThreadLightDumpH\x00\x42\t\n\x07\x63ommand\"\x1b\n\x08PCmdEcho\x12\x0f\n\x07message\x18\x01 \x01(\t\"M\n\x10PCmdEchoResponse\x12(\n\x0e\x63ommonResponse\x18\x01 \x01(\x0b\x32\x10.v1.PCmdResponse\x12\x0f\n\x07message\x18\x02 \x01(\t\"O\n\x14PCmdActiveThreadDump\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x12\n\nthreadName\x18\x02 \x03(\t\x12\x14\n\x0clocalTraceId\x18\x03 \x03(\x03\"\x9e\x01\n\x17PCmdActiveThreadDumpRes\x12(\n\x0e\x63ommonResponse\x18\x01 \x01(\x0b\x32\x10.v1.PCmdResponse\x12)\n\nthreadDump\x18\x02 \x03(\x0b\x32\x15.v1.PActiveThreadDump\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07subType\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"T\n\x19PCmdActiveThreadLightDump\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x12\n\nthreadName\x18\x02 \x03(\t\x12\x14\n\x0clocalTraceId\x18\x03 \x03(\x03\"\xa8\x01\n\x1cPCmdActiveThreadLightDumpRes\x12(\n\x0e\x63ommonResponse\x18\x01 \x01(\x0b\x32\x10.v1.PCmdResponse\x12.\n\nthreadDump\x18\x02 \x03(\x0b\x32\x1a.v1.PActiveThreadLightDump\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07subType\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"\x17\n\x15PCmdActiveThreadCount\"\x9b\x01\n\x18PCmdActiveThreadCountRes\x12\x34\n\x14\x63ommonStreamResponse\x18\x01 \x01(\x0b\x32\x16.v1.PCmdStreamResponse\x12\x1b\n\x13histogramSchemaType\x18\x02 \x01(\x05\x12\x19\n\x11\x61\x63tiveThreadCount\x18\x03 \x03(\x05\x12\x11\n\ttimeStamp\x18\x04 \x01(\x03*\x89\x01\n\x0cPCommandType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PING\x10\x64\x12\x08\n\x04PONG\x10\x65\x12\t\n\x04\x45\x43HO\x10\xc6\x05\x12\x18\n\x13\x41\x43TIVE_THREAD_COUNT\x10\xda\x05\x12\x17\n\x12\x41\x43TIVE_THREAD_DUMP\x10\xe4\x05\x12\x1d\n\x18\x41\x43TIVE_THREAD_LIGHT_DUMP\x10\xee\x05\x42/\n!com.navercorp.pinpoint.grpc.traceB\x08\x43mdProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,ThreadDump__pb2.DESCRIPTOR,])

_PCOMMANDTYPE = _descriptor.EnumDescriptor(
  name='PCommandType',
  full_name='v1.PCommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING', index=1, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PONG', index=2, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECHO', index=3, number=710,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE_THREAD_COUNT', index=4, number=730,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE_THREAD_DUMP', index=5, number=740,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE_THREAD_LIGHT_DUMP', index=6, number=750,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1527,
  serialized_end=1664,
)
_sym_db.RegisterEnumDescriptor(_PCOMMANDTYPE)

PCommandType = enum_type_wrapper.EnumTypeWrapper(_PCOMMANDTYPE)
NONE = 0
PING = 100
PONG = 101
ECHO = 710
ACTIVE_THREAD_COUNT = 730
ACTIVE_THREAD_DUMP = 740
ACTIVE_THREAD_LIGHT_DUMP = 750



_PCMDMESSAGE = _descriptor.Descriptor(
  name='PCmdMessage',
  full_name='v1.PCmdMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='handshakeMessage', full_name='v1.PCmdMessage.handshakeMessage', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failMessage', full_name='v1.PCmdMessage.failMessage', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='v1.PCmdMessage.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=67,
  serialized_end=186,
)


_PCMDSERVICEHANDSHAKE = _descriptor.Descriptor(
  name='PCmdServiceHandshake',
  full_name='v1.PCmdServiceHandshake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='supportCommandServiceKey', full_name='v1.PCmdServiceHandshake.supportCommandServiceKey', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=244,
)


_PCMDRESPONSE = _descriptor.Descriptor(
  name='PCmdResponse',
  full_name='v1.PCmdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseId', full_name='v1.PCmdResponse.responseId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v1.PCmdResponse.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='v1.PCmdResponse.message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=343,
)


_PCMDSTREAMRESPONSE = _descriptor.Descriptor(
  name='PCmdStreamResponse',
  full_name='v1.PCmdStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseId', full_name='v1.PCmdStreamResponse.responseId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequenceId', full_name='v1.PCmdStreamResponse.sequenceId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='v1.PCmdStreamResponse.message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=452,
)


_PCMDREQUEST = _descriptor.Descriptor(
  name='PCmdRequest',
  full_name='v1.PCmdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='v1.PCmdRequest.requestId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandEcho', full_name='v1.PCmdRequest.commandEcho', index=1,
      number=710, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandActiveThreadCount', full_name='v1.PCmdRequest.commandActiveThreadCount', index=2,
      number=730, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandActiveThreadDump', full_name='v1.PCmdRequest.commandActiveThreadDump', index=3,
      number=740, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandActiveThreadLightDump', full_name='v1.PCmdRequest.commandActiveThreadLightDump', index=4,
      number=750, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='command', full_name='v1.PCmdRequest.command',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=455,
  serialized_end=734,
)


_PCMDECHO = _descriptor.Descriptor(
  name='PCmdEcho',
  full_name='v1.PCmdEcho',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='v1.PCmdEcho.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=736,
  serialized_end=763,
)


_PCMDECHORESPONSE = _descriptor.Descriptor(
  name='PCmdEchoResponse',
  full_name='v1.PCmdEchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commonResponse', full_name='v1.PCmdEchoResponse.commonResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='v1.PCmdEchoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=842,
)


_PCMDACTIVETHREADDUMP = _descriptor.Descriptor(
  name='PCmdActiveThreadDump',
  full_name='v1.PCmdActiveThreadDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='v1.PCmdActiveThreadDump.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threadName', full_name='v1.PCmdActiveThreadDump.threadName', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localTraceId', full_name='v1.PCmdActiveThreadDump.localTraceId', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=923,
)


_PCMDACTIVETHREADDUMPRES = _descriptor.Descriptor(
  name='PCmdActiveThreadDumpRes',
  full_name='v1.PCmdActiveThreadDumpRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commonResponse', full_name='v1.PCmdActiveThreadDumpRes.commonResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threadDump', full_name='v1.PCmdActiveThreadDumpRes.threadDump', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='v1.PCmdActiveThreadDumpRes.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subType', full_name='v1.PCmdActiveThreadDumpRes.subType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='v1.PCmdActiveThreadDumpRes.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=926,
  serialized_end=1084,
)


_PCMDACTIVETHREADLIGHTDUMP = _descriptor.Descriptor(
  name='PCmdActiveThreadLightDump',
  full_name='v1.PCmdActiveThreadLightDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='v1.PCmdActiveThreadLightDump.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threadName', full_name='v1.PCmdActiveThreadLightDump.threadName', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localTraceId', full_name='v1.PCmdActiveThreadLightDump.localTraceId', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1086,
  serialized_end=1170,
)


_PCMDACTIVETHREADLIGHTDUMPRES = _descriptor.Descriptor(
  name='PCmdActiveThreadLightDumpRes',
  full_name='v1.PCmdActiveThreadLightDumpRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commonResponse', full_name='v1.PCmdActiveThreadLightDumpRes.commonResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threadDump', full_name='v1.PCmdActiveThreadLightDumpRes.threadDump', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='v1.PCmdActiveThreadLightDumpRes.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subType', full_name='v1.PCmdActiveThreadLightDumpRes.subType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='v1.PCmdActiveThreadLightDumpRes.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1173,
  serialized_end=1341,
)


_PCMDACTIVETHREADCOUNT = _descriptor.Descriptor(
  name='PCmdActiveThreadCount',
  full_name='v1.PCmdActiveThreadCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1343,
  serialized_end=1366,
)


_PCMDACTIVETHREADCOUNTRES = _descriptor.Descriptor(
  name='PCmdActiveThreadCountRes',
  full_name='v1.PCmdActiveThreadCountRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commonStreamResponse', full_name='v1.PCmdActiveThreadCountRes.commonStreamResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='histogramSchemaType', full_name='v1.PCmdActiveThreadCountRes.histogramSchemaType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activeThreadCount', full_name='v1.PCmdActiveThreadCountRes.activeThreadCount', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='v1.PCmdActiveThreadCountRes.timeStamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1369,
  serialized_end=1524,
)

_PCMDMESSAGE.fields_by_name['handshakeMessage'].message_type = _PCMDSERVICEHANDSHAKE
_PCMDMESSAGE.fields_by_name['failMessage'].message_type = _PCMDRESPONSE
_PCMDMESSAGE.oneofs_by_name['message'].fields.append(
  _PCMDMESSAGE.fields_by_name['handshakeMessage'])
_PCMDMESSAGE.fields_by_name['handshakeMessage'].containing_oneof = _PCMDMESSAGE.oneofs_by_name['message']
_PCMDMESSAGE.oneofs_by_name['message'].fields.append(
  _PCMDMESSAGE.fields_by_name['failMessage'])
_PCMDMESSAGE.fields_by_name['failMessage'].containing_oneof = _PCMDMESSAGE.oneofs_by_name['message']
_PCMDRESPONSE.fields_by_name['message'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PCMDSTREAMRESPONSE.fields_by_name['message'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PCMDREQUEST.fields_by_name['commandEcho'].message_type = _PCMDECHO
_PCMDREQUEST.fields_by_name['commandActiveThreadCount'].message_type = _PCMDACTIVETHREADCOUNT
_PCMDREQUEST.fields_by_name['commandActiveThreadDump'].message_type = _PCMDACTIVETHREADDUMP
_PCMDREQUEST.fields_by_name['commandActiveThreadLightDump'].message_type = _PCMDACTIVETHREADLIGHTDUMP
_PCMDREQUEST.oneofs_by_name['command'].fields.append(
  _PCMDREQUEST.fields_by_name['commandEcho'])
_PCMDREQUEST.fields_by_name['commandEcho'].containing_oneof = _PCMDREQUEST.oneofs_by_name['command']
_PCMDREQUEST.oneofs_by_name['command'].fields.append(
  _PCMDREQUEST.fields_by_name['commandActiveThreadCount'])
_PCMDREQUEST.fields_by_name['commandActiveThreadCount'].containing_oneof = _PCMDREQUEST.oneofs_by_name['command']
_PCMDREQUEST.oneofs_by_name['command'].fields.append(
  _PCMDREQUEST.fields_by_name['commandActiveThreadDump'])
_PCMDREQUEST.fields_by_name['commandActiveThreadDump'].containing_oneof = _PCMDREQUEST.oneofs_by_name['command']
_PCMDREQUEST.oneofs_by_name['command'].fields.append(
  _PCMDREQUEST.fields_by_name['commandActiveThreadLightDump'])
_PCMDREQUEST.fields_by_name['commandActiveThreadLightDump'].containing_oneof = _PCMDREQUEST.oneofs_by_name['command']
_PCMDECHORESPONSE.fields_by_name['commonResponse'].message_type = _PCMDRESPONSE
_PCMDACTIVETHREADDUMPRES.fields_by_name['commonResponse'].message_type = _PCMDRESPONSE
_PCMDACTIVETHREADDUMPRES.fields_by_name['threadDump'].message_type = ThreadDump__pb2._PACTIVETHREADDUMP
_PCMDACTIVETHREADLIGHTDUMPRES.fields_by_name['commonResponse'].message_type = _PCMDRESPONSE
_PCMDACTIVETHREADLIGHTDUMPRES.fields_by_name['threadDump'].message_type = ThreadDump__pb2._PACTIVETHREADLIGHTDUMP
_PCMDACTIVETHREADCOUNTRES.fields_by_name['commonStreamResponse'].message_type = _PCMDSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['PCmdMessage'] = _PCMDMESSAGE
DESCRIPTOR.message_types_by_name['PCmdServiceHandshake'] = _PCMDSERVICEHANDSHAKE
DESCRIPTOR.message_types_by_name['PCmdResponse'] = _PCMDRESPONSE
DESCRIPTOR.message_types_by_name['PCmdStreamResponse'] = _PCMDSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['PCmdRequest'] = _PCMDREQUEST
DESCRIPTOR.message_types_by_name['PCmdEcho'] = _PCMDECHO
DESCRIPTOR.message_types_by_name['PCmdEchoResponse'] = _PCMDECHORESPONSE
DESCRIPTOR.message_types_by_name['PCmdActiveThreadDump'] = _PCMDACTIVETHREADDUMP
DESCRIPTOR.message_types_by_name['PCmdActiveThreadDumpRes'] = _PCMDACTIVETHREADDUMPRES
DESCRIPTOR.message_types_by_name['PCmdActiveThreadLightDump'] = _PCMDACTIVETHREADLIGHTDUMP
DESCRIPTOR.message_types_by_name['PCmdActiveThreadLightDumpRes'] = _PCMDACTIVETHREADLIGHTDUMPRES
DESCRIPTOR.message_types_by_name['PCmdActiveThreadCount'] = _PCMDACTIVETHREADCOUNT
DESCRIPTOR.message_types_by_name['PCmdActiveThreadCountRes'] = _PCMDACTIVETHREADCOUNTRES
DESCRIPTOR.enum_types_by_name['PCommandType'] = _PCOMMANDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PCmdMessage = _reflection.GeneratedProtocolMessageType('PCmdMessage', (_message.Message,), {
  'DESCRIPTOR' : _PCMDMESSAGE,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdMessage)
  })
_sym_db.RegisterMessage(PCmdMessage)

PCmdServiceHandshake = _reflection.GeneratedProtocolMessageType('PCmdServiceHandshake', (_message.Message,), {
  'DESCRIPTOR' : _PCMDSERVICEHANDSHAKE,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdServiceHandshake)
  })
_sym_db.RegisterMessage(PCmdServiceHandshake)

PCmdResponse = _reflection.GeneratedProtocolMessageType('PCmdResponse', (_message.Message,), {
  'DESCRIPTOR' : _PCMDRESPONSE,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdResponse)
  })
_sym_db.RegisterMessage(PCmdResponse)

PCmdStreamResponse = _reflection.GeneratedProtocolMessageType('PCmdStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _PCMDSTREAMRESPONSE,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdStreamResponse)
  })
_sym_db.RegisterMessage(PCmdStreamResponse)

PCmdRequest = _reflection.GeneratedProtocolMessageType('PCmdRequest', (_message.Message,), {
  'DESCRIPTOR' : _PCMDREQUEST,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdRequest)
  })
_sym_db.RegisterMessage(PCmdRequest)

PCmdEcho = _reflection.GeneratedProtocolMessageType('PCmdEcho', (_message.Message,), {
  'DESCRIPTOR' : _PCMDECHO,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdEcho)
  })
_sym_db.RegisterMessage(PCmdEcho)

PCmdEchoResponse = _reflection.GeneratedProtocolMessageType('PCmdEchoResponse', (_message.Message,), {
  'DESCRIPTOR' : _PCMDECHORESPONSE,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdEchoResponse)
  })
_sym_db.RegisterMessage(PCmdEchoResponse)

PCmdActiveThreadDump = _reflection.GeneratedProtocolMessageType('PCmdActiveThreadDump', (_message.Message,), {
  'DESCRIPTOR' : _PCMDACTIVETHREADDUMP,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdActiveThreadDump)
  })
_sym_db.RegisterMessage(PCmdActiveThreadDump)

PCmdActiveThreadDumpRes = _reflection.GeneratedProtocolMessageType('PCmdActiveThreadDumpRes', (_message.Message,), {
  'DESCRIPTOR' : _PCMDACTIVETHREADDUMPRES,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdActiveThreadDumpRes)
  })
_sym_db.RegisterMessage(PCmdActiveThreadDumpRes)

PCmdActiveThreadLightDump = _reflection.GeneratedProtocolMessageType('PCmdActiveThreadLightDump', (_message.Message,), {
  'DESCRIPTOR' : _PCMDACTIVETHREADLIGHTDUMP,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdActiveThreadLightDump)
  })
_sym_db.RegisterMessage(PCmdActiveThreadLightDump)

PCmdActiveThreadLightDumpRes = _reflection.GeneratedProtocolMessageType('PCmdActiveThreadLightDumpRes', (_message.Message,), {
  'DESCRIPTOR' : _PCMDACTIVETHREADLIGHTDUMPRES,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdActiveThreadLightDumpRes)
  })
_sym_db.RegisterMessage(PCmdActiveThreadLightDumpRes)

PCmdActiveThreadCount = _reflection.GeneratedProtocolMessageType('PCmdActiveThreadCount', (_message.Message,), {
  'DESCRIPTOR' : _PCMDACTIVETHREADCOUNT,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdActiveThreadCount)
  })
_sym_db.RegisterMessage(PCmdActiveThreadCount)

PCmdActiveThreadCountRes = _reflection.GeneratedProtocolMessageType('PCmdActiveThreadCountRes', (_message.Message,), {
  'DESCRIPTOR' : _PCMDACTIVETHREADCOUNTRES,
  '__module__' : 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:v1.PCmdActiveThreadCountRes)
  })
_sym_db.RegisterMessage(PCmdActiveThreadCountRes)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)