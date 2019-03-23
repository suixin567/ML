using UnityEngine;
using System.Collections;

public class DriverCamera : MonoBehaviour {
	public static DriverCamera instance; 
	Camera mCam;
	int  width = 1000;
	int height =600;
	// Use this for initialization
	void Start () {
		instance = this;
		mCam = Camera.main;
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.Z)) {
            MakeCameraImg();
		}
	}


    //把摄像头视野 打印出png图片
	public void MakeCameraImg()
    {
        RenderTexture rt = new RenderTexture(width, height, 3);
        mCam.pixelRect = new Rect(0, 0, Screen.width, Screen.height);
        mCam.targetTexture = rt;
        Texture2D screenShot = new Texture2D((int)(width), (int)(height),
                                                 TextureFormat.RGB24, false);
        mCam.Render();
        RenderTexture.active = rt;
        screenShot.ReadPixels(new Rect(0, 0, width, height), 0, 0);
        mCam.targetTexture = null;
        RenderTexture.active = null;
        UnityEngine.Object.Destroy(rt);
        byte[] bytes = screenShot.EncodeToPNG();
		string filename =Application.dataPath;
		filename = filename.Substring (0,filename.LastIndexOf("/"))	+ "/training_data/0.jpg";
           //               + System.DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss") + ".png";
        System.IO.File.WriteAllBytes(filename, bytes);

    }
}
