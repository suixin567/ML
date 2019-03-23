import numpy as np
import tools.tool
import tools.tool2
import hippocampus2
import g

kernelV = np.array([[0,1,0],[0,1,0],[0,1,0]])
kernelH = np.array([[0,0,0],[1,1,1],[0,0,0]])
kernelcorner = np.array([[1,1,1],[1,1,1],[1,1,1]])
kernelLeft = np.array([[1,0,0],[0,1,0],[0,0,1]])
kernelRight = np.array([[0,0,1],[0,1,0],[1,0,0]])

hipp2 = hippocampus2.Hippocampus();


def begin(activateimg):

    #检测角点
    cornerResult = conv_corner(activateimg)
    collect_corner(cornerResult)

    # 检测垂直
    verticalResult = conv(activateimg, kernelV)
    collect_vertical(verticalResult)

    # 检测水平
    horizontalResult = conv(activateimg, kernelH)
    collect_horizontal(horizontalResult)

    #左侧检测
    leftResult = conv(activateimg, kernelLeft)
    collect_left(leftResult)

    #右侧检测
    rightResult = conv(activateimg, kernelRight)
    collect_Right(leftResult)

    # 上报完成
    hipp2.collect_features_ok()





def conv_corner(imgae):
    # 第一次卷积
    con_1 = tools.tool.conv_corner(imgae);
    print("第一次卷积后的最大值", con_1.max())
    # 第一次池化
    pool_1 = tools.tool.pool(con_1);
    print("第一次池化后的最大值", pool_1.max());
    # 第二次卷积
    con_2 = tools.tool.conv_corner(pool_1);
    print("第二次卷积后的最大值", con_2.max());
    # 第二次池化
    pool_2 = tools.tool.pool(con_2);
    print("第二次池化后的最大值", pool_2.max())
    # #第三次卷积
    con_3 = tools.tool.conv_corner(pool_2);
    print("第三次卷积后的最大值", con_3.max())
    tools.tool2.show(con_3, 100, "con_3")
    # 第三次池化
    pool_3 = tools.tool.pool(con_3);
    print("第三次池化后的最大值", pool_3.max())
    # #第四次卷积
    con_4 = tools.tool.conv_corner(pool_3);
    print("第四次卷积后的最大值", con_4.max())
    tools.tool2.show(con_4, 100, "con_4")
    # 第四次池化
    pool_4 = tools.tool.pool(con_4);
    print("第四次池化后的最大值", pool_4.max())
    # 第五次卷积
    con_5 = tools.tool.conv_corner(pool_4);
    print("第五次卷积后的最大值", con_5.max())
    tools.tool2.show(con_5, 200, "conv_5")
    return con_5


def collect_corner(image):
    Hi, Wi = image.shape
    interval = image.max() / 10  # 能量分为10个档次
    # print("interval" ,interval)
    engryArr = np.zeros(10)
    for i in range(Hi):
        for j in range(Wi):
            if image[i, j] > 0:  # 只统计有值的地方
                angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                if angleIndex < 0:  # 索引不可以为负数
                    angleIndex = 0
                temp = engryArr[angleIndex]
                temp = temp + 1
                engryArr[angleIndex] = temp
    print("角点能量分布", engryArr);
    old = int(g.frame) - 10000  # 检索之前的10000条数据
    if old < 0:
        old = 0

    # 进行辨别 (当前帧和之前的所有帧进行对比)
    for m in range(int(g.frame) - 1, old, -1):  # 遍历历史记忆(不包含此次记忆，所以-1) # 遍历历史记忆(不包含此次记忆，所以-1)  但这样的话，会导致第0帧的记忆不会被运行到。因为只有 range(3-1,0,-1)时才会运行。也就是说在第二帧时会检查第一帧，第一帧时不会去检查第0帧。
        score = 0
        for n in range(10):
            #print("比较的是：", str(m) + "_corner_" + str(n))
            #print("比较结果是：", g.r.get(str(m) + "_corner_" + str(n)), "    ", engryArr[n])
            if g.r.get(str(m) + "_corner_" + str(n)) == str(engryArr[n]):
                score = score + 10  # 增加10分
        if score == 100:
            print("历史激活器被激活，历史序号", m, "corner", "得分", score);
            # 上报此过滤器。
            hipp2.collect_features(str(m) + "_corner_")
            return  # 如果找到历史中此过滤器的雷同值，则停止继续查找。
    # 存储数据 （示例：88_corner7 = 2）
    for k in range(len(engryArr)):
        g.r.set(str(g.frame) + "_corner_" + str(k), engryArr[k])

###################################################################################

def conv(imgae, kernel):
    # 第一次卷积
    con_1 = tools.tool.conv_same(imgae, kernel);
    print("第一次卷积后的最大值", con_1.max())
    # 第一次池化
    pool_1 = tools.tool.pool(con_1);
    print("第一次池化后的最大值", pool_1.max());
    # 第二次卷积
    con_2 = tools.tool.conv_same(pool_1, kernel);
    print("第二次卷积后的最大值", con_2.max());
    # 第二次池化
    pool_2 = tools.tool.pool(con_2);
    print("第二次池化后的最大值", pool_2.max())
    # #第三次卷积
    con_3 = tools.tool.conv_same(pool_2, kernel);
    print("第三次卷积后的最大值", con_3.max())
    tools.tool2.show(con_3, 100, "con_3")
    # 第三次池化
    pool_3 = tools.tool.pool(con_3);
    print("第三次池化后的最大值", pool_3.max())
    # #第四次卷积
    con_4 = tools.tool.conv_same(pool_3, kernel);
    print("第四次卷积后的最大值", con_4.max())
    tools.tool2.show(con_4, 100, "con_4")
    # 第四次池化
    pool_4 = tools.tool.pool(con_4);
    print("第四次池化后的最大值", pool_4.max())
    # 第五次卷积
    con_5 = tools.tool.conv_same(pool_4, kernel);
    print("第五次卷积后的最大值", con_5.max())
    tools.tool2.show(con_5, 100, "conv_5")
    return con_5


def collect_vertical(image):
    Hi, Wi = image.shape
    interval = image.max() / 10  # 能量分为10个档次
    # print("interval" ,interval)
    engryArr = np.zeros(10)
    for i in range(Hi):
        for j in range(Wi):
            if image[i, j] > 0:  # 只统计有值的地方
                angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                if angleIndex < 0:  # 索引不可以为负数
                    angleIndex = 0
                temp = engryArr[angleIndex]
                temp = temp + 1
                engryArr[angleIndex] = temp
    print("垂直能量分布", engryArr);

    old = int(g.frame) - 10000  # 检索之前的10000条数据
    if old < 0:
        old = 0

    # 进行辨别 (当前帧和之前的所有帧进行对比)
    for m in range(int(g.frame) - 1, old, -1):  # 遍历历史记忆(不包含此次记忆，所以-1)  但这样的话，会导致第0帧的记忆不会被运行到。因为只有 range(3-1,0,-1)时才会运行。也就是说在第二帧时会检查第一帧，第一帧时不会去检查第0帧。
        score = 0
        for n in range(10):
            # print("比较的是：",str(m) + "_vertical_" + str(n))
            # print("比较结果是：",self.r.get(str(m) + "_vertical_" + str(n)),"    ",engryArr[n])
            if g.r.get(str(m) + "_vertical_" + str(n)) == str(engryArr[n]):
                score = score + 10  # 增加10分
        if score == 100:
            print("历史激活器被激活，历史序号", m, "vertical", "得分", score);
            # 上报此过滤器。
            hipp2.collect_features(str(m) + "_vertical_")
            return  # 如果找到历史中此过滤器的雷同值，则停止继续查找。

    # 存储数据 （示例：88_vertical7 = 2）
    for k in range(len(engryArr)):
        g.r.set(str(g.frame) + "_vertical_" + str(k), engryArr[k])
        #print(str(g.frame), "帧时，管道保存了一个新的记忆， key是", str(g.frame) + "_vertical_" + str(k), "数据是", engryArr[k],)





def collect_horizontal(image):
    Hi, Wi = image.shape
    interval = image.max() / 10  # 能量分为10个档次
    # print("interval" ,interval)
    engryArr = np.zeros(10)
    for i in range(Hi):
        for j in range(Wi):
            if image[i, j] > 0:  # 只统计有值的地方
                angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                if angleIndex < 0:  # 索引不可以为负数
                    angleIndex = 0
                temp = engryArr[angleIndex]
                temp = temp + 1
                engryArr[angleIndex] = temp
    print("水平能量分布", engryArr);

    old = int(g.frame) - 10000  # 检索之前的10000条数据
    if old < 0:
        old = 0

    # 进行辨别 (当前帧和之前的所有帧进行对比)
    for m in range(int(g.frame) - 1, old, -1):  # 遍历历史记忆(不包含此次记忆，所以-1)  但这样的话，会导致第0帧的记忆不会被运行到。因为只有 range(3-1,0,-1)时才会运行。也就是说在第二帧时会检查第一帧，第一帧时不会去检查第0帧。
        score = 0
        for n in range(10):
            # print("比较的是：",str(m) + "_vertical_" + str(n))
            # print("比较结果是：",self.r.get(str(m) + "_vertical_" + str(n)),"    ",engryArr[n])
            if g.r.get(str(m) + "_horizontal_" + str(n)) == str(engryArr[n]):
                score = score + 10  # 增加10分
        if score == 100:
            print("历史激活器被激活，历史序号", m, "horizontal", "得分", score);
            # 上报此过滤器。
            hipp2.collect_features(str(m) + "_horizontal_")
            return  # 如果找到历史中此过滤器的雷同值，则停止继续查找。

    # 存储数据 （示例：88_vertical7 = 2）
    for k in range(len(engryArr)):
        g.r.set(str(g.frame) + "_horizontal_" + str(k), engryArr[k])
        #print(str(g.frame), "帧时，管道保存了一个新的记忆， key是", str(g.frame) + "_horizontal_" + str(k), "数据是", engryArr[k],)






def collect_left(image):
    Hi, Wi = image.shape
    interval = image.max() / 10  # 能量分为10个档次
    # print("interval" ,interval)
    engryArr = np.zeros(10)
    for i in range(Hi):
        for j in range(Wi):
            if image[i, j] > 0:  # 只统计有值的地方
                angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                if angleIndex < 0:  # 索引不可以为负数
                    angleIndex = 0
                temp = engryArr[angleIndex]
                temp = temp + 1
                engryArr[angleIndex] = temp
    print("向左能量分布", engryArr);

    old = int(g.frame) - 10000  # 检索之前的10000条数据
    if old < 0:
        old = 0

    # 进行辨别 (当前帧和之前的所有帧进行对比)
    for m in range(int(g.frame) - 1, old, -1):  # 遍历历史记忆(不包含此次记忆，所以-1)  但这样的话，会导致第0帧的记忆不会被运行到。因为只有 range(3-1,0,-1)时才会运行。也就是说在第二帧时会检查第一帧，第一帧时不会去检查第0帧。
        score = 0
        for n in range(10):
            # print("比较的是：",str(m) + "_vertical_" + str(n))
            # print("比较结果是：",self.r.get(str(m) + "_vertical_" + str(n)),"    ",engryArr[n])
            if g.r.get(str(m) + "_left_" + str(n)) == str(engryArr[n]):
                score = score + 10  # 增加10分
        if score == 100:
            print("历史激活器被激活，历史序号", m, "left", "得分", score);
            # 上报此过滤器。
            hipp2.collect_features(str(m) + "_left_")
            return  # 如果找到历史中此过滤器的雷同值，则停止继续查找。

    # 存储数据 （示例：88_vertical7 = 2）
    for k in range(len(engryArr)):
        g.r.set(str(g.frame) + "_left_" + str(k), engryArr[k])
        #print(str(g.frame), "帧时，管道保存了一个新的记忆， key是", str(g.frame) + "_left_" + str(k), "数据是", engryArr[k],)



def collect_Right(image):
    Hi, Wi = image.shape
    interval = image.max() / 10  # 能量分为10个档次
    # print("interval" ,interval)
    engryArr = np.zeros(10)
    for i in range(Hi):
        for j in range(Wi):
            if image[i, j] > 0:  # 只统计有值的地方
                angleIndex = int(image[i, j] // interval) - 1  # 判断此能量属于哪个档次。
                if angleIndex < 0:  # 索引不可以为负数
                    angleIndex = 0
                temp = engryArr[angleIndex]
                temp = temp + 1
                engryArr[angleIndex] = temp
    print("向右能量分布", engryArr);

    old = int(g.frame) - 10000  # 检索之前的10000条数据
    if old < 0:
        old = 0

    # 进行辨别 (当前帧和之前的所有帧进行对比)
    for m in range(int(g.frame) - 1, old, -1):  # 遍历历史记忆(不包含此次记忆，所以-1)  但这样的话，会导致第0帧的记忆不会被运行到。因为只有 range(3-1,0,-1)时才会运行。也就是说在第二帧时会检查第一帧，第一帧时不会去检查第0帧。
        score = 0
        for n in range(10):
            # print("比较的是：",str(m) + "_vertical_" + str(n))
            # print("比较结果是：",self.r.get(str(m) + "_vertical_" + str(n)),"    ",engryArr[n])
            if g.r.get(str(m) + "_right_" + str(n)) == str(engryArr[n]):
                score = score + 10  # 增加10分
        if score == 100:
            print("历史激活器被激活，历史序号", m, "right", "得分", score);
            # 上报此过滤器。
            hipp2.collect_features(str(m) + "_right_")
            return  # 如果找到历史中此过滤器的雷同值，则停止继续查找。

    # 存储数据 （示例：88_vertical7 = 2）
    for k in range(len(engryArr)):
        g.r.set(str(g.frame) + "_right_" + str(k), engryArr[k])
        #print(str(g.frame), "帧时，管道保存了一个新的记忆， key是", str(g.frame) + "_right_" + str(k), "数据是", engryArr[k],)
