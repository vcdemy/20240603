import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Simple PyQt App with QLabel')
window.setGeometry(100, 100, 640, 480)

layout = QVBoxLayout()
window.setLayout(layout)

label = QLabel('Hello, QLabel!')
button = QPushButton('Hello, QPushButton!')

layout.addWidget(label)
layout.addWidget(button)

window.show()
sys.exit(app.exec())