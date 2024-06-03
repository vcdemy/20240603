import skimage
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QImage

app = QApplication(sys.argv)

window = QWidget()
label = QLabel(window)

img = skimage.io.imread('therock.jpg')
bytes_per_line = img.shape[1]*img.shape[2]
q_image = QImage(img, img.shape[1], img.shape[0], bytes_per_line, QImage.Format.Format_RGB888)

pixmap = QPixmap.fromImage(q_image)
label.setPixmap(pixmap)
label.resize(q_image.width(), q_image.height())

window.show()

sys.exit(app.exec())