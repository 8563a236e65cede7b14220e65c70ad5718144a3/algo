"""
    test_server_clientcon
    ----------------------

    Test server client
"""
import threading
import time
import socket
import pytest

from .context import clientcon


def start_server():
    listening_socket = clientcon.ClientListener("localhost", 10000, 5)


def test_client_con():
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    time.sleep(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 10000))
    sock.sendall(b"hello world")

    response = sock.recv(1024)

    sock.close()
    server_thread.join()

    assert response == b"closing"
