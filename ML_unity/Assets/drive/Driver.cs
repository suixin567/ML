using UnityEngine;
using System.Collections;

public class Driver : MonoBehaviour {

    public static Driver driver;

	string lastAction;//上一个动作


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
		lastAction = "forward";
    }

    public void left() {
        transform.Rotate(Vector3.up, -15);
		lastAction = "left";
    }

    public void right() {
        transform.Rotate(Vector3.up, 15);
		lastAction = "right";
    }


    // 碰撞开始
	void OnTriggerEnter(Collider collision)
    {
        if (collision.gameObject.name.StartsWith("wall"))
        {
			Debug.LogWarning("碰撞" + collision.gameObject.name);
			//回到上一步的位置
			switch (lastAction) {
			case "forward":
				transform.Translate(- Vector3.forward * 20*Time.deltaTime);
				break;
			case "left":
				transform.Rotate(Vector3.up, 15);
				break;
			case "right":
				transform.Rotate(Vector3.up, -15);
				break;
			default:
				Debug.LogError ("未知动作！");
				break;
			}
			send("collision");
        }
        
    }

    //发送一个命令给python
    public void send(string msg) {

        ServerForUnity.server.SendMessage(1,2,3, msg);
    }
}
