from PySide6.QtWidgets import QMainWindow, QApplication

import app.ui.resources_rc
from app.ui.main_window import Ui_MainWindow
from app import constants

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_version.setText(constants.APP_VERSION)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
