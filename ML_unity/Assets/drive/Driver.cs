using UnityEngine;
using System.Collections;

public class Driver : MonoBehaviour {

    public static Driver driver;

	// Use this for initialization
	void Start () {
        driver = this;
    }
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.W)) {
            forward();
        }

        if (Input.GetKeyDown(KeyCode.A))
        {
            left();
        }

        if (Input.GetKeyDown(KeyCode.D))
        {
            right();
        }


        if (Input.GetKeyDown(KeyCode.Q))
        {
            send("exit");
        }
        //模拟发生碰撞
        if (Input.GetKeyDown(KeyCode.Space))
        {
            send("collision");
        }

    }






    public void forward() {
        transform.Translate(Vector3.forward * 20*Time.deltaTime);
    }

    public void left() {
        transform.Rotate(Vector3.up, -15);
    }

    public void right() {
        transform.Rotate(Vector3.up, 15);
    }


    // 碰撞开始
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name.StartsWith("wall"))
        {
			Debug.LogWarning("碰撞" + collision.gameObject.name);
			send("collision");
        }
        
    }

    //发送一个命令给python
    public void send(string msg) {

        ServerForUnity.server.SendMessage(1,2,3, msg);
    }
}
