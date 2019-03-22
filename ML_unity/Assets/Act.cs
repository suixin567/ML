using UnityEngine;
using System.Collections;
using UnityEngine.UI;
public class Act : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}

    public void eee() {
        Texture2D t2d = GetComponent<Image>().material.mainTexture as Texture2D;
        if (t2d!=null)
        {
            Color[] cols = t2d.GetPixels();
            MyMat mymat = new MyMat();
            int count = 0;
            int y = -1;

            for (int i = 0; i < cols.Length; i++)
            {
                if (i% cols.Length==0)
                {
                    y++;
                    count = 0;
                
                    mymat.data[count, y] = cols[i];
                }
            }

            Debug.Log(mymat.data);


        }
      
    }
	
	
}
