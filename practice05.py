import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PyQt App with QLabel')
        self.setGeometry(100, 100, 640, 480)
        self.label = QLabel('Hello, PyQt!', self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())