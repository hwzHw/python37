import threading
import socket

# 服务端
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def read():
    client.sendto("".encode("utf8"), ("192.168.15.6", 60001))
    while True:
        try:
            result = client.recvfrom(1024)
            print(result[0].decode("utf8"))
        except :
            print("end")
            break


def write():
    while True:
        str1 = input("输入内容：")
        if str1.__eq__("exit"):
            client.close()
            print(client)

            # client = None
            break
        else:
            client.sendto(str1.encode("utf8"), ("192.168.15.6", 60000))


tread = threading.Thread(target=read)
twrite = threading.Thread(target=write)
tread.start()
twrite.start()
