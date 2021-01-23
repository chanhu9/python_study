#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/7 16:28

import socket
import threading
import sys
import framework

class HttpWebServer:

    def __init__(self):
        server_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print(server_tcp_socket)

        server_tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        server_tcp_socket.bind(("", 9007))
        server_tcp_socket.listen(128)
        self.server_tcp_socket = server_tcp_socket


    def start(self):

        while True:
            service_client_socket, ip_port = self.server_tcp_socket.accept()
            print(service_client_socket)
            print(f"客户端的ip地址和端口号:{ip_port}")

            socket_thread = threading.Thread(target=self.run2, args=(service_client_socket, ip_port))
            # socket_thread.setDaemon(True)
            socket_thread.start()

    @staticmethod
    def run2(service_client_socket, ip_port):

        while True:

            recv_data = service_client_socket.recv(1024)

            recv_data_length = len(recv_data)
            print(f"接受的数据长度为{recv_data_length}")

            if recv_data_length == 0:

                # service_client_socket.close()
                break

            else:

                recv_content = recv_data.decode("gbk")
                print(f"接受的客户端{ip_port}内容:{recv_content}")

                recv_datas = recv_content.split(" ", 2)

                request_path = recv_datas[1]
                print(request_path)

                if request_path == "/":
                    request_path = "/index.html"

                if request_path.endswith(".html"):

                    env = {"request_path": request_path}

                    status , headers, res = framework.handle_request(env)
                    "拼接响应报文"
                    response_header = ""
                    response_line = "HTTP/1.1 %s\r\n"%status
                    for header in headers:
                        # response_header = response_header + (header[0] + ":" + header[1] + "\r\n")
                        response_header = response_header + ("%s:%s\r\n")%header

                    response_data = (response_line + \
                                    response_header + \
                                    "\r\n"+ \
                                    res)
                    print(f"响应数据{response_data}")
                    send_data = response_data.encode("utf-8")

                    service_client_socket.send(send_data)


                else:

                    try:
                        with open("E:\work--doc2\day06\static" + request_path, "rb") as f:
                            data = f.read()

                    except Exception:
                        response_line = "HTTP/1.0 404 not found\r\n"
                        response_headers = "Server: SimpleHTTP/0.6 Python/3.7.0\r\n"
                        with open("E:\work--doc2\day06\static\error.html", "rb") as f:
                            data = f.read()

                        response_body = data

                        response_data = (response_line + response_headers + "\r\n").encode("utf-8") + response_body

                    else:
                        "响应行"
                        response_line = "HTTP/1.0 200 OK\r\n"
                        "响应头"
                        response_headers = "Server: SimpleHTTP/0.6 Python/3.7.0\r\n"
                        "空行"
                        "响应体"
                        response_body = data

                        response_data = (response_line + response_headers + r"\r\n").encode("utf-8") + response_body

                    # # send_content = "收到，发起进攻"
                    # send_data = send_content.encode("gbk")

                    finally:

                        send_data = response_data

                        service_client_socket.send(send_data)

                        # service_client_socket.close()

        service_client_socket.close()


def main():
    web_server = HttpWebServer()
    web_server.start()

#     data = sys.argv
#     port = data[1]
#
#     if len(data) != 2:
#         print("长度必须是2位")
#         return
#
#     if port.isdigit():
#         web_server = HttpWebServer()
#         web_server.start()
#
#     else:
#         print("端口必须是数字")

if __name__ == '__main__':
    main()
