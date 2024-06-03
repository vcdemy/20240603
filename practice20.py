import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton

def on_radio_button_toggled():
    radio_button = app.sender()
    if radio_button.isChecked():
        print(f'Selected option: {radio_button.text()}')

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Radio Button Example')
window.setGeometry(100, 100, 300, 200)

layout = QVBoxLayout(window)

radio_button1 = QRadioButton('Option 1')
radio_button2 = QRadioButton('Option 2')
radio_button3 = QRadioButton('Option 3')

layout.addWidget(radio_button1)
layout.addWidget(radio_button2)
layout.addWidget(radio_button3)

radio_button1.setChecked(True)  # 设置默认选中

radio_button1.toggled.connect(on_radio_button_toggled)
radio_button2.toggled.connect(on_radio_button_toggled)
radio_button3.toggled.connect(on_radio_button_toggled)

window.show()

sys.exit(app.exec())
