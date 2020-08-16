"""A class representing a connection to the server.

Wraps the :mod:`socket` interface for low-level communication
with the algo server.
"""
import socket
from typing import Dict, Any


class Connection:

    def __init__(self, host: str, port: int):
        self.host: str = host
        self.port: int = port
        self.check_valid()

    def check_valid(self):
        arg_types: Dict[str, type] = {"host": str, "port": int}
        host_fine: bool = isinstance(self.host, arg_types.get("host"))
        port_fine: bool = isinstance(self.port, arg_types.get("port"))
        if not (host_fine and port_fine):
            raise TypeError("Host or port invalid")

