import webbrowser
import ctypes

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QButtonGroup
from PySide6.QtCore import QThread, Qt, QPoint

from app.ui import resources_rc
from app.ui.main_window import Ui_MainWindow
from app.ui.debug import Ui_Denug
from app.ui.toys import Ui_Toys
from app.ui.assignment import Ui_Assignment
from app.ui.settings import Ui_Settings

from app import constants
from app.utils import versioning


class ToysWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Toys()
        self.ui.setupUi(self)


class AssignmentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Assignment()
        self.ui.setupUi(self)


class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)


class DebugWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Denug()
        self.ui.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # --- Отключение стандартного окна
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.button_minimize.clicked.connect(self.showMinimized)
        self.button_maximize.clicked.connect(self.toggle_maximize_restore)
        self.button_close.clicked.connect(self.close)
        self.button_settings_h.clicked.connect(self.go_to_settings)

        # --- Перемещение окна
        self.header.mousePressEvent = self.header_mouse_press_event
        self.header.mouseMoveEvent = self.header_mouse_move_event
        self.header.mouseReleaseEvent = self.header_mouse_release_event

        # --- Подготовка панели версий ---
        self.button_version.clicked.connect(self.on_download_clicked)
        self.button_version.setText("v" + constants.APP_VERSION)

        self.button_download.hide()
        self.button_download.clicked.connect(self.on_download_clicked)
        
        # --- Проверка версии ---
        self.version_checker = versioning.VersionChecker()
        self.version_thread = QThread()

        self.version_checker.moveToThread(self.version_thread)
        self.version_checker.versionChecked.connect(self.on_version_checked)
        self.version_thread.started.connect(self.version_checker.check_version)
        self.version_thread.start()

        # --- Разделы ---
        self.toys_widget = ToysWidget()
        self.assignment_widget = AssignmentWidget()
        self.debug_widget = DebugWidget()
        self.settigs_widget = SettingsWidget()

        self.stackedWidget.addWidget(self.toys_widget)          # 1
        self.stackedWidget.addWidget(self.assignment_widget)    # 2
        self.stackedWidget.addWidget(self.settigs_widget)       # 3
        self.stackedWidget.addWidget(self.debug_widget)         # 4

        self.section_buttons = QButtonGroup(self)
        self.section_buttons.setExclusive(True)
        self.section_buttons.addButton(self.button_toys, 1)
        self.section_buttons.addButton(self.button_assignment, 2)
        self.section_buttons.addButton(self.button_settings, 3)
        self.section_buttons.addButton(self.button_debug, 4)

        self.section_buttons.idClicked.connect(self.switch_section)

        self.stackedWidget.setCurrentWidget(self.toys_widget)
        self.button_toys.setChecked(True)


    def switch_section(self, idx: int):
        self.stackedWidget.setCurrentIndex(idx)

    def go_to_settings(self):
        # Индекс settings в stackedWidget и QButtonGroup должен совпадать!
        settings_index = 3 # self.stackedWidget.addWidget(self.settigs_widget)
        self.stackedWidget.setCurrentIndex(settings_index)
        # Установить checked у кнопки settings через QButtonGroup
        self.section_buttons.button(settings_index).setChecked(True)


    def header_mouse_press_event(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_active = True
            self._drag_pos = event.globalPosition().toPoint()
            event.accept()


    def header_mouse_move_event(self, event):
        if self._drag_active and event.buttons() & Qt.LeftButton:
            # Перемещаем главное окно
            main_window = self.window()
            if main_window:
                delta = event.globalPosition().toPoint() - self._drag_pos
                main_window.move(main_window.pos() + delta)
                self._drag_pos = event.globalPosition().toPoint()
            event.accept()


    def header_mouse_release_event(self, event):
        self._drag_active = False
        event.accept()

    def nativeEvent(self, eventType, message):
        if eventType == "windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            if msg.message == 0x0084:  # WM_NCHITTEST
                x = msg.lParam & 0xFFFF
                y = (msg.lParam >> 16) & 0xFFFF
                global_pos = QPoint(x, y)
                pos = self.mapFromGlobal(global_pos)
                w, h = self.width(), self.height()
                bw = constants.BORDER_WIDTH

                # Углы
                if pos.x() < bw and pos.y() < bw:
                    return True, 13  # HTTOPLEFT
                if pos.x() > w - bw and pos.y() < bw:
                    return True, 14  # HTTOPRIGHT
                if pos.x() < bw and pos.y() > h - bw:
                    return True, 16  # HTBOTTOMLEFT
                if pos.x() > w - bw and pos.y() > h - bw:
                    return True, 17  # HTBOTTOMRIGHT

                # Грани
                if pos.x() < bw:
                    return True, 10  # HTLEFT
                if pos.x() > w - bw:
                    return True, 11  # HTRIGHT
                if pos.y() < bw:
                    return True, 12  # HTTOP
                if pos.y() > h - bw:
                    return True, 15  # HTBOTTOM
                
        return False, 0
    
    def resizeEvent(self, event):
        print("resize", self.size())
        super().resizeEvent(event)


    def toggle_maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def on_version_checked(self, remote_version: str):
        if remote_version and remote_version != constants.APP_VERSION:
            self.button_download.show()
            self.on_download_clicked()
        else:
            self.button_download.hide()

        self.version_thread.quit()
        self.version_thread.wait()


    def on_download_clicked(self):
        webbrowser.open(constants.URL_REPO + "/releases")



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
