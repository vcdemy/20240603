import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import skimage

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('課間小專案')
window.setFixedSize(640, 360)
label1 = QLabel(window)
label2 = QLabel(window)
button = QPushButton('Open File', window)
label1.setFixedSize(300, 300)
label1.move(10, 10)
label2.setFixedSize(300, 300)
label2.move(325, 10)
button.setGeometry(10, 320, 150, 30)
label1.setStyleSheet('background-color: gray')
label2.setStyleSheet('background-color: gray')

pixmap1 = QPixmap('therock.jpg')
pixmap1 = pixmap1.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
label1.setPixmap(pixmap1)
pixmap2 = QPixmap('therock.jpg')
pixmap2 = pixmap2.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
label2.setPixmap(pixmap2)

window.show()

sys.exit(app.exec())