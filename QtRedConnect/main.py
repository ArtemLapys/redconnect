import sys
import os
import autorization
from PySide2 import QtWidgets
from main_ui import Ui_mainRedConnect
from reg_ui import Ui_Dialog
from login_ui import Ui_login_Dialog
from Connect import start_sec
import Terminal
import socket
import pyautogui

global userName
userName = str()
global userPassword
userPassword = str()
global userId
userId = int(0)
global keyJoin
keyJoin = str()
global lastKeyJoin
lastKeyJoin = str()




class MainClass(QtWidgets.QMainWindow, Ui_mainRedConnect):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.registration_button_account.clicked.connect(self.open_Dialog)
        self.logiIn_button_account.clicked.connect(self.open_Login)
        self.dialog = Registration()
        self.dialog_login = Login()

        self.pushButton.clicked.connect(self.connect_to_client)
        self.connect_to_terminal_button.clicked.connect(self.changeto2)
        self.connect_to_desktop_button.clicked.connect(self.changeto0)
        self.connect_to_chat_button.clicked.connect(self.changeto3)
        self.name_account.setText("Неизвестный пользователь")


        self.checkbox = 0
        self.check_bg_menu()

    def connect(self, ip):
          sock = socket.socket()
          sock.connect((ip,9096))
          data = sock.recv(1024).decode()
          check = data



    def changeto0(self):
        self.checkbox = 0
    def changeto1(self):
        self.checkbox = 1
    def changeto2(self):
        self.checkbox = 2
    def changeto3(self):
        self.checkbox = 3
    def changeto4(self):
        self.checkbox = 4

    def connect_to_client(self):
        if self.checkbox == 0:
            #self.connect(self.login_extrernal_connection_LineEdit.text())
            image = start_sec(self.login_extrernal_connection_LineEdit.text(), "2")
            self.check_bg_menu()
            screen = pyautogui.screenshoot()
            self.ui.image_last_seanse.setPixmap(screen)
        elif self.checkbox == 1:
            pass
        elif self.checkbox == 2:
            #temp = 'python Terminal.py --ip ' + self.login_extrernal_connection_LineEdit.text() + ' --user root --password ' + self.password_extrernal_connection_LineEdit.text()
            #os.system("mate-terminal -e \'\'")
            self.check_bg_menu()
            ip = self.login_extrernal_connection_LineEdit.text()
            password = self.password_extrernal_connection_LineEdit.text()
            os.system("mate-terminal -e 'python3 Terminal.py --ip " + ip + " --user root --password " + password+ "'")
        elif self.checkbox == 3:
            self.check_bg_menu()
            pass


    def open_Dialog(self):
        self.dialog.show()

    def open_Login(self):
        self.dialog_login.show()

    def check_bg_menu(self):
        pass
        #if self.checkbox == 0:
        #    self.connect_to_desktop_button.setStyleSheet('background:gainsboro;')
         #   self.connect_to_terminal_button.setStyleSheet('background:transparent;')
          #  self.usb_button_2.setStyleSheet('background:transparent;')
        #    self.usb_button.setStyleSheet('background:transparent;')
         #   self.connect_to_chat_button.setStyleSheet('background:transparent;')
      #  elif self.checkbox ==1:
         #   self.connect_to_desktop_button.setStyleSheet('background:transparent;')
      #      self.connect_to_terminal_button.setStyleSheet('background:gainsboro;')
        #    self.usb_button_2.setStyleSheet('background:transparent;')
          #  self.usb_button.setStyleSheet('background:transparent;')
         #   self.connect_to_chat_button.setStyleSheet('background:transparent;')









class Registration(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registraion_buttom.clicked.connect(self.Autorize)

    def Autorize(self):
        global userName
        userName = self.login_registration_LineEdit.text()
        global userPasswordr
        userPassword = self.password_registration_LineEdit.text()
        result = autorization.send_register(userName, userPassword, 44)
        if result[:4] == 'id: ':
                getting = result.split(' | ')
                for elem in getting:
                        item = elem.split(': ')
                        if item[0] == 'id':
                                userId = int(item[1])
                        elif item[0] == 'keyJoin':
                                keyJoin = item[1]
                        elif item[0] == 'LastKeyJoin':
                                lastKeyJoin = item[1]
                print('%d %s %s' % (userId, keyJoin, lastKeyJoin))

        elif result == 'ConnectError':
                self.registration_label.setText("Ошибка подключения.")
        elif result == 'UserError':
                self.registration_label.setText("Ошибка. Пользователь существует.")
        elif result == 'AutorizationError':
                self.registration_label.setText("Ошибка авторизации!")
        elif result == 'RegisterError':
                self.registration_label.setText("Ошибка при регистрации!")
        elif result == 'RegisterSucces':
                self.registration_label.setText("Регистрация успешна!")
                MainClass.name_account.setText(userName)
        else:
                self.registration_label.setText("Неизвестная ошибка!")





class Login(QtWidgets.QMainWindow, Ui_login_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_buttom.clicked.connect(self.Login)

    def Login(self):
        global userName
        userName = self.login_login_LineEdit.text()
        global userPasswordr
        userPassword = self.password_login_LineEdit.text()
        result = autorization.send_login(userName, userPassword)
        if result[:4] == 'id: ':
                getting = result.split(' | ')
                for elem in getting:
                        item = elem.split(': ')
                        if item[0] == 'id':
                                userId = int(item[1])
                        elif item[0] == 'keyJoin':
                                keyJoin = item[1]
                        elif item[0] == 'LastKeyJoin':
                                lastKeyJoin = item[1]
                print('%d %s %s' % (userId, keyJoin, lastKeyJoin))
                self.login_label.setText("Вы авторизованы!")

        elif result == 'ConnectError':
                self.login_label.setText("Ошибка при подключении!")
        elif result == 'UserError':
                self.login_label.setText("Ошибка. Пользователь существует.")
        elif result == 'AutorizationError':
                self.login_label.setText("Ошибка при авторизации!")
        elif result == 'RegisterError':
                self.login_label.setText("Ошибка при регистрации!")
        elif result == 'RegisterSucces':
                self.login_label.setText("Регистрация успешна!")
        else:
                self.login_label.setText("Неизвестная ошибка!")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wnd = MainClass()
    sys.exit(app.exec_())
