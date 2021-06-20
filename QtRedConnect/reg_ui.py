# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(323, 412)
        self.registration_groupbox = QGroupBox(Dialog)
        self.registration_groupbox.setObjectName(u"registration_groupbox")
        self.registration_groupbox.setGeometry(QRect(10, 140, 301, 251))
        self.registraion_buttom = QPushButton(self.registration_groupbox)
        self.registraion_buttom.setObjectName(u"registraion_buttom")
        self.registraion_buttom.setGeometry(QRect(0, 210, 301, 41))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(14)
        self.registraion_buttom.setFont(font)
        self.registraion_buttom.setStyleSheet(u"QPushButton{\n"
"background:rgba(220,220,220,0.3);\n"
"color:black;\n"
"margin:1px;\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"background:rgb(228,70,65);\n"
"font-weight:bold;\n"
"}")
        self.registraion_buttom.setIconSize(QSize(21, 21))
        self.registration_label = QLabel(self.registration_groupbox)
        self.registration_label.setObjectName(u"registration_label")
        self.registration_label.setGeometry(QRect(0, 0, 431, 51))
        self.registration_label.setFont(font)
        self.registration_label.setStyleSheet(u"QLabel{\n"
"background:rgba(220,220,220,0.6);\n"
"color:black;\n"
"margin:1px;\n"
"}")
        self.registration_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.login_registration_label = QLabel(self.registration_groupbox)
        self.login_registration_label.setObjectName(u"login_registration_label")
        self.login_registration_label.setGeometry(QRect(20, 60, 61, 31))
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(12)
        self.login_registration_label.setFont(font1)
        self.password_registration_label = QLabel(self.registration_groupbox)
        self.password_registration_label.setObjectName(u"password_registration_label")
        self.password_registration_label.setGeometry(QRect(20, 130, 61, 31))
        self.password_registration_label.setFont(font1)
        self.login_registration_LineEdit = QLineEdit(self.registration_groupbox)
        self.login_registration_LineEdit.setObjectName(u"login_registration_LineEdit")
        self.login_registration_LineEdit.setGeometry(QRect(30, 90, 341, 31))
        self.login_registration_LineEdit.setFont(font1)
        self.login_registration_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.password_registration_LineEdit = QLineEdit(self.registration_groupbox)
        self.password_registration_LineEdit.setObjectName(u"password_registration_LineEdit")
        self.password_registration_LineEdit.setGeometry(QRect(30, 160, 341, 31))
        self.password_registration_LineEdit.setFont(font1)
        self.password_registration_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.decoration_password_registration_widget = QWidget(self.registration_groupbox)
        self.decoration_password_registration_widget.setObjectName(u"decoration_password_registration_widget")
        self.decoration_password_registration_widget.setGeometry(QRect(30, 180, 241, 16))
        self.decoration_password_registration_widget.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin: 7px, 4px, 0px, 0px;\n"
"}")
        self.decoration_login_registration_widget = QWidget(self.registration_groupbox)
        self.decoration_login_registration_widget.setObjectName(u"decoration_login_registration_widget")
        self.decoration_login_registration_widget.setGeometry(QRect(30, 110, 241, 16))
        self.decoration_login_registration_widget.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin:8px, 3px, 0px, 0px;\n"
"}")
        self.main_label_registration = QLabel(Dialog)
        self.main_label_registration.setObjectName(u"main_label_registration")
        self.main_label_registration.setGeometry(QRect(90, 90, 141, 51))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.main_label_registration.setFont(font2)
        self.logo = QLabel(Dialog)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(110, 10, 100, 100))
        self.logo.setMinimumSize(QSize(100, 100))
        self.logo.setMaximumSize(QSize(100, 100))
        self.logo.setPixmap(QPixmap(u"ico/logo.png"))
        self.main_label_registration_2 = QLabel(Dialog)
        self.main_label_registration_2.setObjectName(u"main_label_registration_2")
        self.main_label_registration_2.setGeometry(QRect(340, 150, 141, 51))
        self.main_label_registration_2.setFont(font2)
        self.logo_2 = QLabel(Dialog)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(360, 70, 100, 100))
        self.logo_2.setMinimumSize(QSize(100, 100))
        self.logo_2.setMaximumSize(QSize(100, 100))
        self.logo_2.setPixmap(QPixmap(u"ico/logo.png"))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.registration_groupbox.setTitle("")
        self.registraion_buttom.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.registration_label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.login_registration_label.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password_registration_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_registration_LineEdit.setText("")
        self.password_registration_LineEdit.setText("")
        self.main_label_registration.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.logo.setText("")
        self.main_label_registration_2.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.logo_2.setText("")
    # retranslateUi

