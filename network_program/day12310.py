#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/31 10:20

import socket
import time

if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.11.24", 9003))
    time.sleep(10)
    send_data = "hello，world".encode("gbk")

    tcp_client_socket.send(send_data)
    recv_data = tcp_client_socket.recv(1024)
    # print(recv_data)
    print(recv_data.decode("gbk"))

    tcp_client_socket.close()
