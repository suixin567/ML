using UnityEngine;
using System.Collections;

public class MyMat {

    public Color[,] data;
    private int numbers;
    private int channels;
    private int width;
    private int height;
    private int id;

    public MyMat()
    {
        data = new Color[64,64];
    }

    public MyMat(int numbers, int channels, int height, int width)
    {
        this.numbers = numbers;
        this.channels = channels;
        this.height = height;
        this.width = width;
      //  data = new double[get4DSize()];
    }

    public int get4DSize()
    {
        return numbers * channels * width * height;
    }

}
