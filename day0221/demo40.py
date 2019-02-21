"""
TCP客户端
"""
import socket
from threading import Thread


def readThread():
    BUFFERSIZE = 1024*1024
    while True:
        try:
            databytes = clientSocket.recv(BUFFERSIZE)
            if len(databytes) == 0:
                clientSocket.close()
                break
            else:
                datastr = databytes.decode("gbk")
                print("收到消息", datastr)
        except Exception as e:
            print(e)
            break


def sendThread():
    while True:
        try:
            if clientSocket._closed:
                break
            else:
                touser = input("请输入接受消息的用户")
                datastr = input("请输入发送内容")
                sendstr = touser+"|"+datastr
                print(sendstr)
                sendbytes = sendstr.encode("gbk")
                clientSocket.send(sendbytes)
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    try:
        # 1创建服务器端通信对象
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2连接服务器
        SERVERADDR = ("192.168.15.6", 9999)
        clientSocket.connect(SERVERADDR)
        # 2.5 添加用户系统
        username = input("请输入用户名")
        usernamebytes = username.encode("gbk")
        clientSocket.send(usernamebytes)

        # 3创建两个线程用于收发服务器消息
        tread = Thread(target=readThread)
        tread.start()
        tsend = Thread(target=sendThread)
        tsend.start()
    except Exception as e:
        print(e)

# TODO 添加心跳检测
"""

心跳包：检测网络是否正常连接
       客户端和服务器一直（通常都是毫秒级）在进行无意义的数据交互，
       如果不能正常收到消息，证明离线
"""




