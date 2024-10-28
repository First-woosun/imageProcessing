import cv2

if __name__=='__main__':
    ori_img = cv2.imread("../images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
    # 원본 이미지 출력
    cv2.imshow("Original image", ori_img)

    # 원본 이미지를 축소해서 출력
    rs_img = cv2.resize(ori_img, (64, 64), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("128x64 image", rs_img)

    # 최소 근접 보간
    z_img1 = cv2.resize(rs_img, (512, 512), interpolation=cv2.INTER_NEAREST)
    # 양방향 선형 보간
    z_img2 = cv2.resize(rs_img, None, fx=8, fy=8, interpolation=cv2.INTER_LINEAR)
    # 양방향 큐빅 보간
    z_img3 = cv2.resize(rs_img, None, fx=8, fy=8, interpolation=cv2.INTER_CUBIC)
    # 픽셀 셈플링 보간
    z_img4 = cv2.resize(rs_img, None, fx=8, fy=8, interpolation=cv2.INTER_AREA)

    # 보간 기법이 적용된 각 이미지 출력
    cv2.imshow("Nearest neighbor intp image", z_img1)
    cv2.imshow("Bilinear intp image", z_img2)
    cv2.imshow("Cubic intp image", z_img3)
    cv2.imshow("Area intp image", z_img4)

    cv2.waitKey(0)