import numpy as np
import cv2

# 원본(흑백) 이미지 저장
ori_image = cv2.imread("../Lena_2.jpg", cv2.IMREAD_UNCHANGED)
c_image = cv2.cvtColor(ori_image, cv2.COLOR_GRAY2BGR)
# 원본 이미지 출력
cv2.imshow('Original image', c_image)

# 이미지의 데이터 저장
rows, cols = ori_image.shape[:2]

# 변환 기준점 지정
pts1 = np.float32([[200, 200], [300, 200], [200, 300]])

# 변환 기준점을 점으로 표시
cv2.circle(c_image, (200, 200), 9, (255, 0, 0), -1)
cv2.circle(c_image, (300, 200), 9, (0, 255, 0), -1)
cv2.circle(c_image, (200, 200), 9, (0, 0, 255), -1)

# 변환 기준점 지정
pts2 = np.float32 ([[200, 200], [350, 200], [200, 250]])
# 이미지 변환(1)
Mat1 = cv2.getAffineTransform(pts1, pts2)
r_image1 = cv2.warpAffine(c_image, Mat1, (cols, rows))

# 변환 기준점 지정
pts2 = np.float32([[200, 200], [300, 230], [260, 300]])
# 이미지 변환(2)
Mat2 = cv2.getAffineTransform(pts1, pts2)
r_image2 = cv2.warpAffine(c_image, Mat2, (cols, rows))

# 변환 기준점 지정
pts2 = np.float32([[200,200], [100, 170], [170, 100]])
# 이미지 변환(3)
Mat3 = cv2.getAffineTransform(pts1, pts2)
r_image3 = cv2.warpAffine(c_image, Mat3, (cols, rows))

# 변환된 각 이미지 출력
cv2.imshow('Affine 1 image', r_image1)
cv2.imshow('Affine 2 image', r_image2)
cv2.imshow('Affine 3 image', r_image3)

cv2.waitKey(0)