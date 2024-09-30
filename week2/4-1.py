import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.setGeometry(0, 0, 800, 500)

if __name__ == '__main__':
    #Create the Qt Application
    app =QApplication(sys.argv)

    #Create and show the form
    form = Form()
    form.show()

    #Run the main Qt loop
    sys.exit(app.exec())