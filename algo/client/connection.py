"""A class representing a connection to the server.

Wraps the :mod:`socket` interface for low-level communication
with the algo server.
"""
import socket


class Connection:

    def __init__(self, host: str, port: int):
        self.host: str = host
        self.port: int = port
