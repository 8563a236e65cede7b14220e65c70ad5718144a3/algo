"""
    test_client_connection
    ----------------------

    Test client connection class and functionality
"""
import pytest
import re
from .context import connection

# ( (host, port), expected )
check_valid_data = (
    (("127.0.0.1", 80), connection.Connection),
    (("localhost", 80), connection.Connection),
    ((5, 80), TypeError),
    ((None, None), TypeError),
    (("localhost", None), TypeError),
    (("", 80), ValueError),
    (("localhost", -50), ValueError),
    (("example.not.exist", 80), ValueError),
    (("localhost", 60000), ValueError)
)


def create_error_regex(error_messages):
    error_regex = "("

    for i in range(len(error_messages)):
        if i == len(error_messages) - 1:
            error_regex += error_messages[i] + r")"
        else:
            error_regex += error_messages[i] + r"|"
    return error_regex


@pytest.mark.parametrize("conn_param,expected", check_valid_data)
def test_connection_check_valid(conn_param, expected):

    if expected == connection.Connection:
        conn = connection.Connection(conn_param[0], conn_param[1])
        assert isinstance(conn, connection.Connection)
    elif expected == TypeError:
        error_messages = [
            r"Host Type invalid",
            r"Port Type invalid"
        ]
        error_regex = create_error_regex(error_messages)

        with pytest.raises(TypeError, match=error_regex):
            conn = connection.Connection(conn_param[0], conn_param[1])
    elif expected == ValueError:
        error_messages = [
            r"Host name empty",
            r"Negative port number supplied",
            r"Cannot resolve host address",
            r"Host and Port not reachable"
        ]
        error_regex = create_error_regex(error_messages)

        with pytest.raises(ValueError, match=error_regex):
            conn = connection.Connection(conn_param[0], conn_param[1])
