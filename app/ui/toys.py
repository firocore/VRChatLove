# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toys.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Toys(object):
    def setupUi(self, Toys):
        if not Toys.objectName():
            Toys.setObjectName(u"Toys")
        Toys.resize(1178, 809)
        Toys.setStyleSheet(u"QWidget {\n"
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
"QScrollBar::handle:vertical {\n"
"    background: #1a3d59;           /* \u0426\u0432\u0435\u0442 \"\u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430\" */\n"
"    min-height: 30px;              /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"    border-radius: 5px;            /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0451\u0432 */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #48647a;      /* \u0426\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #081e30;           /* \u0426\u0432\u0435\u0442 \u0444"
                        "\u043e\u043d\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
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
"    background: none;              /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043a\u0438 */\n"
"}")
        self.horizontalLayout = QHBoxLayout(Toys)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toys = QFrame(Toys)
        self.frame_toys.setObjectName(u"frame_toys")
        self.frame_toys.setFrameShape(QFrame.StyledPanel)
        self.frame_toys.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_toys)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.frame_toys)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 751, 791))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	background-color: #081e30;\n"
"	border: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 60))
        self.frame_4.setMaximumSize(QSize(1000, 45))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retreat = QFrame(self.scrollAreaWidgetContents)
        self.retreat.setObjectName(u"retreat")
        self.retreat.setMinimumSize(QSize(200, 60))
        self.retreat.setMaximumSize(QSize(1000, 45))
        self.retreat.setFrameShape(QFrame.StyledPanel)
        self.retreat.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.retreat, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_retreat = QLabel(self.scrollAreaWidgetContents)
        self.label_retreat.setObjectName(u"label_retreat")
        self.label_retreat.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_retreat.setFont(font)
        self.label_retreat.setStyleSheet(u"color: #ffffff")
        self.label_retreat.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_retreat)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.frame_toys)

        self.frame_side = QFrame(Toys)
        self.frame_side.setObjectName(u"frame_side")
        self.frame_side.setFrameShape(QFrame.StyledPanel)
        self.frame_side.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_side)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 50, 200, 45))
        self.frame_3.setMinimumSize(QSize(200, 45))
        self.frame_3.setMaximumSize(QSize(200, 45))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_side)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Toys)

        QMetaObject.connectSlotsByName(Toys)
    # setupUi

    def retranslateUi(self, Toys):
        Toys.setWindowTitle(QCoreApplication.translate("Toys", u"Form", None))
        self.label_retreat.setText(QCoreApplication.translate("Toys", u"No devices detected", None))
    # retranslateUi

