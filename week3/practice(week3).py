import sys
from gettext import translation

import cv2
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QWidget, QLineEdit, QVBoxLayout,
                               QHBoxLayout, QSizePolicy, QComboBox)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        # 이미지를 출력할 라벨 선언
        self.label = QLabel()
        # 라벨의 사이즈 고정
        self.label.setFixedSize(640, 480)
        # 라벨을 수평 레이아웃에 추가
        self.layout_hori = QHBoxLayout()
        self.layout_hori.addWidget(self.label)

        # 각 요소를 수직으로 배치하기 위한 수직 레이아웃 선언
        self.layout_vert = QVBoxLayout()
        self.layout_vert.addLayout(self.layout_hori)
        
        # 이미지 경로를 입력할 QEditLine 선언
        self.edit = QLineEdit("Write image path here")
        self.edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # 원본 이미지 출력을 위한 QPushButton 선언
        self.button1 = QPushButton("Load Image")
        self.button1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # 이진화 된 이미지 출력을 위한 QPushButton 출력
        self.button2 = QPushButton("Binary Img")
        self.button2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # 이미지 경로 입력과 원본 이미지 출력 버튼, 이진화 된 이미지 출력 버튼을 배치할 수평 레이아웃 선언 및 위젯 추가
        self.layout_hori2 = QHBoxLayout()
        self.layout_hori2.addWidget(self.edit)
        self.layout_hori2.addWidget(self.button1)
        self.layout_hori2.addWidget(self.button2)

        # 이미지 경로 입력과 원본 이미지 출력 버튼, 이진화 된 이미지 출력 버튼을 수직 레이아웃에 추가
        self.layout_vert.addLayout(self.layout_hori2)

        # QComboBox와 콤보박스 라벨, 각 아이템과 관련된 함수 실행을 위한 버튼을 배치할 수평 레이아웃 추가
        self.layout_hori3 = QHBoxLayout()

        # 콥보박스 라벨 선언
        self.combo_label = QLabel("Geometry type:")
        # 콤보 박스 선언 및 아이템 추가
        self.combobox = QComboBox()
        self.combobox.addItem("flip")
        self.combobox.addItem("translation")
        self.combobox.addItem("rotation")

        # 각 기능을 수행할 버튼 선언
        self.GeometryBtn = QPushButton("Geometry Image")

        # QComboBox와 콤보박스 라벨, 각 아이템과 관련된 함수 실행을 위한 버튼을 수평 레이아웃에 배치
        self.layout_hori3.addWidget(self.combo_label, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout_hori3.addWidget(self.combobox)
        self.layout_hori3.addWidget(self.GeometryBtn)

        # 수직 레이아웃에 추가
        self.layout_vert.addLayout(self.layout_hori3)

        widget = QWidget(self)
        widget.setLayout(self.layout_vert)
        self.setCentralWidget(widget)

        # 각 버튼에 함수들 연결
        self.button1.clicked.connect(self.loadImg)
        self.button2.clicked.connect(self.changeToGrayscale)
        self.GeometryBtn.clicked.connect(self.call_Geo)


    # 원본 이미지 출력 함수
    def loadImg(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        h, w, ch = img.shape

        img = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_img))

    # 이진 변환한 이미지 출력 함수
    def changeToGrayscale(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        _, dst = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

        h, w= dst.shape

        dst = QImage(dst.data, h, w, w, QImage.Format_Grayscale8)
        scaled_img = dst.scaled(640, 480, Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap.fromImage(scaled_img))

    # 이미지 반전을 수행하기 위한 함수
    def Geometry_flip(self):
        src = self.edit.text()
        ori_img = cv2.imread(src, cv2.IMREAD_COLOR)
        flip_img = cv2.flip(ori_img, 1)

        h, w, ch = flip_img.shape
        flip_img = QImage(flip_img.data, w, h, ch * w, QImage.Format_BGR888)
        scaled_flip_img = flip_img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_flip_img))

    # Translation 수행을 위한 함수
    def Geometry_translation(self):
        src = self.edit.text()
        ori_img = cv2.imread(src, cv2.IMREAD_COLOR)
        rows, cols = ori_img.shape[:2]
        Mat = np.float32([[1, 0, 50], [0, 1, 20]])
        translation_img = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_REFLECT)

        h, w, ch = translation_img.shape
        translation_img = QImage(translation_img.data, w, h, ch * w, QImage.Format_BGR888)
        scaled_flip_img = translation_img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_flip_img))

    # 이미지 회전을 위한 함수
    def Geometry_rotation(self):
        src = self.edit.text()
        ori_img = cv2.imread(src, cv2.IMREAD_COLOR)

        rows, cols = ori_img.shape[:2]
        Mat = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 1.0)

        rotaion_img = cv2.warpAffine(ori_img, Mat, (cols, rows), borderMode=cv2.BORDER_REPLICATE)

        h, w, ch = rotaion_img.shape
        rotaion_img = QImage(rotaion_img.data, w, h, ch * w, QImage.Format_BGR888)
        scaled_rotaion_img = rotaion_img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_rotaion_img))

    # 위에서 선언한 각 기하학적 변환을 콤보박스의 인덱스에 따라 호출하는 함수
    def call_Geo(self):
        if self.combobox.currentIndex() == 0:
            self.Geometry_flip()
        elif self.combobox.currentIndex() == 1:
            self.Geometry_translation()
        elif self.combobox.currentIndex() == 2:
            self.Geometry_rotation()

if __name__=='__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())