# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
from app.ui import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1249, 687)
        MainWindow.setMinimumSize(QSize(600, 400))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/sidebar/toys.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 16, 28);\n"
"border: none;\n"
"border-radius: 10px;")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Leelawadee UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.header.setFont(font1)
        self.header.setStyleSheet(u"QToolButton {\n"
"  	border: none;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.info = QFrame(self.header)
        self.info.setObjectName(u"info")
        self.info.setFont(font1)
        self.info.setFrameShape(QFrame.StyledPanel)
        self.info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.info)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.label_name = QLabel(self.info)
        self.label_name.setObjectName(u"label_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy1)
        self.label_name.setMaximumSize(QSize(80, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 7px;\n"
"padding-right: 7px;")
        self.label_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_name)

        self.button_version = QPushButton(self.info)
        self.button_version.setObjectName(u"button_version")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_version.sizePolicy().hasHeightForWidth())
        self.button_version.setSizePolicy(sizePolicy2)
        self.button_version.setMaximumSize(QSize(65, 20))
        self.button_version.setFont(font2)
        self.button_version.setStyleSheet(u"background-color: rgb(16, 59, 52);\n"
"color: rgb(80, 232, 125);\n"
"border-radius: 5px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;")

        self.horizontalLayout_5.addWidget(self.button_version)

        self.button_download = QToolButton(self.info)
        self.button_download.setObjectName(u"button_download")
        self.button_download.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(12)
        self.button_download.setFont(font3)
        self.button_download.setStyleSheet(u"QToolButton {\n"
"	padding: 5px;\n"
"  	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/header/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_download.setIcon(icon1)
        self.button_download.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.button_download)

        self.button_remote_control = QPushButton(self.info)
        self.button_remote_control.setObjectName(u"button_remote_control")
        self.button_remote_control.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.button_remote_control.sizePolicy().hasHeightForWidth())
        self.button_remote_control.setSizePolicy(sizePolicy2)
        self.button_remote_control.setMaximumSize(QSize(150, 20))
        self.button_remote_control.setFont(font2)
        self.button_remote_control.setStyleSheet(u"background-color: rgb(104, 0, 1);\n"
"color: rgb(255, 33, 36);\n"
"border-radius: 5px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;")
        self.button_remote_control.setFlat(False)

        self.horizontalLayout_5.addWidget(self.button_remote_control)

        self.button_external_control = QPushButton(self.info)
        self.button_external_control.setObjectName(u"button_external_control")
        sizePolicy2.setHeightForWidth(self.button_external_control.sizePolicy().hasHeightForWidth())
        self.button_external_control.setSizePolicy(sizePolicy2)
        self.button_external_control.setMaximumSize(QSize(150, 20))
        self.button_external_control.setFont(font2)
        self.button_external_control.setStyleSheet(u"background-color: rgb(104, 0, 1);\n"
"color: rgb(255, 33, 36);\n"
"border-radius: 5px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;")

        self.horizontalLayout_5.addWidget(self.button_external_control)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.retreat_2 = QFrame(self.info)
        self.retreat_2.setObjectName(u"retreat_2")
        self.retreat_2.setFont(font1)
        self.retreat_2.setFrameShape(QFrame.StyledPanel)
        self.retreat_2.setFrameShadow(QFrame.Raised)
        self.retreat_2.setLineWidth(1)

        self.horizontalLayout_5.addWidget(self.retreat_2)


        self.horizontalLayout_4.addWidget(self.info)

        self.control = QFrame(self.header)
        self.control.setObjectName(u"control")
        self.control.setFont(font1)
        self.control.setStyleSheet(u"QToolButton {\n"
"	padding: 2px;\n"
"  	border: none;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  	background: #112d43;\n"
"}")
        self.control.setFrameShape(QFrame.StyledPanel)
        self.control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.control)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.button_settings_h = QToolButton(self.control)
        self.button_settings_h.setObjectName(u"button_settings_h")
        self.button_settings_h.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/icons/header/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_settings_h.setIcon(icon2)
        self.button_settings_h.setIconSize(QSize(26, 26))

        self.horizontalLayout_6.addWidget(self.button_settings_h)

        self.button_minimize = QToolButton(self.control)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/icons/header/window-minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_minimize.setIcon(icon3)
        self.button_minimize.setIconSize(QSize(18, 19))

        self.horizontalLayout_6.addWidget(self.button_minimize)

        self.button_maximize = QToolButton(self.control)
        self.button_maximize.setObjectName(u"button_maximize")
        self.button_maximize.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/header/window-restore.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_maximize.setIcon(icon4)
        self.button_maximize.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.button_maximize)

        self.button_close = QToolButton(self.control)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/icons/header/window-close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_close.setIcon(icon5)
        self.button_close.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.button_close)


        self.horizontalLayout_4.addWidget(self.control)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.header)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 9)
        self.sidebar = QWidget(self.body)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy3)
        self.sidebar.setMaximumSize(QSize(85, 16777215))
        self.sidebar.setFont(font1)
        self.sidebar.setLayoutDirection(Qt.LeftToRight)
        self.sidebar.setStyleSheet(u"QToolButton {\n"
" 	background: #00101c;\n"
"	color: #fff;\n"
"  	border: none;\n"
"	border-radius: 8px;\n"
"	padding-top: 8px;\n"
"	padding-bottom: 8px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  	background: #081e30;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"	background-color: #2e2145;\n"
"	color: #9d5cd4;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_toys = QToolButton(self.sidebar)
        self.button_toys.setObjectName(u"button_toys")
        sizePolicy.setHeightForWidth(self.button_toys.sizePolicy().hasHeightForWidth())
        self.button_toys.setSizePolicy(sizePolicy)
        self.button_toys.setFont(font2)
        self.button_toys.setLayoutDirection(Qt.LeftToRight)
        self.button_toys.setAutoFillBackground(False)
        self.button_toys.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/sidebar/toys.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/sidebar/toys_on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_toys.setIcon(icon6)
        self.button_toys.setIconSize(QSize(32, 42))
        self.button_toys.setCheckable(True)
        self.button_toys.setChecked(False)
        self.button_toys.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button_toys.setAutoRaise(False)

        self.verticalLayout_3.addWidget(self.button_toys)

        self.button_assignment = QToolButton(self.sidebar)
        self.button_assignment.setObjectName(u"button_assignment")
        sizePolicy.setHeightForWidth(self.button_assignment.sizePolicy().hasHeightForWidth())
        self.button_assignment.setSizePolicy(sizePolicy)
        self.button_assignment.setFont(font2)
        self.button_assignment.setLayoutDirection(Qt.LeftToRight)
        self.button_assignment.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/sidebar/human.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/sidebar/human_on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_assignment.setIcon(icon7)
        self.button_assignment.setIconSize(QSize(28, 42))
        self.button_assignment.setCheckable(True)
        self.button_assignment.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.button_assignment)

        self.button_debug = QToolButton(self.sidebar)
        self.button_debug.setObjectName(u"button_debug")
        sizePolicy.setHeightForWidth(self.button_debug.sizePolicy().hasHeightForWidth())
        self.button_debug.setSizePolicy(sizePolicy)
        self.button_debug.setFont(font2)
        self.button_debug.setLayoutDirection(Qt.LeftToRight)
        self.button_debug.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/sidebar/tool.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/sidebar/tool_on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_debug.setIcon(icon8)
        self.button_debug.setIconSize(QSize(32, 42))
        self.button_debug.setCheckable(True)
        self.button_debug.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.button_debug)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.button_settings = QToolButton(self.sidebar)
        self.button_settings.setObjectName(u"button_settings")
        sizePolicy.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy)
        self.button_settings.setFont(font2)
        self.button_settings.setLayoutDirection(Qt.LeftToRight)
        self.button_settings.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/sidebar/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icons/sidebar/settings_on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_settings.setIcon(icon9)
        self.button_settings.setIconSize(QSize(32, 38))
        self.button_settings.setCheckable(True)
        self.button_settings.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.button_settings)


        self.horizontalLayout_2.addWidget(self.sidebar)

        self.stackedWidget = QStackedWidget(self.body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"")
        self.empty_page = QWidget()
        self.empty_page.setObjectName(u"empty_page")
        self.stackedWidget.addWidget(self.empty_page)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VRCLove", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"VRCLove", None))
        self.button_version.setText(QCoreApplication.translate("MainWindow", u"v0.0.0", None))
        self.button_download.setText("")
        self.button_remote_control.setText(QCoreApplication.translate("MainWindow", u"Remote Contol", None))
        self.button_external_control.setText(QCoreApplication.translate("MainWindow", u"External contol", None))
        self.button_settings_h.setText("")
        self.button_minimize.setText("")
        self.button_maximize.setText("")
        self.button_close.setText("")
        self.button_toys.setText(QCoreApplication.translate("MainWindow", u"Toys", None))
        self.button_assignment.setText(QCoreApplication.translate("MainWindow", u"Toys\n"
"Assignment", None))
        self.button_debug.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.button_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

