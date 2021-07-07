import socket


def recv(udb_socket: socket):
    recv_data = udb_socket.recvfrom(1024)
    print("%s:%s说%s" % (str(recv_data[1][0]), str(recv_data[1][-1]), recv_data[0].decode("utf-8")))


def send(udb_socket: socket, port: int):
    input_data = input("请输入：")
    udb_socket.sendto(input_data.encode("utf-8"), ("", port))
