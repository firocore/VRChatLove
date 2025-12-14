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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Denug(object):
    def setupUi(self, Denug):
        if not Denug.objectName():
            Denug.setObjectName(u"Denug")
        Denug.resize(631, 349)
        Denug.setStyleSheet(u"background-color: rgb(8, 30, 48);\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(Denug)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Denug)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Denug)

        QMetaObject.connectSlotsByName(Denug)
    # setupUi

    def retranslateUi(self, Denug):
        Denug.setWindowTitle(QCoreApplication.translate("Denug", u"Form", None))
        self.label.setText(QCoreApplication.translate("Denug", u"DEBUG", None))
    # retranslateUi

