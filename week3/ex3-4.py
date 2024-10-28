import cv2

if __name__ == '__main__':
    # 원본 이미지 불러오기
    ori_img = cv2.imread("../images/Lenna.jpg", cv2.IMREAD_UNCHANGED)

    # 상하 반전
    f_image0 = cv2.flip(ori_img, 0)
    # 좌우 반전
    f_image_p1 = cv2.flip(ori_img, 1)
    # 원점 대칭
    f_image_m1 = cv2.flip(ori_img, -1)

    # 원본 영상과 반전시킨 각 이미지 출력
    cv2.imshow('Original image', ori_img)
    cv2.imshow('Flip image (Up/Down, 0)', f_image0)
    cv2.imshow('Flip image (Left/Right, 1)', f_image_p1)
    cv2.imshow('Flip image (Y=X, -1)', f_image_m1)

    cv2.waitKey(0)