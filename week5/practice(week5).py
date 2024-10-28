import sys
from gettext import translation

import cv2
import numpy as np
from PySide6.QtCore import Qt, QLine
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QWidget, QLineEdit, QVBoxLayout,
                               QHBoxLayout, QSizePolicy, QComboBox, QGridLayout)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.count = 0
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
        self.edit = QLineEdit("../images/person_dark.jpg")
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


        
        # 원근 변환을 수행할 기준점의 좌표를 표시할 QEditLine 옆에 표시할 라벨 선언
        self.label_pos1 = QLabel("Pos1")
        self.label_pos2 = QLabel("Pos2")
        self.label_pos3 = QLabel("Pos3")
        self.label_pos4 = QLabel("Pos4")

        # 기준점의 좌표값을 표시할 QEditLine 선언
        self.Ledit_x1 = QLineEdit()
        self.Ledit_y1 = QLineEdit()
        self.Ledit_x2 = QLineEdit()
        self.Ledit_y2 = QLineEdit()
        self.Ledit_x3 = QLineEdit()
        self.Ledit_y3 = QLineEdit()
        self.Ledit_x4 = QLineEdit()
        self.Ledit_y4 = QLineEdit()

        # 원근 변환관 관련된 위젯을 그리드 레이아웃으로 배치
        pos_grid = QGridLayout()
        pos_grid.addWidget(self.label_pos1, 0, 0)
        pos_grid.addWidget(self.Ledit_x1, 0, 1)
        pos_grid.addWidget(self.Ledit_y1, 0, 2)
        pos_grid.addWidget(self.label_pos2, 0, 3)
        pos_grid.addWidget(self.Ledit_x2, 0, 4)
        pos_grid.addWidget(self.Ledit_y2, 0, 5)
        pos_grid.addWidget(self.label_pos3, 1, 0)
        pos_grid.addWidget(self.Ledit_x3, 1, 1)
        pos_grid.addWidget(self.Ledit_y3, 1, 2)
        pos_grid.addWidget(self.label_pos4, 1, 3)
        pos_grid.addWidget(self.Ledit_x4, 1, 4)
        pos_grid.addWidget(self.Ledit_y4, 1, 5)

        # 원본 이미지로 되돌리는 버튼
        self.initialize_btn = QPushButton("Initialize Pos")
        # 원근 변환을 수행할 버튼
        self.perspecive_btn = QPushButton("Perspective Image")

        # 그리드 레이아웃과 initialize_btn, perspectice_btn을 수평으로 배치
        self.layout_hori4 = QHBoxLayout()
        self.layout_hori4.addLayout(pos_grid)
        self.layout_hori4.addWidget(self.initialize_btn)
        self.layout_hori4.addWidget(self.perspecive_btn)

        #에지 발견을 수행할 콤보박스와 버튼 선언
        self.edgeLabel = QLabel("Filter Type", alignment=Qt.AlignmentFlag.AlignRight)
        
        self.edgecombo = QComboBox()
        self.edgecombo.addItem("Sobel_XY")
        self.edgecombo.addItem("Scharr_X")
        self.edgecombo.addItem("Scharr_Y")
        self.edgecombo.addItem("Laplacian")
        self.edgecombo.addItem("Canny")
        
        self.edgebtn = QPushButton("Edge Detection")
        
        #edgecombo와 라벨, 버튼을 수평 레이아웃에 추가
        self.layout_hori5 = QHBoxLayout()
        self.layout_hori5.addWidget(self.edgeLabel)
        self.layout_hori5.addWidget(self.edgecombo)
        self.layout_hori5.addWidget(self.edgebtn)


        # 수직 레이아웃에 추가
        self.layout_vert.addLayout(self.layout_hori3)
        self.layout_vert.addLayout(self.layout_hori4)
        self.layout_vert.addLayout(self.layout_hori5)

        widget = QWidget(self)
        widget.setLayout(self.layout_vert)
        self.setCentralWidget(widget)

        # 각 버튼에 함수 연결
        self.button1.clicked.connect(self.load_img_func)
        self.button2.clicked.connect(self.changeToBinary)
        self.GeometryBtn.clicked.connect(self.call_Geo)
        self.initialize_btn.clicked.connect(self.initialize)
        self.perspecive_btn.clicked.connect(self.perspective_image)
        self.edgebtn.clicked.connect(self.call_edgeFilter)


    # def loadImg(self):
    #     src = self.edit.text()
    #     img = cv2.imread(src, cv2.IMREAD_COLOR)
    #
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #
    #     h, w, ch = img.shape
    #
    #     img = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
    #     scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
    #
    #     self.label.setPixmap(QPixmap.fromImage(scaled_img))

    # 이미지의 이진화를 수행하는 함수
    def changeToBinary(self):
        self.m_proc_img = cv2.cvtColor(self.m_proc_img, cv2.COLOR_BGR2GRAY)
        _, self.m_proc_img = cv2.threshold(self.m_proc_img, 110, 255, cv2.THRESH_BINARY)

        # print(len(self.m_proc_img.shape))
        self.update_img(self.m_proc_img)

    # 이미지 반전을 수행하는 함수
    def Geometry_flip(self):
        src = self.edit.text()
        ori_img = cv2.imread(src, cv2.IMREAD_COLOR)
        self.m_proc_img = cv2.flip(self.m_proc_img, 1)

        self.update_img(self.m_proc_img)

    # 이미지 Translation을 수행하는 함수
    def Geometry_translation(self):
        rows, cols = self.m_proc_img.shape[:2]
        Mat = np.float32([[1, 0, 50], [0, 1, 20]])
        self.m_proc_img = cv2.warpAffine(self.m_proc_img, Mat, (cols, rows), borderMode=cv2.BORDER_REFLECT)

        self.update_img(self.m_proc_img)

    # 이미지 회전을 수행하는 함수
    def Geometry_rotation(self):
        rows, cols = self.m_proc_img.shape[:2]
        Mat = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 1.0)

        self.m_proc_img = cv2.warpAffine(self.m_proc_img, Mat, (cols, rows), borderMode=cv2.BORDER_REPLICATE)

        self.update_img(self.m_proc_img)

    # 각 기하학적 변환을 conbobox의 인덱스에 따라 호출하는 함수
    def call_Geo(self):
        if self.combobox.currentIndex() == 0:
            self.Geometry_flip()
        elif self.combobox.currentIndex() == 1:
            self.Geometry_translation()
        elif self.combobox.currentIndex() == 2:
            self.Geometry_rotation()
        
    # 이미지 포멧(컬러, 흑백)에 따라 이미지를 출력하는 함수
    def update_img(self, img):
        if len(img.shape) < 3:
            h, w = img.shape
            ch = 1
            img_format = QImage.Format_Grayscale8
        else:
            h, w, ch = img.shape
            img_format = QImage.Format_RGB888
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = QImage(img.data, w, h, ch * w, img_format)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap.fromImage(scaled_img))

    # 원본 이미지를 m_main_img에 저장하고 각 변환을 수행할 m_proc_img에 복사하는 함수
    def load_img_func(self):
        self.m_main_img = cv2.imread(f"{self.edit.text()}", cv2.IMREAD_COLOR)
        self.m_main_img = cv2.resize(self.m_main_img, (640, 480))
        self.m_proc_img = self.m_main_img.copy()
        self.update_img(self.m_proc_img)

    # 원근 변환을 초기화 하는 함수
    def initialize(self):
        self.Ledit_x1.setText("")
        self.Ledit_y1.setText("")
        self.Ledit_x2.setText("")
        self.Ledit_y2.setText("")
        self.Ledit_x3.setText("")
        self.Ledit_y3.setText("")
        self.Ledit_x4.setText("")
        self.Ledit_y4.setText("")

        self.m_proc_img = self.m_main_img.copy()
        self.update_img(self.m_proc_img)

    # 마우스를 클릭한 지점의 좌표를 저장하고 해당 좌표에 점을 추가하는 함수
    def mousePressEvent(self, event):
        x = event.position().x() - self.label.x()
        y = event.position().y() - self.label.y()
        x, y = int(x), int(y)

        if  self.count == 0:
            self.Ledit_x1.setText(f"{x}")
            self.Ledit_y1.setText(f"{y}")
            self.count += 1
            cv2.circle(self.m_proc_img, (x, y), 5, (255, 0, 0), -1)

        elif self.count == 1:
            self.Ledit_x2.setText(f"{x}")
            self.Ledit_y2.setText(f"{y}")
            self.count += 1
            cv2.circle(self.m_proc_img, (x, y), 5, (0, 255, 0), -1)

        elif self.count == 2:
            self.Ledit_x3.setText(f"{x}")
            self.Ledit_y3.setText(f"{y}")
            self.count += 1
            cv2.circle(self.m_proc_img, (x, y), 5, (0, 0, 255), -1)

        elif self.count == 3:
            self.Ledit_x4.setText(f"{x}")
            self.Ledit_y4.setText(f"{y}")
            self.count = 0
            cv2.circle(self.m_proc_img, (x, y), 5, (0, 255, 255), -1)

        self.update_img(self.m_proc_img)

    # 각 기준점에 대한 원근 변환을 수행하는 함수
    def perspective_image(self):
        rows, cols = self.m_proc_img.shape[:2]
        x1 = self.Ledit_x1.text()
        y1 = self.Ledit_y1.text()
        x2 = self.Ledit_x2.text()
        y2 = self.Ledit_y2.text()
        x3 = self.Ledit_x3.text()
        y3 = self.Ledit_y3.text()
        x4 = self.Ledit_x4.text()
        y4 = self.Ledit_y4.text()

        pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        pts2 = np.float32([[0, 0], [cols-1, 0], [cols - 1, rows - 1], [0, rows - 1]])
        Mat1 = cv2.getPerspectiveTransform(pts1, pts2)
        self.m_proc_img = cv2.warpPerspective(self.m_proc_img, Mat1, (cols, rows))

        self.update_img(self.m_proc_img)

    #에지 검출 함수를 출력하는 함수
    def call_edgeFilter(self):
        value = self.m_proc_img.shape
        img = self.m_proc_img.copy()
        if len(value) >= 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if self.edgecombo.currentIndex() == 0:
            self.Sobel_XY(img)
        elif self.edgecombo.currentIndex() == 1:
            self.Scharr_X(img)
        elif self.edgecombo.currentIndex() == 2:
            self.Scharr_Y(img)
        elif self.edgecombo.currentIndex() == 3:
            self.Laplacian(img)
        elif self.edgecombo.currentIndex() == 4:
            self.Canny(img)

    #sobel 필터
    def Sobel_XY(self, img):
        s_imageXY = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize = 3)
        self.update_img(s_imageXY)

    #x축 방향의 Scharr 필터
    def Scharr_X(self, img):
        s_imageX = cv2.Scharr(img, cv2.CV_8U, 1, 0)
        self.update_img(s_imageX)

    #y축 방향의 Scharr 필터
    def Scharr_Y(self, img):
        s_imageY = cv2.Scharr(img, cv2.CV_8U, 0, 1)
        self.update_img(s_imageY)

    #Laplacian 필터
    def Laplacian(self, img):
        l_image = cv2.Laplacian(img, cv2.CV_8U, ksize=3)
        self.update_img(l_image)

    #Canny 필터
    def Canny(self,img):
        c_image = cv2.Canny(img, 150, 300)
        self.update_img(c_image)

if __name__=='__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())