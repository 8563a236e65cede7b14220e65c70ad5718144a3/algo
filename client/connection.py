"""
    Low level client communication with server
    -------------------------------------------------------

    Wraps the :mod:`socket` interface for low-level communication
    with the :mod:`algo.server`.
"""
import socket
from typing import Dict, Union


class Connection:
    """
    Contains a variety of helper functions for communication
    over socket and error checking

    .. automethod:: __init__
    """
    def __init__(self, host: str, port: int) -> None:
        """
        Assigns connection parameters to instance variables
        and checks received parameters for errors.

        :param host: the local or remote server's name or ip address
        :type host: str
        :param port: the port number to connect to
        :type port: int
        :returns: None
        """
        self.host: str = host
        self.port: int = port
        self.check_valid()

    def check_valid(self) -> None:
        """
        Pick up any type errors or value errors
        from :meth:`Connection.__init__`
        and raise. Also check if given host and port is a
        reachable, resolvable address.

        :returns: None
        """
        arg_types: Dict[str, Union[str, int]] = {"host": str(), "port": int()}
        host_type_fine: bool = isinstance(self.host, type(arg_types.get("host")))
        port_type_fine: bool = isinstance(self.port, type(arg_types.get("port")))

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

        if reachable:
            raise ValueError("Host and Port not reachable")