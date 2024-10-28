import sys
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # 콤보박스 아이템의 내용과 인덱스 출력을 위한 QPushButton
        self.button = QPushButton("Print Combo Item")
        self.my_combo_box = QComboBox()
        # 콤보박스에 아이템 추가
        self.my_combo_box.addItem("Asnenal")
        self.my_combo_box.addItem("Manchester City")
        self.my_combo_box.addItem("Spurs")
        self.my_combo_box.addItem("Liverpool")

        # 버튼 클릭시 실행할 함수 연결
        self.button.clicked.connect(self.print_item)
        # 콤보 박스 연에 출력할 라벨 선언
        self.combo_label = QLabel("My list:")

        # 콤보박스 라벨과 콤보 박스를 수평 레이아웃으로 배치
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.combo_label)
        h_layout.addWidget(self.my_combo_box)

        # 위 수평 레이아웃과 QPushButton을 수직으로 배치
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.button)

        widget = QWidget(self)
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    # QPushButton에 연결해줄 함수 정읜
    def print_item(self):
        print(f"currentText: {self.my_combo_box.currentText()}")
        print(f"currentIndex: {self.my_combo_box.currentIndex()}")

if __name__ == '__main__':
    app = QApplication()
    w = Window()
    w.show()
    sys.exit(app.exec())
