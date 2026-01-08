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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QWidget)

class Ui_Toys(object):
    def setupUi(self, Toys):
        if not Toys.objectName():
            Toys.setObjectName(u"Toys")
        Toys.resize(1131, 757)
        Toys.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 16, 28);\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: #081e30;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Toys)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Toys)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Toys)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Toys)

        QMetaObject.connectSlotsByName(Toys)
    # setupUi

    def retranslateUi(self, Toys):
        Toys.setWindowTitle(QCoreApplication.translate("Toys", u"Form", None))
    # retranslateUi

