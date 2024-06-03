import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Different Layouts Example')
window.setGeometry(100, 100, 400, 300)

# 创建左侧布局
left_layout = QVBoxLayout()

left_label = QLabel('Left Side')
left_layout.addWidget(left_label)

left_button = QPushButton('Left Button')
left_layout.addWidget(left_button)

# 创建右侧布局
right_layout = QVBoxLayout()

right_label = QLabel('Right Side')
right_layout.addWidget(right_label)

right_button = QPushButton('Right Button')
right_layout.addWidget(right_button)

# 将左右布局放置在水平布局中
main_layout = QHBoxLayout()
main_layout.addLayout(left_layout)
main_layout.addLayout(right_layout)

# 将水平布局设置为窗口的主布局
window.setLayout(main_layout)

window.show()
sys.exit(app.exec())
