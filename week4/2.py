import numpy as np
import cv2

if __name__=='__main__':
    ori_img = cv2.imread('../images/Lenna.jpg', cv2.IMREAD_COLOR)
    rows, cols = ori_img.shape[:2]

    #pts1좌표 표시
    pts1 = np.float32([[80, 280], [220, 220], [250, 480], [60, 420]])

    # 원근 변환을 수행할 기준점 표시
    cv2.circle(ori_img, (80, 280), 9, (255, 0, 0), -1)
    cv2.circle(ori_img, (220, 220),9, (0, 255, 0), -1)
    cv2.circle(ori_img, (250, 480),9, (0, 0, 255), -1)
    cv2.circle(ori_img, (60, 420), 9, (0, 255, 255), -1)

    # 원근 변환시 평행선이 유지되지 않음을 확인하기 위한 선 2개 추가
    cv2.line(ori_img, (0, 340), (511, 340), (255, 0, 0), 2)
    cv2.line(ori_img, (0, 380), (511, 380), (0, 0, 255), 2)

    # pts2 좌표 표시
    pts2 = np.float32([[10, 10], [502, 10], [502, 502], [10, 502]])
    # 좌표값을 기준으로 원근 변환 수핼
    Mat1 = cv2.getPerspectiveTransform(pts1, pts2)

    print('Perspective matrix')
    print(Mat1)

    # 원본 이미지화 원근 변환 이미지 출력
    r_image = cv2.warpPerspective(ori_img, Mat1, (cols, rows))
    cv2.imshow('Original image', ori_img)
    cv2.imshow('Perspective image', r_image)

    cv2.waitKey(0)