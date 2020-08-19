"""
    Client Server Protocol
    -------------------------------

    Contains constants for client server communication and other helper functions
"""
import enum
import struct

proto_size = struct.Struct("I").size


class PROTO(enum.Enum):
    """
    The constants used in fixed size headers to denote the type of
    request from the client or response from the server.
    """
    HEARTBEAT = 1
    HEARTBEAT_RESPONSE = 2


def pack_proto(proto_enum: PROTO) -> bytes:
    packer: struct.Struct = struct.Struct("I")
    return packer.pack(proto_enum.value)


def unpack_proto(data: bytes) -> int:
    unpacker: struct.Struct = struct.Struct("I")
    unpacked_data: int = unpacker.unpack(data)[0]
    return unpacked_data
