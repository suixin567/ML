using UnityEngine;
using System.Collections;

public class RetinaCells : MonoBehaviour {

    public int index = -1;
    public Color oldColor;
    public Transform ActivateCellParent;
    GameObject gameObject;
    // Use this for initialization
    void Start () {
        gameObject = new GameObject();
        gameObject.name = index.ToString();
        gameObject.transform.SetParent(ActivateCellParent);
        gameObject.AddComponent<ActivateCell>();
        Vector3 pos = transform.localPosition;
        gameObject.transform.localPosition = pos;
    }
	

    public void set(Color newColor) {
        if (oldColor != newColor)
        {
            //Debug.Log("im changed" + index);
            gameObject.GetComponent<ActivateCell>().count++;

        }
        this.oldColor = newColor;
    }
}
