import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Simple PyQt App with QLabel')
window.setGeometry(100, 100, 640, 480)

layout = QVBoxLayout()
window.setLayout(layout)

buttons = []

for i in range(10):
    button = QPushButton(f'QPushButton{i:02}!')
    buttons.append(button)
    layout.addWidget(button)

window.show()
sys.exit(app.exec())