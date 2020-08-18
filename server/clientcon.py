"""
    Low level communication with clients
    -------------------------------------------------------------

    Wraps the :mod:`socket` interface for low-level communication
    with the :mod:`client`.
"""
import socket
import selectors
from typing import List, Any


class ClientListener:
    """
    The main listener for client connections. Keeps track of all
    client connections and maintains the socket selector for
    multiplexed I/O

    .. automethod:: __init__
    """

    def __init__(self, address: str, port: int, max_con: int) -> None:
        self.clients: List[ClientConnection] = list()
        self.address: str = address
        self.port: int = port
        self.selector: selectors.DefaultSelector = selectors.DefaultSelector()
        self.server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.bind(address)
        self.server.listen(max_con)

        self.selector.register(self.server, selectors.EVENT_READ, self.accept)

    def accept(self, sock: socket.socket) -> None:
        """
        Create an instance of ClientConnection and store for later use
        :param sock: the socket returned from the listener
        :type sock: socket.socket
        :return: None
        """
        new_connection: socket.socket
        address: Any

        (new_connection, address) = sock.accept()
        new_connection.setblocking(False)
        client_con: ClientConnection = ClientConnection(new_connection)
        self.clients.append(client_con)
        self.selector.register(new_connection, selectors.EVENT_READ, client_con.read)

    def read(self):
        pass


class ClientConnection:
    """
    A class representing a client connection. Handles low-level
    socket communication, receiving requests and sending back data.
    """

    def __init__(self, sock: socket.socket, id: int) -> None:
        self.socket: socket.socket = sock
        self.buffer: str = str()
        self.id: int = id

    def read(self, sock, mask):
        self.buffer += self.sock.recv(1024)
