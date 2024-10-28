import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QWidget, QVBoxLayout, QMainWindow)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        #명령을 입력창 선언
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")

        # 입력창을 레이아웃에 삽입
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 버튼 클릭시 작동할 함수 연결
        self.button.clicked.connect(self.greetings)

    # 작동할 함수 선언
    def greetings(self):
        print(f"Hello {self.edit.text()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())