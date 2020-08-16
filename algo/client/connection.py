"""
    A class representing a connection to the server
    -----------------------------------------------

    Wraps the :mod:`socket` interface for low-level communication
    with the algo server.
"""
import socket
import subprocess
from typing import Dict


class Connection:

    def __init__(self, host: str, port: int):
        self.host: str = host
        self.port: int = port
        self.check_valid()

    def check_valid(self) -> None:
        """
            Check :meth:`algo.client.connection.Connection.__init__` arguments
            ------------------------------------------------------------------

            If MyPy or a linter has not been run on a user script, pick up
            type errors here and raise. Also check if given host and port is a
            reachable, resolvable address.
        """
        arg_types: Dict[str, type] = {"host": str, "port": int}
        host_type_fine: bool = isinstance(self.host, arg_types.get("host"))
        port_type_fine: bool = isinstance(self.port, arg_types.get("port"))

        # Check arguments of the correct type
        if not host_type_fine:
            raise TypeError("Host Type invalid")
        if not port_type_fine:
            raise TypeError("Port Type invalid")

        # Check for common errors in supplied values
        if self.host == "":
            raise ValueError("Host name empty")
        if not (self.port > 0):
            raise ValueError("Negative port number supplied")

        # Check if host address is resolvable
        try:
            socket.gethostbyname(self.host)
        except socket.gaierror as err:
            raise ValueError("Cannot resolve host address")

        # Check if host and port are reachable
        sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        reachable: int = sock.connect_ex((self.host, self.port))
        sock.close()
        if not reachable:
            raise ValueError("Host and Port not reachable")
