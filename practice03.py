import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.statusBar().showMessage("Hello MainWindow!")
window.menuBar().addMenu('File')
window.show()
sys.exit(app.exec())
