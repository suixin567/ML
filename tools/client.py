# -*- coding: utf-8 -*-
import json
import socket

class SocketModel(object):
        def __init__(self):
                self.Type=1
                self.Area = 2
                self.Command = 3
                self.Message = "hello"



class Client(object):
        def __init__(self):
                self.run = True
                HOST = '127.0.0.1'
                PORT = 7999
                self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.s.connect((HOST, PORT))       #要连接的IP与端口
                self.send()
                while self.run:
                        data = self.s.recv(1024)
                        self.receive(data)


        def receive(self,data):
                model = data.decode()
                dict = json.loads(model)
                model = SocketModel()
                model.__dict__.update(dict)
                print(model.Message)



        def send(self):
                model = SocketModel()
                message = json.dumps(model.__dict__)
                self.s.sendall(message.encode())  # 把命令发送给对端

        def close(self):
                self.run = False  # 关闭连接
                self.s.close()




