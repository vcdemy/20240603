import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 定义一个更新标签内容的函数
def update_label():
    label.setText('Timer triggered!')

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建窗口对象
window = QWidget()
window.setWindowTitle('QTimer singleShot Example')
window.setGeometry(100, 100, 300, 200)

# 创建一个垂直布局
layout = QVBoxLayout()
window.setLayout(layout)

# 创建一个标签
label = QLabel('Waiting for timer...', window)
layout.addWidget(label)

# 使用 QTimer.singleShot 设置一个单次触发的定时器
QTimer.singleShot(5000, update_label)  # 设置定时器5秒后触发update_label函数

# 显示窗口
window.show()

# 运行应用程序的事件循环
sys.exit(app.exec())
