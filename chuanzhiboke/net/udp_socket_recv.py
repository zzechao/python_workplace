import socket
import udp


def main():
    udb_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udb_socket.bind(("", 2245))

    while True:
        udp.recv(udb_socket)
        udp.send(udb_socket, 2244)

    udb_socket.close()


if __name__ == "__main__":
    main()
