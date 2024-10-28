import cv2
img = cv2.imread('./images/person_dark.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)

s_imageX = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
s_imageY = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
s_imageXY = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=3)

cv2.imshow('Original image', img)
cv2.imshow('SobelXdirectionimage', s_imageX)
cv2.imshow('SobelYdirectionimage', s_imageY)
cv2.imshow('SobelX-Y directionimage', s_imageXY)

cv2.waitKey(0)
