using UnityEngine;
using System.Collections;

public class ObjectsHolder : MonoBehaviour {

	public static ObjectsHolder instance;

	public GameObject[] objs;
	int currentIndex = -1;

	// Use this for initialization
	void Start () {
		instance = this;
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown(KeyCode.Space)) {
			RandomObj ();
		}
	}

	public void RandomObj(){
		
		for (int i = 0; i < objs.Length; i++) {
			objs [i].SetActive (false);
		}
		currentIndex  = Random.Range(0,objs.Length );
		objs [currentIndex].SetActive (true);
		print ("切换物体"+objs [currentIndex].name);
	}

	public void Prediction(string value){
		if (int.Parse(value) == currentIndex) {
			ServerForUnity.server.SendMessage(1,2,3, "yes");
		} else {
			ServerForUnity.server.SendMessage(1,2,3, "no");
		}
	}
}
