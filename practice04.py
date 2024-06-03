import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Simple PyQt App with QLabel')
window.setGeometry(0, 0, 640, 480)
label = QLabel('Hello, PyQt!', window)
window.show()
sys.exit(app.exec())
