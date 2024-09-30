import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton

def say_hello():
    print("Button Clicked, Hello!")

app = QApplication(sys.argv)

button = QPushButton("Click me")

button.clicked.connect(say_hello)

button.show()

app.exec()