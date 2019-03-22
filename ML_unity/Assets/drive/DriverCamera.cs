using UnityEngine;
using System.Collections;

public class DriverCamera : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.Z)) {
            MakeCameraImg(Camera.main,1000,600);
        }
	}


    //把摄像头视野 打印出png图片
    private void MakeCameraImg(Camera mCam, int width, int height)
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
        string filename = Application.dataPath + "/imgs/"
                          + System.DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss") + ".png";
        System.IO.File.WriteAllBytes(filename, bytes);

    }
}
