import cv2

if __name__ == '__main__':
    #레스터 그래픽 영상 파일 형식을 메모리로 읽어오는 imread()함수
    #첫 번째 인자인 filename 은 상대 경로 또는 절대 경로를 통해  읽어들일 영상을 선택한다.
    #두 번째 인자는 flags로 영상파일을 읽어올 옵션을 지정한다.(사이즈 조절, 컬러, 그레이스케일...)ㄴ
    img = cv2.imread("../headphone.jpg", cv2.IMREAD_GRAYSCALE)

    #영상을 지정한 윈도우에 출력하는 imshow()함수
    #첫 번째 인자인 winname은 이미지를 출력할 윈도우를 지정한다. 이 때 일치하는 윈도우가 없다면 새로운 윈도우를 생성한다.
    cv2.imshow("Image", img)
    
    #영상을 저장하는 imwrite()함수
    #첫 번째 인자는 저장할 파일의 경로와 파일의 확장자를 지정한다.
    #두 번쨰 인자는 저장할 영상 데이터를 지정한다.
    #세 번째 인자는 flag가 있는데 영상 파일을 저장할 때 옵션을 지정할 수 있다.
    cv2.imwrite('Lena_1.bmp', img)
    cv2.imwrite('Lena_2.jpg', img)

    #지정한 시간동안 사용자가 키를 입력할 때까지 프로그램을 대기시키는 waitkey() 함수이다.
    #대기할 시간을 인자로 받는대 0보다 작거나 같은 경우 무한 대기에 들어간다.
    cv2.waitKey(0)

#---------------------------------------------------------------------------------

# if __name__ == '__main__':
#     #color Image
#     img = cv2.imread("./images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
#     height, width, channel = img.shape
#     print("height: {}, width: {}, channel: {}" .format(height, width, channel))
#
#     #gray Image
#     img = cv2.imread("./Lena_2.jpg", cv2.IMREAD_UNCHANGED)
#     height, width = img.shape
#     print("height: {}, width: {}".format(height, width))

#----------------------------------------------------------------------------------

# img = cv2.imread("./images/Lenna.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow('image', img)
#
# #cv2.waitkey(1000)
# key = cv2.waitKey(0)
# print("key = {0} ({1})" .format(key, chr(key)))

#----------------------------------------------------------------------------------

# src = cv2.imread("../Lena_2.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow('src', src)
#
# _, dst = cv2.threshold(src, 160, 255, cv2.THRESH_BINARY)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)