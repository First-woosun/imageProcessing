import sys
import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import  QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # 이미지를 띄울 라벨 초기화
        self.label = QLabel("Image here")
        self.label.setFixedSize(640, 480)
        self.setCentralWidget(self.label)

        # ../images/Lenna.jpg 경로의 이미지 저장 및 데이터 저장
        img = cv2.imread(f'../images/Lenna.jpg', cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        h, w,ch = img.shape

        img = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

        # 저장한 이미지를 라벨에 띄우기
        self.label.setPixmap(QPixmap.fromImage(scaled_img))
        print("update image")

if __name__ == '__main__':
    app = QApplication()
    w = Window()
    w.show()
    sys.exit(app.exec())