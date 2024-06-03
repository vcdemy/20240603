import practice05
import sys
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = practice05.MyWindow()
window.show()
sys.exit(app.exec())
