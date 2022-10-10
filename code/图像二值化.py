import cv2

img = cv2.imread('q2.jpg')
# 转为灰度图
new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = new_img.shape[0:2]

# 设置阈值
thresh = 10

# 遍历每一个像素点
for row in range(height):
    for col in range(width):
        # 获取到灰度值
        gray = new_img[row, col]
        # 如果灰度值高于阈值 就等于255最大值
        print(gray)
        if gray > thresh:
            new_img[row, col] = 255
        # 如果小于阈值，就直接改为0
        elif gray < thresh:
            new_img[row, col] = 5

cv2.imshow('img', new_img)
cv2.waitKey()
