# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 480)
        Dialog.setMinimumSize(QSize(800, 480))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalWidget = QWidget(Dialog)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(500, 200))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalWidget.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 7px;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.info_label = QLabel(self.horizontalWidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setStyleSheet(u"background: transparent;\n"
"font: 24pt \"Furore\";\n"
"color: #000;")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.info_label)


        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 2)

        self.horizontalFrame = QFrame(Dialog)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(self.horizontalFrame)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(170, 60))
        self.cancelButton.setMaximumSize(QSize(16777215, 16777215))
        self.cancelButton.setStyleSheet(u"border-radius: 7%;\n"
"background: #A93838;\n"
"color: #ffffff;\n"
"font: 20pt \"Furore\";")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.close_button = QPushButton(self.horizontalFrame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(170, 60))
        self.close_button.setMaximumSize(QSize(16777215, 16777215))
        self.close_button.setStyleSheet(u"border-radius: 7%;\n"
"background: #38A962;\n"
"color: #ffffff;\n"
"font: 20pt \"Furore\";")

        self.horizontalLayout.addWidget(self.close_button)


        self.gridLayout.addWidget(self.horizontalFrame, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.info_label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
        self.close_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
    # retranslateUi

