import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Form Layout Example')

layout = QFormLayout()
window.setLayout(layout)

label1 = QLabel('Label 1:')
edit1 = QLineEdit()
layout.addRow(label1, edit1)

label2 = QLabel('Label 2:')
edit2 = QLineEdit()
layout.addRow(label2, edit2)

label3 = QLabel('Label 3:')
edit3 = QLineEdit()
layout.addRow(label3, edit3)

window.show()
sys.exit(app.exec())
