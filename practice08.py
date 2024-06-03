import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QDialog

def on_button_clicked():
    dialog = QDialog(window)
    dialog.setModal(True)
    dialog.resize(300, 200)
    dialog.show()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Simple PyQt App with QLabel')
window.setGeometry(100, 100, 640, 480) 
button = QPushButton('Hello, PyQt!', window)
button.clicked.connect(on_button_clicked)
window.show()
sys.exit(app.exec())