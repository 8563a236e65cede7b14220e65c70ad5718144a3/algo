"""
    Client Server Protocol
    -------------------------------

    Contains constants for client server communication and other helper functions
"""
import enum


class PROTO(enum.Enum):
    HEARTBEAT = 1
    HEARTBEAT_RESPONSE = 2
