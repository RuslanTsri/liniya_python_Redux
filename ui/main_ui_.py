# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: #EDEDEE;")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.verticalWidget = QWidget(MainWindow)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(99)
        sizePolicy1.setVerticalStretch(99)
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.verticalWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.vboxLayout = QVBoxLayout(self.verticalWidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalWidget1 = QWidget(self.verticalWidget)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(100, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalWidget = QWidget(self.verticalWidget1)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalWidget2 = QWidget(self.horizontalWidget)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalWidget2.setMinimumSize(QSize(200, 100))
        self.verticalWidget2.setMaximumSize(QSize(200, 100))
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.verticalWidget2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(180, 40))
        self.label.setMaximumSize(QSize(180, 40))
        self.label.setStyleSheet(u"font: 16pt \"Furore\";\n"
"color: #38A962;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.plastic_max_len_lineEdit = QLineEdit(self.verticalWidget2)
        self.plastic_max_len_lineEdit.setObjectName(u"plastic_max_len_lineEdit")
        self.plastic_max_len_lineEdit.setMinimumSize(QSize(180, 40))
        self.plastic_max_len_lineEdit.setMaximumSize(QSize(180, 40))
        self.plastic_max_len_lineEdit.setStyleSheet(u"background-color: #38A962;\n"
"font: 14pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 15px;")
        self.plastic_max_len_lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.plastic_max_len_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.plastic_max_len_lineEdit)


        self.horizontalLayout.addWidget(self.verticalWidget2)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalWidget3 = QWidget(self.horizontalWidget)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalWidget3.setMinimumSize(QSize(200, 100))
        self.verticalWidget3.setMaximumSize(QSize(200, 100))
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.verticalWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(180, 40))
        self.label_2.setMaximumSize(QSize(180, 40))
        self.label_2.setStyleSheet(u"font: 16pt \"Furore\";\n"
"color: #38A962;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.plastic_len_finished_label = QLabel(self.verticalWidget3)
        self.plastic_len_finished_label.setObjectName(u"plastic_len_finished_label")
        self.plastic_len_finished_label.setMinimumSize(QSize(180, 40))
        self.plastic_len_finished_label.setMaximumSize(QSize(180, 40))
        self.plastic_len_finished_label.setStyleSheet(u"font: 16pt \"Furore\";\n"
"color: #38A962;")
        self.plastic_len_finished_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.plastic_len_finished_label)


        self.horizontalLayout.addWidget(self.verticalWidget3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.horizontalWidget)


        self.vboxLayout.addWidget(self.verticalWidget1)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vboxLayout.addItem(self.verticalSpacer_2)

        self.horizontalWidget1 = QWidget(self.verticalWidget)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalWidget1.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalWidget4 = QWidget(self.horizontalWidget1)
        self.verticalWidget4.setObjectName(u"verticalWidget4")
        self.verticalWidget4.setMinimumSize(QSize(200, 100))
        self.verticalWidget4.setMaximumSize(QSize(200, 100))
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.verticalWidget4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(180, 40))
        self.label_4.setMaximumSize(QSize(180, 40))
        self.label_4.setStyleSheet(u"font: 16pt \"Furore\";\n"
"color: #38A962;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.diameter_lineEdit = QLineEdit(self.verticalWidget4)
        self.diameter_lineEdit.setObjectName(u"diameter_lineEdit")
        self.diameter_lineEdit.setMinimumSize(QSize(180, 40))
        self.diameter_lineEdit.setMaximumSize(QSize(180, 40))
        self.diameter_lineEdit.setStyleSheet(u"background-color: #38A962;\n"
"font: 14pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 15px;")
        self.diameter_lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.diameter_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.diameter_lineEdit)


        self.horizontalLayout_2.addWidget(self.verticalWidget4)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.verticalWidget5 = QWidget(self.horizontalWidget1)
        self.verticalWidget5.setObjectName(u"verticalWidget5")
        self.verticalWidget5.setMinimumSize(QSize(200, 100))
        self.verticalWidget5.setMaximumSize(QSize(200, 100))
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.verticalWidget5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(180, 40))
        self.label_5.setMaximumSize(QSize(180, 40))
        self.label_5.setStyleSheet(u"font: 16pt \"Furore\";\n"
"color: #38A962;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.speed_lineEdit = QLineEdit(self.verticalWidget5)
        self.speed_lineEdit.setObjectName(u"speed_lineEdit")
        self.speed_lineEdit.setMinimumSize(QSize(180, 40))
        self.speed_lineEdit.setMaximumSize(QSize(180, 40))
        self.speed_lineEdit.setStyleSheet(u"background-color: #38A962;\n"
"font: 14pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 15px;")
        self.speed_lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.speed_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.speed_lineEdit)


        self.horizontalLayout_2.addWidget(self.verticalWidget5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.vboxLayout.addWidget(self.horizontalWidget1)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vboxLayout.addItem(self.verticalSpacer_4)

        self.horizontalWidget2 = QWidget(self.verticalWidget)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalWidget2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.testButton = QPushButton(self.horizontalWidget2)
        self.testButton.setObjectName(u"testButton")
        self.testButton.setMinimumSize(QSize(180, 40))
        self.testButton.setMaximumSize(QSize(180, 40))
        self.testButton.setStyleSheet(u"background-color: #38A962;\n"
"font: 14pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 15px;")

        self.horizontalLayout_3.addWidget(self.testButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.vboxLayout.addWidget(self.horizontalWidget2)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_3)

        MainWindow.setCentralWidget(self.verticalWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u043e \u043c", None))
        self.plastic_max_len_lineEdit.setText("")
        self.plastic_max_len_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043a\u0442\u0438\u0447\u043d\u0456", None))
        self.plastic_len_finished_label.setText(QCoreApplication.translate("MainWindow", u"0 \u041c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0456\u0430\u043c\u0435\u0442\u0440", None))
        self.diameter_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.75", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0432\u0438\u0434\u043a\u0456\u0441\u0442\u044c \u043c/\u0441", None))
        self.speed_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442", None))
    # retranslateUi

