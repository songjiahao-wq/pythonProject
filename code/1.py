# 导入相关包
import cv2
import numpy as np
from matplotlib import pyplot as plt
# %matplotlib inline
filename = 'my.jpg'
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img.shape) # 输出通道数，大小是350*350 3通道
# plt.imshow(img)
# plt.show()

class Brightness:
    def __init__(self, brightness_factor):
        self.brightness_factor = brightness_factor

    def __call__(self, img):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 通过cv2.cvtColor把图像从BGR转换到HSV
        darker_hsv = img_hsv.copy()
        darker_hsv[:, :, 2] = self.brightness_factor * darker_hsv[:, :, 2]
        return cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)


brightness = Brightness(1.0)
img2 = brightness(img)
plt.imshow(img2)

brightness = Brightness(5.0)
img3 = brightness(img)
plt.imshow(img3)
plt.show()