import threading
import socket
# 客服端
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("192.168.15.6", 60001))
addr = None


def read():
    while True:
        try:
            result = server.recvfrom(1024)
            print(result)
            global addr
            addr = result[1]
        except:
            print("end")
            break


def write():
    while True:
        try:
            info = input("输入发送内容：")
            if info.__eq__("exit"):
                server.close()
                break
            else:
                server.sendto(info.encode("utf8"), addr)
        except:
            print("end")
            break


t1 = threading.Thread(target=read)
t2 = threading.Thread(target=write)
t1.start()
t2.start()