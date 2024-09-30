import cv2

if __name__ == '__main__':
    ori_img = cv2.imread("../images/Lenna.jpg", cv2.IMREAD_UNCHANGED)

    f_image0 = cv2.flip(ori_img, 0)
    f_image_p1 = cv2.flip(ori_img, 1)
    f_image_m1 = cv2.flip(ori_img, -1)

    cv2.imshow('Original image', ori_img)
    cv2.imshow('Flip image (Up/Down, 0)', f_image0)
    cv2.imshow('Flip image (Left/Right, 1)', f_image_p1)
    cv2.imshow('Flip image (Y=X, -1)', f_image_m1)

    cv2.waitKey(0)