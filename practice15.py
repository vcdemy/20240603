import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer

def timeout():
    print('Triggered!')

app = QApplication(sys.argv)

window = QWidget()

timer = QTimer()
timer.timeout.connect(timeout)
timer.start(1000)

window.show()

sys.exit(app.exec())