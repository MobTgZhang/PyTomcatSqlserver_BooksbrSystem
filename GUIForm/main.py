from PyQt5 import QtCore, QtWidgets,QtGui
import sys
from connect_db import get_user_name,get_name
import os
import json
# 重写closeEvent函数
class DialogMain(QtWidgets.QWidget):
    def closeEvent(self, a0: QtGui.QCloseEvent):
        value = QtWidgets.QMessageBox.information(None, "提示信息", "真的要退出系统吗？",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if value == QtWidgets.QMessageBox.Yes:
            a0.accept()
            app = QtWidgets.QApplication(sys.argv)
            sys.exit(app.exec_())
        else:
            a0.ignore()
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setObjectName("MainWindow")
        self.resize(559, 333)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("sublime-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 40, 161, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(self.tr("馆长"))
        self.comboBox.addItem(self.tr("管理员"))
        self.comboBox.addItem(self.tr("操作员"))
        self.comboBox.addItem(self.tr("读者"))
        self.comboBox.currentTextChanged.connect(self.user_check)

        # 用户名
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 71, 21))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 90, 161, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(False)

        # 密码
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 68, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 150, 71, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 140, 161, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        regExp = QtGui.QRegExpValidator(QtCore.QRegExp("([0-9]|[a-z]|[A-Z])*"))
        self.textEdit_2.setValidator(regExp)
        self.textEdit_2.setMaxLength(15)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 200, 101, 31))
        self.pushButton_2.setObjectName("pushButton")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 200, 101, 31))
        self.pushButton_3.setObjectName("pushButton_2")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 31))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(self)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(self)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书管理系统----欢迎"))
        self.label.setText(_translate("MainWindow", "用户选择"))
        self.label_2.setText(_translate("MainWindow", "登录名"))
        self.label_3.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "登陆"))
        self.pushButton.clicked.connect(self.log_in)
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.pushButton_2.clicked.connect(self.log_in_register)
        self.pushButton_3.setText(_translate("MainWindow", "退出"))
        self.pushButton_3.clicked.connect(self.exit_func)
        self.menu.setTitle(_translate("MainWindow", "操作"))
        self.action.setText(_translate("MainWindow", "软件信息"))
        self.action.triggered.connect(self.InforPrint)
        self.action_2.setText(_translate("MainWindow", "退出"))
        self.action_2.triggered.connect(self.exit_func)
    # 馆长
    def user_check(self):
        if self.comboBox.currentText() == "馆长":
            self.textEdit.setEnabled(False)
        else:
            self.textEdit.setEnabled(True)
    # 软件信息
    def InforPrint(self):
        from Infor import Infor_Dialog
        Form1 = QtWidgets.QDialog()
        ui = Infor_Dialog()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
    # 登陆
    def log_in(self):
        typeUser = self.comboBox.currentIndex()
        name = self.textEdit.toPlainText().strip()
        passwd = self.textEdit_2.text()
        ip_address = "192.168.43.205"
        # 检查用户名和密码是否为空
        if name == "" and self.comboBox.currentText().strip()!="馆长":
            QtWidgets.QMessageBox.warning(None,"错误提示","请输入用户名!",QtWidgets.QMessageBox.Yes)
            self.textEdit.setFocus()
            return
        else:
            if passwd.strip() == "":
                QtWidgets.QMessageBox.warning(None, "错误提示", "请输入密码!", QtWidgets.QMessageBox.Yes)
                self.textEdit_2.setFocus()
                return
        result = get_user_name(typeUser,name,passwd,ip_address)
        if result:
            QtWidgets.QMessageBox.information(None, "提示信息", "登陆成功!", QtWidgets.QMessageBox.Yes)
            # 本地生成用户的登陆信息
            path_file = "cache"
            new_dict = {
                "name":name,
                "password":passwd
            }
            if not os.path.exists(path_file):
                os.mkdir(path_file)
            with open(os.path.join(path_file,"UserLoginData.jsq"),"w") as file:
                json.dump(new_dict, file)
            # 加密用户数据
            #登陆界面的选择
            if typeUser == 3:
                self.destroy()
                from Reader_Main_Page import Reader_Dialog
                Form1 = DialogMain()
                ui = Reader_Dialog()
                ui.setupUi(Form1)
                Form1.show()
                return
            elif typeUser == 2:
                from controler import ContorlerDialog
                Form1 = DialogMain()
                ui = ContorlerDialog()
                ui.setupUi(Form1)
                Form1.show()
                Form1.exec_()
                return
            elif typeUser == 1:
                from Manager import Manager_Dialog
                Form1 = DialogMain()
                ui = Manager_Dialog()
                ui.setupUi(Form1)
                Form1.show()
                Form1.exec_()
                return
            else:
                from Director import Director_Dialog
                Form1 = DialogMain()
                ui = Director_Dialog()
                ui.setupUi(Form1)
                Form1.show()
                Form1.exec_()
                return
        else:
            QtWidgets.QMessageBox.warning(None, "提示信息", "登陆失败,请检查用户名和密码是否正确!", QtWidgets.QMessageBox.Yes)
    # 注册
    def log_in_register(self):
        from regiter import Register_Dialog
        Form1 = QtWidgets.QDialog()
        ui = Register_Dialog()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
    # 退出系统
    def exit_func(self):
         sys.exit(app.exec_())
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())