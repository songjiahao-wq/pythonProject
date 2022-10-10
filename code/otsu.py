import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def rgb2gray(rgb):
    # 将rgb转灰度
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


#    return 0.2989 * image[:,:,0] + 0.5870*image[:,:,1] + 0.1140*image[:,:,2]

image = img.imread('my.jpg')
gray = rgb2gray(image)
h, x = np.histogram(gray.ravel(), bins=256)

plt.imshow(gray, cmap=plt.get_cmap('gray'))  # 显示灰度图
plt.show()

# 整体均值
meanall = np.sum(np.dot(h, np.array([n for n in range(256)])))
meanall = meanall / np.sum(np.array([n for n in range(256)]))
maxscore = 0;
gi = []
for i in range(1, 255):
    # 分割图像的均值只需要将直方图的高度乘以x坐标求和，再除以x坐标之和
    mean1 = np.sum(np.dot(h[0:i], np.array([n for n in range(i)])))
    mean1 = mean1 / np.sum(h[0:i])
    mean2 = np.sum(np.dot(h[i:256], np.array([n for n in range(i, 256)])))
    mean2 = mean2 / np.sum(h[i:256])
    # 公式计算
    score = sum(h[0:i]) * ((meanall - mean1) ** 2) + sum(h[i:256]) * ((meanall - mean2) ** 2)

    #    用于绘图
    gi.append(score)
    if maxscore < score:  # 记录最大值
        maxscore = score
        threshold = i

# print("max value = %d, th = %d" % (maxg, threshold))

# 用于绘图
gi.append(min(gi))
gi.insert(0, min(gi))
plot1 = plt.figure()
# 绘制直方图
plt.bar(np.array([n for n in range(256)]), h)
# 绘制分割点
plt.axvline(threshold, color='r')
# 绘制类间方差遍历过程示意图
plt.scatter([n for n in range(256)], (gi - min(gi)) / (max(gi) - min(gi)) * max(h))
plt.show()
