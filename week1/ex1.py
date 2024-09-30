import cv2

# if __name__ == '__main__':
#     img = cv2.imread("./images/Lenna.jpg", cv2.IMREAD_GRAYSCALE)
#     cv2.imshow("Image", img)
#     cv2.imwrite('Lena_1.bmp', img)
#     cv2.imwrite('Lena_2.jpg', img)
#     cv2.waitKey(0)

#---------------------------------------------------------------------------------

# if __name__ == '__main__':
#     #color Image
#     img = cv2.imread("./images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
#     height, width, channel = img.shape
#     print("height: {}, width: {}, channel: {}" .format(height, width, channel))
#
#     #gray Image
#     img = cv2.imread("./Lena_2.jpg", cv2.IMREAD_UNCHANGED)
#     height, width = img.shape
#     print("height: {}, width: {}".format(height, width))

#----------------------------------------------------------------------------------

# img = cv2.imread("./images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow('image', img)
#
# #cv2.waitkey(1000)
# key = cv2.waitKey(0)
# print("key = {0} ({1})" .format(key, chr(key)))

#----------------------------------------------------------------------------------

src = cv2.imread("../Lena_2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

_, dst = cv2.threshold(src, 160, 255, cv2.THRESH_BINARY)
cv2.imshow('dst', dst)
cv2.waitKey(0)