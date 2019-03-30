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
                HOST = '127.0.0.1'
                PORT = 7999
                self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.s.connect((HOST, PORT))       #要连接的IP与端口
                #开启一个线程进行监听消息
                self.th = Thread(target=self.listen, args=(99,))
                self.th.start()
                print("套接字初始化完成...");

        def listen(self,arg):
                while g.run:
                        data = self.s.recv(1024)
                        self.receive(data)


        def receive(self,data):

                model = data.decode()
                dict = json.loads(model)
                model = SocketModel()
                model.__dict__.update(dict)


                # print(model.Message)
                if model.Message == "exit":
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")
                        print("收到退出指令----------------------》》》》")

                        g.run = False

                if model.Message == "yes":
                    print("收到消息：YYYYYYYYYY")
                    print("收到消息：YYYYYYYYYY")
                    print("收到消息：YYYYYYYYYY")
                    print("收到消息：YYYYYYYYYY")
                    print("收到消息：YYYYYYYYYY")

                if model.Message == "no":
                        print("收到消息：NNNNNNNNNNNN")
                        print("收到消息：NNNNNNNNNNNN")
                        print("收到消息：NNNNNNNNNNNN")
                        print("收到消息：NNNNNNNNNNNN")
                        print("收到消息：NNNNNNNNNNNN")
                        g.feedback.state = "no"

                #unity截图完成
                if model.Message == "cameraok":
                        g.feedback.state = "cameraok"



        def send(self,msg):
                model = SocketModel()
                model.Message = msg
                message = json.dumps(model.__dict__)
                self.s.sendall(message.encode())  # 把命令发送给对端


