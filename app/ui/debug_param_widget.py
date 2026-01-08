# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_param_widget.ui'
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
    QSizePolicy, QToolButton, QWidget)
from app.ui import resources_rc

class Ui_debug_widget(object):
    def setupUi(self, debug_widget):
        if not debug_widget.objectName():
            debug_widget.setObjectName(u"debug_widget")
        debug_widget.resize(490, 35)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(debug_widget.sizePolicy().hasHeightForWidth())
        debug_widget.setSizePolicy(sizePolicy)
        debug_widget.setMinimumSize(QSize(0, 35))
        debug_widget.setMaximumSize(QSize(16777215, 35))
        debug_widget.setStyleSheet(u"QWidget {\n"
"	background-color: #112d43;\n"
"	border: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(debug_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(debug_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_name)

        self.label_value = QLabel(self.frame)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setFont(font)
        self.label_value.setLayoutDirection(Qt.RightToLeft)
        self.label_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_value)

        self.button_favorite = QToolButton(self.frame)
        self.button_favorite.setObjectName(u"button_favorite")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_favorite.sizePolicy().hasHeightForWidth())
        self.button_favorite.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/debug/star.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/debug/star_filled.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_favorite.setIcon(icon)
        self.button_favorite.setIconSize(QSize(24, 24))
        self.button_favorite.setCheckable(True)
        self.button_favorite.setChecked(False)
        self.button_favorite.setAutoRaise(False)

        self.horizontalLayout_2.addWidget(self.button_favorite)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(debug_widget)

        QMetaObject.connectSlotsByName(debug_widget)
    # setupUi

    def retranslateUi(self, debug_widget):
        debug_widget.setWindowTitle(QCoreApplication.translate("debug_widget", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("debug_widget", u"name", None))
        self.label_value.setText(QCoreApplication.translate("debug_widget", u"value", None))
        self.button_favorite.setText("")
    # retranslateUi

