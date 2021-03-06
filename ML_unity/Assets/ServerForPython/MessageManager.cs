﻿using UnityEngine;
using System.Collections;
using System.Collections.Generic;


public class MessageManager : MonoBehaviour
{
    public static MessageManager instance;

    void Awake()
    {
        instance = this;
        StartCheckMessage();
    }

    /// <summary>
    /// 开始检测消息
    /// </summary>
    public void StartCheckMessage()
    {
        StartCoroutine(checkMessage());

    }

    IEnumerator checkMessage()
    {
        while (true)
        {
            yield return new WaitForSeconds(Time.deltaTime);

            List<string> list = ServerForUnity.server.getList();
            if (list == null)
            {
                continue;
            }
            for (int i = 0; i < 8; i++)
            {
                if (list.Count > 0)
                {
                    string modelStr = list[0];
                    OnMessage(modelStr);
                    list.RemoveAt(0);
                }
                else
                {
                    break;
                }
            }
        }
    }


    public void OnMessage(string modelStr)
    {
        SocketModel model = Coding<SocketModel>.decode(modelStr);
        if (model == null)
        {
            return;
        }
        //Debug.Log("收到了" + model.Message);
        switch (model.Message)
        {
            case UnityProtocol.CAMERA:
                ObjectsHolder.instance.RandomObj();
                DriverCamera.instance.MakeCameraImg();
                ServerForUnity.server.SendMessage(1, 2, 3,UnityProtocol.CAMERA_OK);
                break;
            default:
                ObjectsHolder.instance.Prediction(model.Message);
                break;
        }
    }

}