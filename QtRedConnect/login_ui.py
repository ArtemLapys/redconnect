# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login_Dialog(object):
    def setupUi(self, login_Dialog):
        if not login_Dialog.objectName():
            login_Dialog.setObjectName(u"login_Dialog")
        login_Dialog.resize(320, 427)
        self.logo = QLabel(login_Dialog)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(110, 10, 100, 100))
        self.logo.setMinimumSize(QSize(100, 100))
        self.logo.setMaximumSize(QSize(100, 100))
        self.logo.setPixmap(QPixmap(u"ico/logo.png"))
        self.main_label_login = QLabel(login_Dialog)
        self.main_label_login.setObjectName(u"main_label_login")
        self.main_label_login.setGeometry(QRect(90, 110, 141, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_label_login.setFont(font)
        self.login_groupbox = QGroupBox(login_Dialog)
        self.login_groupbox.setObjectName(u"login_groupbox")
        self.login_groupbox.setGeometry(QRect(10, 160, 301, 251))
        self.login_buttom = QPushButton(self.login_groupbox)
        self.login_buttom.setObjectName(u"login_buttom")
        self.login_buttom.setGeometry(QRect(0, 210, 301, 41))
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(14)
        self.login_buttom.setFont(font1)
        self.login_buttom.setStyleSheet(u"QPushButton{\n"
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
        self.login_buttom.setIconSize(QSize(21, 21))
        self.login_label = QLabel(self.login_groupbox)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(0, 0, 431, 51))
        self.login_label.setFont(font1)
        self.login_label.setStyleSheet(u"QLabel{\n"
"background:rgba(220,220,220,0.6);\n"
"color:black;\n"
"margin:1px;\n"
"}")
        self.login_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.login_login_label = QLabel(self.login_groupbox)
        self.login_login_label.setObjectName(u"login_login_label")
        self.login_login_label.setGeometry(QRect(20, 60, 61, 31))
        font2 = QFont()
        font2.setFamily(u"Open Sans")
        font2.setPointSize(12)
        self.login_login_label.setFont(font2)
        self.password_login_label = QLabel(self.login_groupbox)
        self.password_login_label.setObjectName(u"password_login_label")
        self.password_login_label.setGeometry(QRect(20, 130, 61, 31))
        self.password_login_label.setFont(font2)
        self.login_login_LineEdit = QLineEdit(self.login_groupbox)
        self.login_login_LineEdit.setObjectName(u"login_login_LineEdit")
        self.login_login_LineEdit.setGeometry(QRect(30, 90, 341, 31))
        self.login_login_LineEdit.setFont(font2)
        self.login_login_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.password_login_LineEdit = QLineEdit(self.login_groupbox)
        self.password_login_LineEdit.setObjectName(u"password_login_LineEdit")
        self.password_login_LineEdit.setGeometry(QRect(30, 160, 341, 31))
        self.password_login_LineEdit.setFont(font2)
        self.password_login_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.decoration_password_widget_login = QWidget(self.login_groupbox)
        self.decoration_password_widget_login.setObjectName(u"decoration_password_widget_login")
        self.decoration_password_widget_login.setGeometry(QRect(30, 180, 241, 16))
        self.decoration_password_widget_login.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin: 7px, 4px, 0px, 0px;\n"
"}")
        self.decoration_login_widget_login = QWidget(self.login_groupbox)
        self.decoration_login_widget_login.setObjectName(u"decoration_login_widget_login")
        self.decoration_login_widget_login.setGeometry(QRect(30, 110, 241, 16))
        self.decoration_login_widget_login.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin:8px, 3px, 0px, 0px;\n"
"}")

        self.retranslateUi(login_Dialog)

        QMetaObject.connectSlotsByName(login_Dialog)
    # setupUi

    def retranslateUi(self, login_Dialog):
        login_Dialog.setWindowTitle(QCoreApplication.translate("login_Dialog", u"Dialog", None))
        self.logo.setText("")
        self.main_label_login.setText(QCoreApplication.translate("login_Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.login_groupbox.setTitle("")
        self.login_buttom.setText(QCoreApplication.translate("login_Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.login_label.setText(QCoreApplication.translate("login_Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.login_login_label.setText(QCoreApplication.translate("login_Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password_login_label.setText(QCoreApplication.translate("login_Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_login_LineEdit.setText("")
        self.password_login_LineEdit.setText("")
    # retranslateUi

