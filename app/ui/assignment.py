# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assignment.ui'
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

class Ui_Assignment(object):
    def setupUi(self, Assignment):
        if not Assignment.objectName():
            Assignment.setObjectName(u"Assignment")
        Assignment.resize(400, 300)
        Assignment.setStyleSheet(u"background-color: rgb(8, 30, 48);\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(Assignment)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Assignment)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Assignment)

        QMetaObject.connectSlotsByName(Assignment)
    # setupUi

    def retranslateUi(self, Assignment):
        Assignment.setWindowTitle(QCoreApplication.translate("Assignment", u"Form", None))
        self.label.setText(QCoreApplication.translate("Assignment", u"ASSIGNMENT", None))
    # retranslateUi

