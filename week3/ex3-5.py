import sys
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Print Combo Item")
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItem("Asnenal")
        self.my_combo_box.addItem("Manchester City")
        self.my_combo_box.addItem("Spurs")
        self.my_combo_box.addItem("Liverpool")

        self.button.clicked.connect(self.print_item)
        self.combo_label = QLabel("My list:")

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.combo_label)
        h_layout.addWidget(self.my_combo_box)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.button)

        widget = QWidget(self)
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    def print_item(self):
        print(f"currentText: {self.my_combo_box.currentText()}")
        print(f"currentIndex: {self.my_combo_box.currentIndex()}")

if __name__ == '__main__':
    app = QApplication()
    w = Window()
    w.show()
    sys.exit(app.exec())
