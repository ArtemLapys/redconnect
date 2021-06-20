# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainRedConnect(object):
    def setupUi(self, mainRedConnect):
        if not mainRedConnect.objectName():
            mainRedConnect.setObjectName(u"mainRedConnect")
        mainRedConnect.resize(900, 640)
        mainRedConnect.setMinimumSize(QSize(200, 200))
        mainRedConnect.setMaximumSize(QSize(960, 640))
        self.bg_widget_account = QWidget(mainRedConnect)
        self.bg_widget_account.setObjectName(u"bg_widget_account")
        self.bg_widget_account.setGeometry(QRect(-10, -10, 911, 71))
        font = QFont()
        font.setFamily(u"Open Sans")
        self.bg_widget_account.setFont(font)
        self.bg_widget_account.setStyleSheet(u"QWidget{\n"
"background:silver;\n"
"color:black;\n"
"}")
        self.bg_groupbox_wigdet = QGroupBox(self.bg_widget_account)
        self.bg_groupbox_wigdet.setObjectName(u"bg_groupbox_wigdet")
        self.bg_groupbox_wigdet.setGeometry(QRect(0, -10, 911, 101))
        self.registration_button_account = QPushButton(self.bg_groupbox_wigdet)
        self.registration_button_account.setObjectName(u"registration_button_account")
        self.registration_button_account.setGeometry(QRect(570, 30, 161, 41))
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(12)
        self.registration_button_account.setFont(font1)
        self.registration_button_account.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background:rgba(228,70,65,0.8);\n"
"border:0;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:black;\n"
"background:rgb(228,70,65);\n"
"border-color:black;\n"
"border:1px  solid black;\n"
"font-weight:bold;\n"
"}")
        icon = QIcon()
        icon.addFile(u"ico/registrationNEW.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registration_button_account.setIcon(icon)
        self.registration_button_account.setIconSize(QSize(20, 20))
        self.logiIn_button_account = QPushButton(self.bg_groupbox_wigdet)
        self.logiIn_button_account.setObjectName(u"logiIn_button_account")
        self.logiIn_button_account.setGeometry(QRect(740, 30, 161, 41))
        self.logiIn_button_account.setFont(font1)
        self.logiIn_button_account.setAutoFillBackground(False)
        self.logiIn_button_account.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background:rgba(228,70,65,0.8);\n"
"border:0;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:black;\n"
"background:rgb(228,70,65);\n"
"border-color:black;\n"
"border:1px  solid black;\n"
"font-weight:bold;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"ico/loginIN.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logiIn_button_account.setIcon(icon1)
        self.logiIn_button_account.setIconSize(QSize(22, 22))
        self.name_account = QLabel(self.bg_groupbox_wigdet)
        self.name_account.setObjectName(u"name_account")
        self.name_account.setGeometry(QRect(30, 20, 431, 31))
        font2 = QFont()
        font2.setFamily(u"Open Sans")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.name_account.setFont(font2)
        self.welcome_label_account = QLabel(self.bg_groupbox_wigdet)
        self.welcome_label_account.setObjectName(u"welcome_label_account")
        self.welcome_label_account.setGeometry(QRect(40, 50, 421, 20))
        self.welcome_label_account.setFont(font1)
        self.menu_widget = QWidget(mainRedConnect)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setGeometry(QRect(540, 60, 361, 601))
        self.menu_widget.setStyleSheet(u"QWidget{\n"
"color:black;\n"
"\n"
"}")
        self.menu_groupBox = QGroupBox(self.menu_widget)
        self.menu_groupBox.setObjectName(u"menu_groupBox")
        self.menu_groupBox.setGeometry(QRect(0, -10, 361, 591))
        self.connect_to_desktop_button = QPushButton(self.menu_groupBox)
        self.connect_to_desktop_button.setObjectName(u"connect_to_desktop_button")
        self.connect_to_desktop_button.setGeometry(QRect(0, 10, 361, 51))
        self.connect_to_desktop_button.setFont(font1)
        self.connect_to_desktop_button.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"ico/desktopconnect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_to_desktop_button.setIcon(icon2)
        self.connect_to_desktop_button.setIconSize(QSize(22, 22))
        self.connect_to_terminal_button = QPushButton(self.menu_groupBox)
        self.connect_to_terminal_button.setObjectName(u"connect_to_terminal_button")
        self.connect_to_terminal_button.setGeometry(QRect(0, 60, 361, 51))
        self.connect_to_terminal_button.setFont(font1)
        self.connect_to_terminal_button.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"ico/terminalconnect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_to_terminal_button.setIcon(icon3)
        self.connect_to_terminal_button.setIconSize(QSize(22, 22))
        self.mydata_groupbox = QGroupBox(self.menu_groupBox)
        self.mydata_groupbox.setObjectName(u"mydata_groupbox")
        self.mydata_groupbox.setGeometry(QRect(10, 320, 341, 261))
        self.mydata_label = QLabel(self.mydata_groupbox)
        self.mydata_label.setObjectName(u"mydata_label")
        self.mydata_label.setGeometry(QRect(0, 0, 341, 51))
        font3 = QFont()
        font3.setFamily(u"Open Sans")
        font3.setPointSize(14)
        self.mydata_label.setFont(font3)
        self.mydata_label.setStyleSheet(u"QLabel{\n"
"background:rgba(220,220,220,0.6);\n"
"color:black;\n"
"margin:1px;\n"
"}")
        self.mydata_label.setAlignment(Qt.AlignCenter)
        self.login_mydata_label = QLabel(self.mydata_groupbox)
        self.login_mydata_label.setObjectName(u"login_mydata_label")
        self.login_mydata_label.setGeometry(QRect(20, 50, 61, 31))
        self.login_mydata_label.setFont(font1)
        self.password_mydata_label = QLabel(self.mydata_groupbox)
        self.password_mydata_label.setObjectName(u"password_mydata_label")
        self.password_mydata_label.setGeometry(QRect(20, 120, 61, 31))
        self.password_mydata_label.setFont(font1)
        self.password_mydata_LineEdit = QLineEdit(self.mydata_groupbox)
        self.password_mydata_LineEdit.setObjectName(u"password_mydata_LineEdit")
        self.password_mydata_LineEdit.setEnabled(False)
        self.password_mydata_LineEdit.setGeometry(QRect(30, 150, 261, 31))
        self.password_mydata_LineEdit.setFont(font1)
        self.password_mydata_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.login_mydata_LineEdit = QLineEdit(self.mydata_groupbox)
        self.login_mydata_LineEdit.setObjectName(u"login_mydata_LineEdit")
        self.login_mydata_LineEdit.setEnabled(False)
        self.login_mydata_LineEdit.setGeometry(QRect(30, 80, 261, 31))
        self.login_mydata_LineEdit.setFont(font1)
        self.login_mydata_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.update_data_mydata_button = QPushButton(self.mydata_groupbox)
        self.update_data_mydata_button.setObjectName(u"update_data_mydata_button")
        self.update_data_mydata_button.setGeometry(QRect(0, 220, 341, 41))
        self.update_data_mydata_button.setFont(font3)
        self.update_data_mydata_button.setStyleSheet(u"QPushButton{\n"
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
        icon4 = QIcon()
        icon4.addFile(u"ico/updatedata.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_data_mydata_button.setIcon(icon4)
        self.update_data_mydata_button.setIconSize(QSize(22, 22))
        self.decoration_password_mydata_widget = QWidget(self.mydata_groupbox)
        self.decoration_password_mydata_widget.setObjectName(u"decoration_password_mydata_widget")
        self.decoration_password_mydata_widget.setGeometry(QRect(30, 170, 261, 16))
        self.decoration_password_mydata_widget.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin: 7px, 4px, 0px, 0px;\n"
"}")
        self.decoration_login_mydata_widget = QWidget(self.mydata_groupbox)
        self.decoration_login_mydata_widget.setObjectName(u"decoration_login_mydata_widget")
        self.decoration_login_mydata_widget.setGeometry(QRect(30, 100, 261, 16))
        self.decoration_login_mydata_widget.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin:8px, 3px, 0px, 0px;\n"
"}")
        self.connect_to_chat_button = QPushButton(self.menu_groupBox)
        self.connect_to_chat_button.setObjectName(u"connect_to_chat_button")
        self.connect_to_chat_button.setGeometry(QRect(0, 210, 361, 51))
        self.connect_to_chat_button.setFont(font1)
        self.connect_to_chat_button.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"ico/connectchat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_to_chat_button.setIcon(icon5)
        self.connect_to_chat_button.setIconSize(QSize(24, 24))
        self.information_button = QPushButton(self.menu_groupBox)
        self.information_button.setObjectName(u"information_button")
        self.information_button.setGeometry(QRect(0, 260, 361, 51))
        self.information_button.setFont(font1)
        self.information_button.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"ico/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.information_button.setIcon(icon6)
        self.information_button.setIconSize(QSize(22, 22))
        self.usb_button = QPushButton(self.menu_groupBox)
        self.usb_button.setObjectName(u"usb_button")
        self.usb_button.setGeometry(QRect(0, 160, 361, 51))
        self.usb_button.setFont(font1)
        self.usb_button.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"ico/usbconnect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usb_button.setIcon(icon7)
        self.usb_button.setIconSize(QSize(25, 25))
        self.usb_button_2 = QPushButton(self.menu_groupBox)
        self.usb_button_2.setObjectName(u"usb_button_2")
        self.usb_button_2.setGeometry(QRect(0, 110, 361, 51))
        self.usb_button_2.setFont(font1)
        self.usb_button_2.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:gainsboro;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"ico/command.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usb_button_2.setIcon(icon8)
        self.usb_button_2.setIconSize(QSize(18, 18))
        self.main_label = QLabel(mainRedConnect)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(30, 70, 431, 41))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.main_label.setFont(font4)
        self.external_connection_groupbox = QGroupBox(mainRedConnect)
        self.external_connection_groupbox.setObjectName(u"external_connection_groupbox")
        self.external_connection_groupbox.setGeometry(QRect(40, 120, 431, 251))
        self.pushButton = QPushButton(self.external_connection_groupbox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 210, 431, 41))
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u"ico/connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(21, 21))
        self.external_connection_label = QLabel(self.external_connection_groupbox)
        self.external_connection_label.setObjectName(u"external_connection_label")
        self.external_connection_label.setGeometry(QRect(0, 0, 431, 51))
        self.external_connection_label.setFont(font3)
        self.external_connection_label.setStyleSheet(u"QLabel{\n"
"background:rgba(220,220,220,0.6);\n"
"color:black;\n"
"margin:1px;\n"
"}")
        self.external_connection_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.login_extrernal_connection_label = QLabel(self.external_connection_groupbox)
        self.login_extrernal_connection_label.setObjectName(u"login_extrernal_connection_label")
        self.login_extrernal_connection_label.setGeometry(QRect(30, 60, 61, 31))
        self.login_extrernal_connection_label.setFont(font1)
        self.password_extrernal_connection_label = QLabel(self.external_connection_groupbox)
        self.password_extrernal_connection_label.setObjectName(u"password_extrernal_connection_label")
        self.password_extrernal_connection_label.setGeometry(QRect(30, 130, 61, 31))
        self.password_extrernal_connection_label.setFont(font1)
        self.login_extrernal_connection_LineEdit = QLineEdit(self.external_connection_groupbox)
        self.login_extrernal_connection_LineEdit.setObjectName(u"login_extrernal_connection_LineEdit")
        self.login_extrernal_connection_LineEdit.setGeometry(QRect(40, 90, 341, 31))
        self.login_extrernal_connection_LineEdit.setFont(font1)
        self.login_extrernal_connection_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.password_extrernal_connection_LineEdit = QLineEdit(self.external_connection_groupbox)
        self.password_extrernal_connection_LineEdit.setObjectName(u"password_extrernal_connection_LineEdit")
        self.password_extrernal_connection_LineEdit.setGeometry(QRect(40, 160, 341, 31))
        self.password_extrernal_connection_LineEdit.setFont(font1)
        self.password_extrernal_connection_LineEdit.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"color:black;\n"
" border:0px;\n"
"}")
        self.decoration_password_external_connection_widget = QWidget(self.external_connection_groupbox)
        self.decoration_password_external_connection_widget.setObjectName(u"decoration_password_external_connection_widget")
        self.decoration_password_external_connection_widget.setGeometry(QRect(40, 180, 341, 16))
        self.decoration_password_external_connection_widget.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin: 7px, 4px, 0px, 0px;\n"
"}")
        self.decoration_login_external_connection_widget = QWidget(self.external_connection_groupbox)
        self.decoration_login_external_connection_widget.setObjectName(u"decoration_login_external_connection_widget")
        self.decoration_login_external_connection_widget.setGeometry(QRect(40, 110, 341, 16))
        self.decoration_login_external_connection_widget.setStyleSheet(u"QWidget{\n"
"background: rgb(228,70,65);\n"
"margin:8px, 3px, 0px, 0px;\n"
"}")
        self.seans_main_label_ = QLabel(mainRedConnect)
        self.seans_main_label_.setObjectName(u"seans_main_label_")
        self.seans_main_label_.setGeometry(QRect(40, 380, 431, 41))
        self.seans_main_label_.setFont(font4)
        self.seans_main_label_.setStyleSheet(u"QLabel{\n"
"color:black;\n"
"}")
        self.image_last_seanse1 = QLabel(mainRedConnect)
        self.image_last_seanse1.setObjectName(u"image_last_seanse1")
        self.image_last_seanse1.setGeometry(QRect(50, 420, 200, 200))
        self.image_last_seanse1.setMinimumSize(QSize(200, 200))
        self.image_last_seanse1.setMaximumSize(QSize(200, 200))
        self.image_last_seanse1.setAutoFillBackground(False)
        self.image_last_seanse1.setStyleSheet(u"QLabel{\n"
"border: 1px solid lightgray;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border: 2px solid black;\n"
"}")
        self.image_last_seanse1.setScaledContents(True)
        self.image_last_seanse2 = QLabel(mainRedConnect)
        self.image_last_seanse2.setObjectName(u"image_last_seanse2")
        self.image_last_seanse2.setGeometry(QRect(290, 420, 200, 200))
        self.image_last_seanse2.setMinimumSize(QSize(200, 200))
        self.image_last_seanse2.setMaximumSize(QSize(200, 200))
        self.image_last_seanse2.setStyleSheet(u"QLabel{\n"
"border: 1px solid lightgray;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border: 2px solid black;\n"
"}")
        self.image_last_seanse2.setScaledContents(True)
        self.image_last_seanse2.setWordWrap(False)

        self.retranslateUi(mainRedConnect)

        QMetaObject.connectSlotsByName(mainRedConnect)
    # setupUi

    def retranslateUi(self, mainRedConnect):
        mainRedConnect.setWindowTitle(QCoreApplication.translate("mainRedConnect", u"mainRedConnect", None))
        self.bg_groupbox_wigdet.setTitle(QCoreApplication.translate("mainRedConnect", u"GroupBox", None))
        self.registration_button_account.setText(QCoreApplication.translate("mainRedConnect", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.logiIn_button_account.setText(QCoreApplication.translate("mainRedConnect", u"\u0412\u0445\u043e\u0434", None))
        self.name_account.setText(QCoreApplication.translate("mainRedConnect", u"\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.welcome_label_account.setText(QCoreApplication.translate("mainRedConnect", u"\u041c\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u043b\u0438\u0441\u044c! \u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.menu_groupBox.setTitle("")
        self.connect_to_desktop_button.setText(QCoreApplication.translate("mainRedConnect", u" \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0440\u0430\u0431\u043e\u0447\u0435\u043c\u0443 \u0441\u0442\u043e\u043b\u0443", None))
        self.connect_to_terminal_button.setText(QCoreApplication.translate("mainRedConnect", u" \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0443", None))
        self.mydata_groupbox.setTitle("")
        self.mydata_label.setText(QCoreApplication.translate("mainRedConnect", u"\u041c\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.login_mydata_label.setText(QCoreApplication.translate("mainRedConnect", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password_mydata_label.setText(QCoreApplication.translate("mainRedConnect", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_mydata_LineEdit.setText("")
        self.login_mydata_LineEdit.setText("")
        self.update_data_mydata_button.setText(QCoreApplication.translate("mainRedConnect", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.connect_to_chat_button.setText(QCoreApplication.translate("mainRedConnect", u" \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0447\u0430\u0442\u0443", None))
        self.information_button.setText(QCoreApplication.translate("mainRedConnect", u" \u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.usb_button.setText(QCoreApplication.translate("mainRedConnect", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a USB", None))
        self.usb_button_2.setText(QCoreApplication.translate("mainRedConnect", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0434\u043b\u044f \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430", None))
        self.main_label.setText(QCoreApplication.translate("mainRedConnect", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u043d\u044b\u043c \u0434\u043e\u0441\u0442\u0443\u043f\u043e\u043c", None))
        self.external_connection_groupbox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("mainRedConnect", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.external_connection_label.setText(QCoreApplication.translate("mainRedConnect", u"  \u0412\u043d\u0435\u0448\u043d\u0435\u0435 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.login_extrernal_connection_label.setText(QCoreApplication.translate("mainRedConnect", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password_extrernal_connection_label.setText(QCoreApplication.translate("mainRedConnect", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_extrernal_connection_LineEdit.setText("")
        self.password_extrernal_connection_LineEdit.setText("")
        self.seans_main_label_.setText(QCoreApplication.translate("mainRedConnect", u"\u041d\u0435\u0434\u0430\u0432\u043d\u0438\u0435 \u0441\u0435\u0430\u043d\u0441\u044b", None))
        self.image_last_seanse1.setText("")
        self.image_last_seanse2.setText("")
    # retranslateUi

