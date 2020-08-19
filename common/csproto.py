"""
    Client Server Protocol
    -------------------------------

    Contains constants for client server communication and other helper functions
"""
import enum


class PROTO(enum.Enum):
    """
    The constants used in fixed size headers to denote the type of
    request from the client or response from the server.
    """
    HEARTBEAT = 1
    HEARTBEAT_RESPONSE = 2
