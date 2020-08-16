"""
    test_client_connection
    ----------------------

    Test client connection class and functionality
"""
import pytest
from .context import connection

check_valid_data = (
    ("127.0.0.1", 80),
    ("localhost", 80),
    (5, 60)
)


@pytest.mark.parametrize("host,port", check_valid_data)
def test_connection_check_valid(host, port):
    conn = connection.Connection(host, port)
    assert isinstance(conn, connection.Connection)
