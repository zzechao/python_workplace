import socket
import udp


def main():
    udb_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udb_socket.bind(("", 2244))

    while True:
        udp.send(udb_socket, 2245)
        udp.recv(udb_socket)

    udb_socket.close()


if __name__ == "__main__":
    main()
