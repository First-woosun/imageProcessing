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
        self.label = QLabel()
        self.label.setFixedSize(640, 480)
        self.layout_hori = QHBoxLayout()
        self.layout_hori.addWidget(self.label)

        self.layout_vert = QVBoxLayout()
        self.layout_vert.addLayout(self.layout_hori)

        self.edit = QLineEdit("Write image path here")
        self.edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.button1 = QPushButton("Load Image")
        self.button1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.button2 = QPushButton("Binary Img")
        self.button2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.layout_hori2 = QHBoxLayout()
        self.layout_hori2.addWidget(self.edit)
        self.layout_hori2.addWidget(self.button1)
        self.layout_hori2.addWidget(self.button2)

        self.layout_vert.addLayout(self.layout_hori2)

        self.layout_hori3 = QHBoxLayout()

        self.combo_label = QLabel("Geometry type:")
        self.combobox = QComboBox()
        self.combobox.addItem("flip")
        self.combobox.addItem("translation")
        self.combobox.addItem("rotation")

        self.GeometryBtn = QPushButton("Geometry Image")

        self.layout_hori3.addWidget(self.combo_label, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout_hori3.addWidget(self.combobox)
        self.layout_hori3.addWidget(self.GeometryBtn)
        self.layout_vert.addLayout(self.layout_hori3)

        widget = QWidget(self)
        widget.setLayout(self.layout_vert)
        self.setCentralWidget(widget)

        self.button1.clicked.connect(self.loadImg)
        self.button2.clicked.connect(self.changeToGrayscale)
        self.GeometryBtn.clicked.connect(self.call_Geo)


    def loadImg(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        h, w, ch = img.shape

        img = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_img))

    def changeToGrayscale(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        _, dst = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

        h, w= dst.shape

        dst = QImage(dst.data, h, w, w, QImage.Format_Grayscale8)
        scaled_img = dst.scaled(640, 480, Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap.fromImage(scaled_img))

    def Geometry_flip(self):
        src = self.edit.text()
        ori_img = cv2.imread(src, cv2.IMREAD_COLOR)
        flip_img = cv2.flip(ori_img, 1)

        h, w, ch = flip_img.shape
        flip_img = QImage(flip_img.data, w, h, ch * w, QImage.Format_BGR888)
        scaled_flip_img = flip_img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_flip_img))

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