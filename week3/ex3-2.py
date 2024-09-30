import numpy as np
import cv2

if __name__ == '__main__':
    ori_img = cv2.imread("../images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
    cv2.imshow('Original image', ori_img)
    rows, cols = ori_img.shape[:2]
    Mat = np.float32([[1, 0, 30], [0, 1, 60]])

    t_image1 = cv2.warpAffine(ori_img, Mat, (cols, rows))
    t_image2 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    t_image3 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_REPLICATE)
    t_image4 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_REFLECT)
    t_image5 = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_WRAP)

    cv2.imshow('Transformation image - default', t_image1)
    cv2.imshow('Transformation image - BORDER_CONSTANT', t_image2)
    cv2.imshow('Transformation image - BORDER_REPLICATE', t_image3)
    cv2.imshow('Transformation image - BORDER_REFLECT', t_image4)
    cv2.imshow('Transformation image - BORDER_WRAP', t_image5)
    cv2.waitKey(0)
