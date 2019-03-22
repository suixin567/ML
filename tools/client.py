# -*- coding: utf-8 -*-
import json
import socket
from threading import Thread
import g

class SocketModel(object):
        def __init__(self):
                self.Type=1
                self.Area = 2
                self.Command = 3
                self.Message = ""



class Client(object):
        def __init__(self):
                self.run = True
                HOST = '127.0.0.1'
                PORT = 7999
                self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.s.connect((HOST, PORT))       #要连接的IP与端口
                #开启一个线程进行监听消息
                self.th = Thread(target=self.listen, args=(99,))
                self.th.start()

        def listen(self,arg):
                while self.run:
                        data = self.s.recv(1024)
                        self.receive(data)


        def receive(self,data):
                model = data.decode()
                dict = json.loads(model)
                model = SocketModel()
                model.__dict__.update(dict)
                print(model.Message)
                if model.Message == "exit":
                        self.run = False
                #发生了碰撞
                if model.Message == "collision":
                        g.feedback.state = "collision"



        def send(self,msg):
                model = SocketModel()
                model.Message = msg
                message = json.dumps(model.__dict__)
                self.s.sendall(message.encode())  # 把命令发送给对端


