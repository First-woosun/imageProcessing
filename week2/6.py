import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QLineEdit, QPushButton, QVBoxLayout)
from PySide6.QtGui import QImage, QPixmap
import cv2

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        # 이미지의 path를 입력할 QEditLine 선언
        self.edit = QLineEdit("Write image path here")
        self.button = QPushButton("Load Image")

        # 위젯을 레이아웃에 추가
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 버튼 클릭시 작동할 함수 연결
        self.button.clicked.connect(self.imageup)
    
    # 버튼 클릭시 작동할 함수
    def imageup(self):
        src = self.edit.text()
        img = cv2.imread(src, cv2.IMREAD_COLOR)
        cv2.imshow('img', img)

if __name__=='__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())