using UnityEngine;
using System.Collections;

public class Rotate : MonoBehaviour {
    public int speed = 1;
	// Use this for initialization
	void Start () {
        StartCoroutine(y());
	}
	

    IEnumerator y() {
        int count = 0;
        while (count < 200) {
            yield return new WaitForSeconds(Time.deltaTime);
            count++;
            transform.Rotate(new Vector3(0, speed, 0));
        }
        yield return null;
        StartCoroutine(x());
    }
    IEnumerator x()
    {
        int count = 0;
        while (count < 200)
        {
            yield return new WaitForSeconds(Time.deltaTime);
            count++;
            transform.Rotate(new Vector3(speed,0, 0));
        }
        yield return null;
        StartCoroutine(z());
    }

    IEnumerator z()
    {
        int count = 0;
        while (count < 200)
        {
            yield return new WaitForSeconds(Time.deltaTime);
            count++;
            transform.Rotate(new Vector3( 0, 0,speed));
        }
        yield return null;
        StartCoroutine(x());
    }
}
