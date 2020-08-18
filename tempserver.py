"""
    test_server_clientcon
    ----------------------

    Test server client
"""
from server.clientcon import ClientListener


def test_client_con():
    listening_socket = ClientListener("localhost", 10000, 5)
    print(listening_socket)
    print("here")


def main():
    test_client_con()


if __name__ == '__main__':
    main()
