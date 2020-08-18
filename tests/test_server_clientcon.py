"""
    test_server_clientcon
    ----------------------

    Test server client
"""
import pytest
from .context import connection
from .context import clientcon


def test_client_con():
    listening_socket = clientcon.ClientListener("localhost", 10000, 5)
    print(listening_socket)
    print("here")
