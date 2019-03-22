using UnityEngine;
using System.Collections;

public class ActivateCell : MonoBehaviour {

    public int count=0;
	// Use this for initialization
	void Start () {
        //Invoke("des",0.2f);
	}
    void des() {
        Destroy(gameObject);
    }

}
