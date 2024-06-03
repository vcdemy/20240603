import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimer

def timeout():
    global count
    label.setText(f"{count}")
    count += 1

app = QApplication(sys.argv)

window = QWidget()
label = QLabel(window)

timer = QTimer()
timer.timeout.connect(timeout)
timer.start(1000)

count = 0

window.show()

sys.exit(app.exec())