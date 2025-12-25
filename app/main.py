import webbrowser
import ctypes
from ctypes import c_short
import asyncio

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QButtonGroup
from PySide6.QtCore import QThread, Qt, QPoint, Signal, Slot
from qasync import QEventLoop

from app.ui import resources_rc
from app.ui.main_window import Ui_MainWindow
from app.ui.debug import Ui_Debug
from app.ui.debug_param_widget import Ui_debug_widget
from app.ui.toys import Ui_Toys
from app.ui.assignment import Ui_Assignment
from app.ui.settings import Ui_Settings

from app import constants
from app.utils import versioning
from app.osc.osc_listener import start_osc_server, store


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
    param_updated = Signal(str, object)
    clear_params = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Debug()
        self.ui.setupUi(self)

        self.favorites = []

        self.param_widgets: dict[str, DebugParamWidget] = {}
        self.param_updated.connect(self.update_param)

        self.clear_params.connect(self.clear_all_params)

    @Slot(str, object)
    def update_param(self, name: str, value):
        if name in self.param_widgets:
            widget = self.param_widgets[name]
            old_value = widget.get_value()
            str_value = str(value)

            if old_value != str_value:
                widget.set_value(value)
        else:
            print("New parameter added:", name)
            widget = DebugParamWidget(name, value)
            widget.favorite_toggled.connect(self.on_favorite_toggled)
            self.param_widgets[name] = widget
            # Вставляем перед retreat, если он есть
            idx = self.ui.verticalLayout_2.indexOf(self.ui.retreat)
            self.ui.verticalLayout_2.insertWidget(idx, widget)

    @Slot()
    def clear_all_params(self):
        for widget in self.param_widgets.values():
            widget.setParent(None)
            widget.deleteLater()

        self.param_widgets.clear()
        self.favorites.clear()

    @Slot(str, bool)
    def on_favorite_toggled(self, name: str, checked: bool):
        widget = self.param_widgets.get(name)
        if not widget:
            return
        
        layout = self.ui.verticalLayout_2
        layout.removeWidget(widget)

        if checked:
            # Добавить в список избранных и переместить наверх (последним среди избранных)
            self.favorites.append(name)
            # Найти индекс последнего избранного
            if len(self.favorites) > 1:
                last_fav_name = self.favorites[-2]
                last_fav_widget = self.param_widgets[last_fav_name]
                idx = layout.indexOf(last_fav_widget) + 1
            else:
                idx = 0
            layout.insertWidget(idx, widget)
        else:
            # Убрать из избранных и переместить перед retreat
            if name in self.favorites:
                self.favorites.remove(name)
            idx = layout.indexOf(self.ui.retreat)
            layout.insertWidget(len(self.favorites), widget)

class DebugParamWidget(QWidget):
    favorite_toggled = Signal(str, bool)

    def __init__(self, name: str, value, parent=None):
        super().__init__(parent)
        self.ui = Ui_debug_widget()
        self.ui.setupUi(self)
        self.set_name(name)
        self.set_value(value)

        self.ui.button_favorite.toggled.connect(self.on_favorite_toggled)

    def set_name(self, name: str):
        self.ui.label_name.setText(str(name))

    def set_value(self, value):
        self.ui.label_value.setText(str(value))

    def get_value(self) -> str:
        return self.ui.label_value.text()

    def on_favorite_toggled(self, checked: bool):
        self.favorite_toggled.emit(self.ui.label_name.text(), checked)

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
                x = c_short(msg.lParam & 0xFFFF).value
                y = c_short((msg.lParam >> 16) & 0xFFFF).value
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
    from app.osc.osc_listener import set_debug_widget

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    set_debug_widget(window.debug_widget)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        loop.create_task(start_osc_server())
        loop.run_forever()
        sys.exit(app.exec())


    
