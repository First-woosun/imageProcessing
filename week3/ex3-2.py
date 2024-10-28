import numpy as np
import cv2

if __name__ == '__main__':
    # 원본 이미지 출력
    ori_img = cv2.imread("../images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
    cv2.imshow('Original image', ori_img)

    # Translation을 위한 인자들
    rows, cols = ori_img.shape[:2]
    Mat = np.float32([[1, 0, 30], [0, 1, 60]])

    # Default
    t_image1 = cv2.warpAffine(ori_img, Mat, (cols, rows))
    # boder_constant
    t_image2 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    # replicate
    t_image3 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_REPLICATE)
    # reflect
    t_image4 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_REFLECT)
    # wrap
    t_image5 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_WRAP)

    # 이동 시킨 각 이미지 출력
    cv2.imshow('Transformation image - default', t_image1)
    cv2.imshow('Transformation image - BORDER_CONSTANT', t_image2)
    cv2.imshow('Transformation image - BORDER_REPLICATE', t_image3)
    cv2.imshow('Transformation image - BORDER_REFLECT', t_image4)
    cv2.imshow('Transformation image - BORDER_WRAP', t_image5)
    cv2.waitKey(0)
