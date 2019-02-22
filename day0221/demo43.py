"""
HTTP TCP 编写Web服务器
"""
import socket
from threading import Thread

# 5 开启接受客户端数据的线程


def recvThread(cli):
    print(cli.getpeername(),"连接了")
    data = cli.recv(1024).decode("utf-8")
    if len(data) == 0:
        print(cli.getpeername(), "断开了")
    else:
        filename = data.split(" ")[1]
        # print(filename)
        responseLine = "HTTP/1.1 200 OK\r\n"
        responseHeader = "Content-Type: text/html\r\n"
        responseNUllLIne = "\r\n"
        try:
            with open("templates" + filename, "rb") as f:
                responseBody = f.read()
        except:
            with open("templates/404.html","rb") as f:
                responseBody = f.read()
        cli.send(responseLine.encode("utf-8"))
        cli.send(responseHeader.encode("utf-8"))
        cli.send(responseNUllLIne.encode("utf-8"))
        cli.send(responseBody)

    cli.close()


if __name__ == "__main__":
    # 1创建socket服务端
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2 绑定地址
    SERVERADDR = ("192.168.15.6", 9999)
    serverSocket.bind(SERVERADDR)
    # 3开启监听
    serverSocket.listen()

    # 4开始接受客户端连接
    while True:
        clientSocket, clientAddr = serverSocket.accept()
        rThread = Thread(target=recvThread, args=(clientSocket,))
        rThread.start()
