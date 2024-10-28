import sys

import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QWidget, QLineEdit, QVBoxLayout,
                               QHBoxLayout, QSizePolicy)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        self.label = QLabel("Image1 here")
        self.label.setFixedSize(640, 480)
        self.layout_hori = QHBoxLayout()
        self.layout_hori.addWidget(self.label)

        self.layout_vert = QVBoxLayout()
        self.layout_vert.addLayout(self.layout_hori)

        # 출력할 이미지의 path를 입력할 QEditLine 선언
        self.edit = QLineEdit("Write image path here")
        self.edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # 이미지를 컬러로 출력하기 위한 QPushButton 선언
        self.button1 = QPushButton("Color Image")
        self.button1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # 이미지를 이진화 해서 출력하기 위한 QPushButton 선언
        self.button2 = QPushButton("Binary Img")
        self.button2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # 수평 레이아웃에 위 3개를 추가
        self.layout_hori2 = QHBoxLayout()
        self.layout_hori2.addWidget(self.edit)
        self.layout_hori2.addWidget(self.button1)
        self.layout_hori2.addWidget(self.button2)

        # 이미지를 출력할 라벨과 수직으로 배치
        self.layout_vert.addLayout(self.layout_hori2)

        widget = QWidget(self)
        widget.setLayout(self.layout_vert)
        self.setCentralWidget(widget)

        # 각 버튼을 클릭하면 작동 할 함수를 연결
        self.button1.clicked.connect(self.Imageup)
        self.button2.clicked.connect(self.changeToGrayscale)


    # 컬러 이미지 출력 함수
    def Imageup(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        h, w, ch = img.shape

        img = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_img))

    # 이진화된 이미지를 출력하는 함수
    def changeToGrayscale(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        _, dst = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

        h, w= dst.shape

        dst = QImage(dst.data, h, w, w, QImage.Format_Grayscale8)
        scaled_img = dst.scaled(640, 480, Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap.fromImage(scaled_img))


if __name__=='__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())