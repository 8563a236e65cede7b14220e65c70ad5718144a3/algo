"""
    test_client_connection
    ----------------------

    Test client connection class and functionality
"""
from client import connection


def main():
    conn = connection.Connection("localhost", 10000)


if __name__ == "__main__":
    main()