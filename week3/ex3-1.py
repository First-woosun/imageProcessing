import cv2

if __name__=='__main__':
    ori_img = cv2.imread("../images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original image", ori_img)

    rs_img = cv2.resize(ori_img, (64, 64), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("128x64 image", rs_img)

    z_img1 = cv2.resize(rs_img, (512, 512), interpolation=cv2.INTER_NEAREST)
    z_img2 = cv2.resize(rs_img, None, fx=8, fy=8, interpolation=cv2.INTER_LINEAR)
    z_img3 = cv2.resize(rs_img, None, fx=8, fy=8, interpolation=cv2.INTER_CUBIC)
    z_img4 = cv2.resize(rs_img, None, fx=8, fy=8, interpolation=cv2.INTER_AREA)

    cv2.imshow("Nearest neighbor intp image", z_img1)
    cv2.imshow("Bilinear intp image", z_img2)
    cv2.imshow("Cubic intp image", z_img3)
    cv2.imshow("Area intp image", z_img4)

    cv2.waitKey(0)