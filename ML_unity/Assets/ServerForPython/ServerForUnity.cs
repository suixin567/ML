using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;


public class ServerForUnity : MonoBehaviour
{

    public static ServerForUnity server;

    #region 属性
    Socket tcpServer;
    private static string ipAddress = "127.0.0.1";
    private static int port = 7999;
    Thread th;
    List<string> msgList = new List<string>();
    #endregion

    void Awake()
    {
        server = this;
    }

    public void Start()
    {
        try
        {
            th = new Thread(new ThreadStart(startServer));
            th.Start();
        }
        catch (Exception err)
        {
            Debug.Log("服务器开启失败" + err.ToString());
        }
    }

    void startServer()
    {
        try
        {
            tcpServer = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            tcpServer.Bind(new IPEndPoint(IPAddress.Parse(ipAddress), port));
            tcpServer.Listen(1);//最大连接数
            Debug.Log("Unity服务器开启");
            while (true)
            {
                try
                {
                    clientSocket = tcpServer.Accept();
                    ReceiveMessage();
                }
                catch
                {
                }
            }
        }
        catch (Exception e)
        {
            Debug.Log("服务器启动失败...");
        }

    }

    private Socket clientSocket;

    static int maxBufferSize = 102400;
    private byte[] data = new byte[maxBufferSize];//存放客户端发来的数据

    private void ReceiveMessage()
    {
        while (true)
        {
            try
            {

                int length = clientSocket.Receive(data);
                if (length >= maxBufferSize)
                {
                    Debug.Log("收到超长数据");
                }
                string message = Encoding.UTF8.GetString(data, 0, length);
                if (message == "") {
                    throw new Exception();
                }
                this.msgList.Add(message);
            }
            catch (Exception e)
            {
                Debug.Log("python断开..."+e);
                break;
            }

        }
    }

    public void SendMessage(int type, int area, int command, string message)
    {
        SocketModel model = new SocketModel();
        model.Type = type;
        model.Area = area;
        model.Command = command;
        model.Message = message;

        string message2 = Coding<SocketModel>.encode(model);
        byte[] data = Encoding.UTF8.GetBytes(message2);
        try
        {
            clientSocket.Send(data);
        }
        catch (Exception err)
        {
            Debug.Log("向Unity发送消息失败！" + err.ToString());
        }

    }




    public List<string> getList()
    {
        return this.msgList;
    }


}

