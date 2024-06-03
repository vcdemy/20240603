import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Image Display Example')
window.setGeometry(100, 100, 800, 600)  # 设置窗口大小，可以根据图片大小调整

label = QLabel(window)
pixmap = QPixmap('therock.jpg')  # 替换为你的图片路径
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
window.show()

sys.exit(app.exec())
