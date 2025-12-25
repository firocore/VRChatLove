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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Toys(object):
    def setupUi(self, Toys):
        if not Toys.objectName():
            Toys.setObjectName(u"Toys")
        Toys.resize(461, 333)
        Toys.setStyleSheet(u"background-color: rgb(8, 30, 48);\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(Toys)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Toys)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Toys)

        QMetaObject.connectSlotsByName(Toys)
    # setupUi

    def retranslateUi(self, Toys):
        Toys.setWindowTitle(QCoreApplication.translate("Toys", u"Form", None))
        self.label.setText(QCoreApplication.translate("Toys", u"TOYS", None))
    # retranslateUi

