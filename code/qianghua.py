# import cv2
#
# # Read the original image
# img = cv2.imread('q.jpg',flags=0)
# # Blur the image for better edge detection
# img_blur = cv2.GaussianBlur(img,(3,3), sigmaX=0, sigmaY=0)
# import imutils
# img_blur = imutils.resize(img_blur,width=720)
# # Sobel Edge Detection
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
#
# # Canny Edge Detection
# edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
#
# # Display Canny Edge Detection Image
# cv2.imshow('Canny Edge Detection', edges)
# cv2.waitKey(0)
#
# # Display Sobel Edge Detection Images
# cv2.imshow('Sobel X', sobelx)
#
# cv2.imshow('Sobel Y', sobely)
#
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)
# 导入相关包
import cv2
import numpy as np

# 读取图片
img = cv2.imread('q.jpg')

# cv2.imshow('lena', img)
# cv2.waitKey(0)  # 持续函数
print(img)
q = img
with open('q.txt', 'w') as f:
    f.write(str(q))
height = img.shape[0]
width = img.shape[1]

negative_file = np.zeros((height, width, 3))

# BGR图像拆分为3通道
b, g, r = cv2.split(img)
r = 255 - r
b = 255 - b
g = 255 - g

negative_file[:, :, 0] = b
negative_file[:, :, 1] = g
negative_file[:, :, 2] = r
print('**************************')
print(negative_file)
cv2.imwrite("negative_file.jpg", negative_file)
