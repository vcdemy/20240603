import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap

def open_file():
    file_name, _ = QFileDialog.getOpenFileName(window, 'Open Image File', '', 'Image Files (*.png *.jpg *.bmp)')
    if file_name:  # 如果用户选择了文件
        pixmap = QPixmap(file_name)
        left_label.setPixmap(pixmap)
        left_label.resize(pixmap.width(), pixmap.height())

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

# 将左右布局放置在水平布局中
main_layout = QHBoxLayout()
main_layout.addLayout(left_layout)
main_layout.addLayout(right_layout)

# 将水平布局设置为窗口的主布局
window.setLayout(main_layout)

left_button.clicked.connect(open_file)

window.show()
sys.exit(app.exec())
