import sys

import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QWidget, QLineEdit, QVBoxLayout,
                               QHBoxLayout, QSizePolicy)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        self.label = QLabel("Image here")
        self.label.setFixedSize(640, 480)
        self.layout_vert = QVBoxLayout()
        self.layout_vert.addWidget(self.label)

        self.edit = QLineEdit("Write image path here")
        self.edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.button = QPushButton("Load Image")
        self.button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.layout_hori = QHBoxLayout()
        self.layout_hori.addWidget(self.edit)
        self.layout_hori.addWidget(self.button)

        self.layout_vert.addLayout(self.layout_hori)

        widget = QWidget(self)
        widget.setLayout(self.layout_vert)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.imageup)

    def imageup(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        h, w, ch = img.shape

        img = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap.fromImage(scaled_img))
        print("update image")



if __name__=='__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())