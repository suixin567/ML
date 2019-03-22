using UnityEngine;
using System.Collections;
using System.IO;
using UnityEngine.UI;

public class GetImage : MonoBehaviour
{
    public RenderTexture rt;  //声明一个截图时候用的中间变量 
    Texture2D t2d;
    Texture2D memt2d;
    Texture2D activatet2d;

    public Image activateImg;
    void Start()
    {
        t2d = new Texture2D(rt.width, rt.height, TextureFormat.RGB24, false);
        memt2d = new Texture2D(rt.width, rt.height, TextureFormat.RGB24, false);
        activatet2d = new Texture2D(rt.width, rt.height, TextureFormat.RGB24, false);
        Camera.main.targetTexture = rt;
        Debug.Log("图片尺寸："+t2d.width+" x "+ t2d.height);
    }

    void Update()
    {
            //截图到t2d中
            RenderTexture.active = rt;
            t2d.ReadPixels(new Rect(0, 0, rt.width, rt.height), 0, 0);
            t2d.Apply();
            RenderTexture.active = null;

            Color[] cols = t2d.GetPixels();
            Color[] cols2 = memt2d.GetPixels();
            Color[] cols3 = new Color[cols.Length];

            for (int i = 0; i < cols.Length; i++)
            {
                if (cols[i]!= cols2[i])
                {
                    cols3[i] = cols[i];
                }
        }
       

        memt2d.SetPixels(cols);
        memt2d.Apply();
        activatet2d.SetPixels(cols3);
        activatet2d.Apply();

        activateImg.material.mainTexture = activatet2d;
        activateImg.GetComponent<Act>().eee();

        //将图片保存起来
        //byte[] byt = t2d.EncodeToJPG();
        //File.WriteAllBytes(Application.dataPath + "//" + num.ToString() + ".jpg", byt);
    }
}