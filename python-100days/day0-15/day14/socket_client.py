from socket import socket
def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    client.connect(('127.0.0.1',7865))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()