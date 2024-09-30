import cv2
#
# origin = cv2.imread("./images/person_light.jpg", cv2.IMREAD_UNCHANGED)
#
# img = cv2.imread("./images/person_light.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cv2.imwrite('person_gray.jpg', img)


src1 = cv2.imread("./person_gray.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
_, dst1 = cv2.threshold(src1, 110, 255, cv2.THRESH_BINARY)
cv2.imshow('dst1', dst1)

src2 = cv2.imread("./images/person_dark.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
_, dst2 = cv2.threshold(src2, 110, 255, cv2.THRESH_BINARY)
cv2.imshow('dst2', dst2)

src3 = cv2.imread("./images/person_dark.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
_, dst3 = cv2.threshold(src3, 110, 255, cv2.THRESH_TOZERO)
cv2.imshow('dst3', dst3)

cv2.waitKey(0)