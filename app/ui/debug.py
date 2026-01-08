# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Debug(object):
    def setupUi(self, Debug):
        if not Debug.objectName():
            Debug.setObjectName(u"Debug")
        Debug.resize(1064, 651)
        Debug.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 16, 28);\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: #081e30;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	background-color: #081e30;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #112d43;\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1a3d59;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #1a3d59;           /* \u0426\u0432\u0435\u0442 \"\u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430\" */\n"
"    min-height: 30px;              /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"    border-radius: 5px;            /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0451\u0432 */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #48647a;      /* \u0426\u0432\u0435"
                        "\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #081e30;           /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    width: 10px;                   /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    margin: 0px 0px 0px 0px;       /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    border-radius: 5px;            /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0451\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;              /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;              /* \u0423\u0431\u0438\u0440"
                        "\u0430\u0435\u043c \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043a\u0438 */\n"
"}")
        self.horizontalLayout = QHBoxLayout(Debug)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(Debug)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"QWidget {\n"
"	background-color: #081e30;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.frame_main)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 693, 641))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.retreat = QFrame(self.scrollAreaWidgetContents)
        self.retreat.setObjectName(u"retreat")
        self.retreat.setStyleSheet(u"")
        self.retreat.setFrameShape(QFrame.StyledPanel)
        self.retreat.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.retreat)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_retreat = QLabel(self.retreat)
        self.label_retreat.setObjectName(u"label_retreat")
        self.label_retreat.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_retreat.setFont(font)
        self.label_retreat.setStyleSheet(u"color: #ffffff")
        self.label_retreat.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label_retreat)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.retreat)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.frame_main)

        self.frame_side = QFrame(Debug)
        self.frame_side.setObjectName(u"frame_side")
        self.frame_side.setStyleSheet(u"#frame_side {\n"
"background-color: rgb(0, 16, 28);\n"
"}\n"
"")
        self.frame_side.setFrameShape(QFrame.StyledPanel)
        self.frame_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_side)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_side)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_retreat_2 = QLabel(self.frame)
        self.label_retreat_2.setObjectName(u"label_retreat_2")
        self.label_retreat_2.setFont(font)
        self.label_retreat_2.setStyleSheet(u"color: #ffffff")
        self.label_retreat_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_retreat_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_side)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.button_clear = QPushButton(self.frame_2)
        self.button_clear.setObjectName(u"button_clear")
        sizePolicy.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy)
        self.button_clear.setFont(font)

        self.horizontalLayout_2.addWidget(self.button_clear)

        self.button_reload = QPushButton(self.frame_2)
        self.button_reload.setObjectName(u"button_reload")
        sizePolicy.setHeightForWidth(self.button_reload.sizePolicy().hasHeightForWidth())
        self.button_reload.setSizePolicy(sizePolicy)
        self.button_reload.setFont(font)
        self.button_reload.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.button_reload)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_3.setStretch(0, 13)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.frame_side)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Debug)

        QMetaObject.connectSlotsByName(Debug)
    # setupUi

    def retranslateUi(self, Debug):
        Debug.setWindowTitle(QCoreApplication.translate("Debug", u"Form", None))
        self.label_retreat.setText(QCoreApplication.translate("Debug", u"No osc parameters detected", None))
        self.label_retreat_2.setText(QCoreApplication.translate("Debug", u"In dev", None))
        self.button_clear.setText(QCoreApplication.translate("Debug", u"Clear", None))
        self.button_reload.setText(QCoreApplication.translate("Debug", u"Reload", None))
    # retranslateUi

