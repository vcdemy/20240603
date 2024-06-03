import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PyQt6.QtGui import QPixmap

# 定义一个函数，用于打开文件选择对话框并显示选择的图片
def open_file():
    # 打开文件选择对话框
    file_name, _ = QFileDialog.getOpenFileName(window, 'Open Image File', '', 'Image Files (*.png *.jpg *.bmp)')
    if file_name:  # 如果用户选择了文件
        pixmap = QPixmap(file_name)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建窗口对象
window = QWidget()
window.setWindowTitle('Image Display Example')
window.setGeometry(100, 100, 800, 600)

# 创建一个垂直布局
layout = QVBoxLayout()

# 创建一个 QLabel 对象
label = QLabel()
layout.addWidget(label)

# 创建一个按钮，用于打开文件选择对话框
button = QPushButton('Open Image')
button.clicked.connect(open_file)
layout.addWidget(button)

# 设置窗口的布局
window.setLayout(layout)

# 显示窗口
window.show()

# 运行应用程序的事件循环
sys.exit(app.exec())
