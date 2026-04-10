# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.right_detector_button = QPushButton(self.centralwidget)
        self.right_detector_button.setObjectName(u"right_detector_button")
        self.right_detector_button.setMinimumSize(QSize(100, 60))
        self.right_detector_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.right_detector_button, 8, 4, 1, 1)

        self.minus_button = QPushButton(self.centralwidget)
        self.minus_button.setObjectName(u"minus_button")
        self.minus_button.setMinimumSize(QSize(50, 60))
        self.minus_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.minus_button, 4, 5, 1, 1)

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setMinimumSize(QSize(50, 60))
        self.button_1.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.button_1, 4, 2, 1, 1)

        self.left_detector_button = QPushButton(self.centralwidget)
        self.left_detector_button.setObjectName(u"left_detector_button")
        self.left_detector_button.setMinimumSize(QSize(100, 60))
        self.left_detector_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.left_detector_button, 8, 1, 1, 1)

        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(170, 60))
        self.verticalWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.len_button = QPushButton(self.verticalWidget)
        self.len_button.setObjectName(u"len_button")
        self.len_button.setMinimumSize(QSize(150, 60))
        self.len_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.verticalLayout_4.addWidget(self.len_button)


        self.gridLayout_2.addWidget(self.verticalWidget, 0, 0, 1, 2)

        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(100, 60))
        self.stop_button.setMaximumSize(QSize(9999999, 60))
        self.stop_button.setStyleSheet(u"background-color: #A93838;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.stop_button, 8, 5, 1, 1)

        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(50, 60))
        self.add_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.add_button, 4, 0, 1, 1)

        self.button_10 = QPushButton(self.centralwidget)
        self.button_10.setObjectName(u"button_10")
        self.button_10.setMinimumSize(QSize(50, 60))
        self.button_10.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.button_10, 4, 1, 1, 1)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(100, 60))
        self.start_button.setMaximumSize(QSize(9999999, 60))
        self.start_button.setStyleSheet(u"background-color: #3858A9;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.start_button, 8, 0, 1, 1)

        self.verticalWidget_4 = QWidget(self.centralwidget)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalWidget_4.setMinimumSize(QSize(170, 100))
        self.verticalWidget_4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 40))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.diametr_button = QPushButton(self.verticalWidget_4)
        self.diametr_button.setObjectName(u"diametr_button")
        self.diametr_button.setMinimumSize(QSize(150, 60))
        self.diametr_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.verticalLayout_6.addWidget(self.diametr_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.verticalWidget_4, 2, 0, 1, 2)

        self.verticalWidget_5 = QWidget(self.centralwidget)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        self.verticalWidget_5.setMinimumSize(QSize(170, 100))
        self.verticalWidget_5.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 40))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.width_button = QPushButton(self.verticalWidget_5)
        self.width_button.setObjectName(u"width_button")
        self.width_button.setMinimumSize(QSize(150, 60))
        self.width_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.verticalLayout_7.addWidget(self.width_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addWidget(self.verticalWidget_5, 2, 4, 1, 2)

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(170, 100))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 40))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.parking_margin_button = QPushButton(self.verticalFrame)
        self.parking_margin_button.setObjectName(u"parking_margin_button")
        self.parking_margin_button.setMinimumSize(QSize(150, 60))
        self.parking_margin_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.verticalLayout_2.addWidget(self.parking_margin_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.verticalFrame, 2, 2, 1, 2)

        self.verticalWidget_2 = QWidget(self.centralwidget)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setMinimumSize(QSize(170, 100))
        self.verticalWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 40))
        self.label_2.setMaximumSize(QSize(999999, 40))
        self.label_2.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.plastic_len_finished_label = QLabel(self.verticalWidget_2)
        self.plastic_len_finished_label.setObjectName(u"plastic_len_finished_label")
        self.plastic_len_finished_label.setMinimumSize(QSize(150, 60))
        self.plastic_len_finished_label.setMaximumSize(QSize(16777215, 40))
        self.plastic_len_finished_label.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.plastic_len_finished_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.plastic_len_finished_label)


        self.gridLayout_2.addWidget(self.verticalWidget_2, 0, 2, 1, 2)

        self.verticalWidget_3 = QWidget(self.centralwidget)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setMinimumSize(QSize(170, 100))
        self.verticalLayout = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 40))
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setStyleSheet(u"font: 22pt \"Furore\";\n"
"color: #38A962;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.user_speed_s2_button = QPushButton(self.verticalWidget_3)
        self.user_speed_s2_button.setObjectName(u"user_speed_s2_button")
        self.user_speed_s2_button.setMinimumSize(QSize(150, 60))
        self.user_speed_s2_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.verticalLayout.addWidget(self.user_speed_s2_button)


        self.gridLayout_2.addWidget(self.verticalWidget_3, 0, 4, 1, 2)

        self.button_001 = QPushButton(self.centralwidget)
        self.button_001.setObjectName(u"button_001")
        self.button_001.setMinimumSize(QSize(50, 60))
        self.button_001.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.button_001, 4, 4, 1, 1)

        self.button_01 = QPushButton(self.centralwidget)
        self.button_01.setObjectName(u"button_01")
        self.button_01.setMinimumSize(QSize(50, 60))
        self.button_01.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.button_01, 4, 3, 1, 1)

        self.park_button = QPushButton(self.centralwidget)
        self.park_button.setObjectName(u"park_button")
        self.park_button.setMinimumSize(QSize(100, 60))
        self.park_button.setStyleSheet(u"background-color: #38A962;\n"
"font: 22pt \"Furore\";\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 7px;")

        self.gridLayout_2.addWidget(self.park_button, 8, 2, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.right_detector_button.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.minus_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.left_detector_button.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u043e \u043c", None))
        self.len_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0456\u0430\u043c\u0435\u0442\u0440 \u043c\u043c", None))
        self.diametr_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043c\u043c", None))
        self.width_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442 \u0412\u0456\u0434\u0441\u0442\u0443\u043f \u043c\u043c", None))
        self.parking_margin_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043a\u0442\u0438\u0447\u043d\u0456 \u041c", None))
        self.plastic_len_finished_label.setText(QCoreApplication.translate("MainWindow", u"0 \u041c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0432\u0438\u0434\u043a\u0456\u0441\u0442\u044c k", None))
        self.user_speed_s2_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_001.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.button_01.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.park_button.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0440\u043a", None))
    # retranslateUi

