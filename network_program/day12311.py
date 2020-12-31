#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/31 11:14


import socket

if __name__ == '__main__':
    server_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(server_tcp_socket)

    server_tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    server_tcp_socket.bind(("", 9004))
    server_tcp_socket.listen(128)

    service_client_socket, ip_port = server_tcp_socket.accept()
    print(service_client_socket)
    print(f"客户端的ip地址和端口号:{ip_port}")

    recv_data = service_client_socket.recv(1024)
    recv_data_length = len(recv_data)
    print(f"接受的数据长度为{recv_data_length}")


    recv_content = recv_data.decode("gbk")
    print(f"接受的客户端内容:{recv_content}")

    send_content = "收到，发起进攻"
    send_data = send_content.encode("gbk")

    service_client_socket.send(send_data)

    service_client_socket.close()
    server_tcp_socket.close()









