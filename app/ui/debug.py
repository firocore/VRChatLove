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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Debug(object):
    def setupUi(self, Debug):
        if not Debug.objectName():
            Debug.setObjectName(u"Debug")
        Debug.resize(1156, 832)
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 755, 822))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.retreat = QFrame(self.scrollAreaWidgetContents)
        self.retreat.setObjectName(u"retreat")
        self.retreat.setStyleSheet(u"")
        self.retreat.setFrameShape(QFrame.StyledPanel)
        self.retreat.setFrameShadow(QFrame.Raised)

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

        self.horizontalLayout.addWidget(self.frame_side)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Debug)

        QMetaObject.connectSlotsByName(Debug)
    # setupUi

    def retranslateUi(self, Debug):
        Debug.setWindowTitle(QCoreApplication.translate("Debug", u"Form", None))
    # retranslateUi

