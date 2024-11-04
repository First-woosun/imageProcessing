import cv2
capture = cv2.VideoCapture(0)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('Framewidth; {}, height {}'.format(width, height))
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
while cv2.waitKey(32) < 0:
    ret, frame = capture.read()
    if not ret:  # ret== False:
        break
    cv2.imshow("Frame", frame)
capture.release()
