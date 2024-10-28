import cv2
if __name__ == '__main__':
    # 원본 이미지 출력
    ori_img = cv2.imread("./images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
    cv2.imshow('Original image', ori_img)

    # 이미지 회전을 위한 각 인자값 입력
    rows, cols = ori_img.shape[:2] # channel 여부 무시
    Mat1 = cv2.getRotationMatrix2D((0, 0), 45, 1.0)
    Mat2 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1.0)
    Mat3 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1.0)

    # (0,0) 45도로 회전
    r_image1 = cv2.warpAffine(ori_img, Mat1, (cols, rows))
    # (w/2, h/2)45도 회전, 경계 처리 = replicate
    r_image2 = cv2.warpAffine(ori_img, Mat2, (cols, rows), borderMode=cv2.BORDER_REPLICATE)
    # (w/2, h/2) 45도 회전, 경계 처리 = default
    r_image3 = cv2.warpAffine(ori_img, Mat2, (cols, rows), borderMode=cv2.BORDER_DEFAULT)
    # (w/2, h/2) 90도 회전
    r_image4 = cv2.warpAffine(ori_img, Mat3, (cols, rows))

    # 회전 시킨 각 이미지 출력
    cv2.imshow('Rotation image- (0, 0), 45)', r_image1)
    cv2.imshow('Rotation image- (w/2, h/2), 45 - replicate)', r_image2)
    cv2.imshow('Rotation image- (w/2, h/2), 45 - default)', r_image3)
    cv2.imshow('Rotation image- (w/2, h/2), 90', r_image4)
    cv2.waitKey(0)