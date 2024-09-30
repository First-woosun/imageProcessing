import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button1.clicked.connect(self.button1_slot)
        self.button2.clicked.connect(self.button2_slot)
        self.button3.clicked.connect(self.button3_slot)

    def button1_slot(self):
        print(f"Button1")

    def button2_slot(self):
        print(f"Button2")

    def button3_slot(self):
        print(f"Button3")

if __name__ == '__main__':
    #Create the Qt Application
    app =QApplication(sys.argv)

    #Create and show the form
    form = Form()
    form.show()

    #Run the main Qt loop
    sys.exit(app.exec())