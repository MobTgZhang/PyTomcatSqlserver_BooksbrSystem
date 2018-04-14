from PyQt5 import QtCore, QtGui, QtWidgets
from Clock import Clock
import datetime
import requests
from connect_db import get_user_basic_data,alter_data
import os
import json
import pandas as pd
import time
import re

class Reader_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 444)
        Dialog.destroyed.connect(self.exit_func)
        # 读者信息
        self.ButtonReaderInfor = QtWidgets.QPushButton(Dialog)
        self.ButtonReaderInfor.setGeometry(QtCore.QRect(30, 30, 121, 41))
        self.ButtonReaderInfor.setObjectName("ButtonReaderInfor")
        self.ButtonReaderInfor.clicked.connect(self.print_reader)
        # 图书的借还信息
        self.borrowInfor = QtWidgets.QPushButton(Dialog)
        self.borrowInfor.setGeometry(QtCore.QRect(30, 80, 121, 41))
        self.borrowInfor.setObjectName("borrowInfor")
        self.borrowInfor.clicked.connect(self.print_borrow)
        # 图书的归还操作
        self.borrowbutton = QtWidgets.QPushButton(Dialog)
        self.borrowbutton.setGeometry(QtCore.QRect(30, 130, 121, 41))
        self.borrowbutton.setObjectName("borrowbutton")
        self.borrowbutton.clicked.connect(self.QueryPrint)
        # 摘要笔记
        self.NoteBook = QtWidgets.QPushButton(Dialog)
        self.NoteBook.setGeometry(QtCore.QRect(30, 180, 121, 41))
        self.NoteBook.setObjectName("NoteBook")
        self.NoteBook.clicked.connect(self.book_note)
        # 退出按钮
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(500, 380, 121, 41))
        self.ExitButton.setObjectName("ExitButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.ExitButton.clicked.connect(lambda :self.exit_func(Dialog))
        # 日历框架图
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 40, 456, 178))
        self.calendarWidget.setObjectName("calendarWidget")
        # 显示日期和时间
        self.TD_label = QtWidgets.QLabel(Dialog)
        self.TD_label.setGeometry(QtCore.QRect(400, 220, 150, 30))
        self.TD_label.setObjectName("label_date")
        self.TD_label.setText("登陆时间")
        self.label_date = QtWidgets.QLabel(Dialog)
        self.label_date.setGeometry(QtCore.QRect(400, 260, 180, 30))
        self.label_date.setObjectName("label_date")
        today = datetime.date.today()
        self.label_date.setText(" 日期:%d年 %d月 %d日" % (today.year, today.month, today.day))
        self.label_time = QtWidgets.QLabel(Dialog)
        self.label_time.setGeometry(QtCore.QRect(400, 300, 150, 30))
        self.label_time.setObjectName("label_time")
        timeNow = datetime.datetime.now()
        self.label_time.setText(" 时间:%d时 %d分 %d秒" % (timeNow.hour, timeNow.minute, timeNow.second))

        # 时钟的框架图
        self.widget = Clock(Dialog)
        self.widget.initUI()
        self.widget.setGeometry(QtCore.QRect(150, 230, 341, 211))
        self.widget.setObjectName("widget")
        self.widget.setFixedSize(250, 230)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "读者主界面"))
        self.ButtonReaderInfor.setText(_translate("Dialog", "查看读者信息"))
        self.borrowInfor.setText(_translate("Dialog", "查看借阅与归还"))
        self.borrowbutton.setText(_translate("Dialog", "图书查询与借阅"))
        self.NoteBook.setText(_translate("Dialog", "读书摘要笔记"))
        self.ExitButton.setText(_translate("Dialog", "退出系统"))
    # 退出系统
    def exit_func(self,Dialog):
        Dialog.close()
    # 显示读者信息
    def print_reader(self):
        try:
            ip_address = "192.168.43.205"
            result = get_user_basic_data(4,ip_address)
            time.sleep(0.5)
            if result:
                Form1 = QtWidgets.QWidget()
                ui = ReaderInformation_Dialog()
                ui.setupUi(Form1)
                Form1.show()
                Form1.exec_()
            else:
                QtWidgets.QMessageBox.warning(None,"错误提示","读者信息读取失败！")
        except requests.ConnectionError:
            QtWidgets.QMessageBox.warning(None,"错误提示","网络连接错误，请检查网络连接状况!")
    # 查看借阅信息
    def print_borrow(self):
        try:
            ip_address = "192.168.43.205"
            # 查看借阅信息的函数
            # 连接数据库查阅借阅信息
            time.sleep(0.5)
            if True:  # result:
                # 将服务器端发送过来的信息缓存到本地的缓存文件夹中
                with open("ReaderBorrowInfo.json","w",encoding="utf-8") as file:
                    pass
                Form1 = QtWidgets.QWidget()
                ui = ViewBorrowDialog()
                ui.setupUi(Form1)
                Form1.show()
                Form1.exec_()
            else:
                QtWidgets.QMessageBox.warning(None, "错误提示", "读者信息读取失败！")
        except requests.ConnectionError:
            QtWidgets.QMessageBox.warning(None, "错误提示", "网络连接错误，请检查网络连接状况!")
    #读书摘要笔记
    def book_note(self):
        Form1 = QtWidgets.QWidget()
        ui = BookNote()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
    #读者借阅与查询
    def QueryPrint(self):
        Form1 = QtWidgets.QWidget()
        ui = BookBorrowQuery()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
# 读者信息界面
class ReaderInformation_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 609)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 20, 481, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # 姓名
        self.LABEL_NAME = QtWidgets.QLabel(self.frame)
        self.LABEL_NAME.setGeometry(QtCore.QRect(50, 30, 121, 41))
        self.LABEL_NAME.setObjectName("LABEL_NAME")
        self.NAME = QtWidgets.QTextEdit(self.frame)
        self.NAME.setGeometry(QtCore.QRect(190, 30, 191, 41))
        self.NAME.setObjectName("NAME")
        # 年龄
        self.LABEL_AGE = QtWidgets.QLabel(self.frame)
        self.LABEL_AGE.setGeometry(QtCore.QRect(50, 80, 121, 41))
        self.LABEL_AGE.setObjectName("LABEL_AGE")
        self.AGE = QtWidgets.QLineEdit(self.frame)
        self.AGE.setGeometry(QtCore.QRect(190, 80, 191, 41))
        self.AGE.setObjectName("AGE")
        RegExp = QtGui.QRegExpValidator(QtCore.QRegExp("([0-9])*"))
        self.AGE.setMaxLength(2)
        self.AGE.setValidator(RegExp)
        #登录名
        self.LABEL_LOGNAME = QtWidgets.QLabel(self.frame)
        self.LABEL_LOGNAME.setGeometry(QtCore.QRect(50, 330, 121, 41))
        self.LABEL_LOGNAME.setObjectName("LABEL_LOGNAME")
        self.LOG_NAME = QtWidgets.QLineEdit(self.frame)
        self.LOG_NAME.setGeometry(QtCore.QRect(190, 330, 191, 41))
        self.LOG_NAME.setObjectName("LOG_NAME")
        regExp = QtGui.QRegExpValidator(QtCore.QRegExp("([A-Z]|[a-z]|[0-9]|_)*"))
        self.LOG_NAME.setValidator(regExp)
        self.LOG_NAME.setMaxLength(15)
        # 可借阅数量
        Borrow_Height = 190
        self.LABEL_BOOKNUM = QtWidgets.QLabel(self.frame)
        self.LABEL_BOOKNUM.setGeometry(QtCore.QRect(50, Borrow_Height, 121, 41))
        self.LABEL_BOOKNUM.setObjectName("LABEL_BOOKNUM")
        #####
        self.LABEL_MAX = QtWidgets.QLabel(self.frame)
        self.LABEL_MAX.setGeometry(QtCore.QRect(310, Borrow_Height, 121, 41))
        self.LABEL_MAX.setObjectName("LABEL_MAX")
        self.LABEL_MAX.setText("最大可借数量")
        self.LABEL_HAVE = QtWidgets.QLabel(self.frame)
        self.LABEL_HAVE.setGeometry(QtCore.QRect(160, Borrow_Height, 121, 41))
        self.LABEL_HAVE.setObjectName("LABEL_HAVE")
        self.LABEL_HAVE.setText("可借数量")

        self.BOOKNUM_MAX = QtWidgets.QTextBrowser(self.frame)
        self.BOOKNUM_MAX.setGeometry(QtCore.QRect(230, Borrow_Height, 50, 41))
        self.BOOKNUM_MAX.setObjectName("BOOKNUM_MAX")
        self.BOOKNUM_HAVE = QtWidgets.QTextBrowser(self.frame)
        self.BOOKNUM_HAVE.setGeometry(QtCore.QRect(420,Borrow_Height,50,41))
        self.BOOKNUM_HAVE.setObjectName("BOOKNUM_HAVE")
        #######
        # 联系方式
        self.LABEL_ATTACH = QtWidgets.QLabel(self.frame)
        self.LABEL_ATTACH.setGeometry(QtCore.QRect(50, 230, 81, 41))
        self.LABEL_ATTACH.setObjectName("LABEL_ATTACH")
        self.COMMUNICATE = QtWidgets.QLineEdit(self.frame)
        self.COMMUNICATE.setGeometry(QtCore.QRect(190, 280, 191, 41))
        self.COMMUNICATE.setObjectName("COMMUNICATE")
        # 读者号
        self.LABEL_EEADERID = QtWidgets.QLabel(self.frame)
        self.LABEL_EEADERID.setGeometry(QtCore.QRect(50, 130, 121, 41))
        self.LABEL_EEADERID.setObjectName("LABEL_EEADERID")
        self.READERID = QtWidgets.QTextBrowser(self.frame)
        self.READERID.setGeometry(QtCore.QRect(190, 140, 191, 41))
        self.READERID.setObjectName("READERID")
        # 确定
        self.OKButton = QtWidgets.QPushButton(self.frame)
        self.OKButton.setGeometry(QtCore.QRect(270, 490, 141, 41))
        self.OKButton.setObjectName("OKButton")
        # 修改
        self.MODIFIY = QtWidgets.QPushButton(self.frame)
        self.MODIFIY.setGeometry(QtCore.QRect(30, 490, 141, 41))
        self.MODIFIY.setObjectName("MODIFIY")

        self.QQ = QtWidgets.QRadioButton(self.frame)
        self.QQ.setGeometry(QtCore.QRect(150, 240, 51, 22))
        self.QQ.setObjectName("QQ")
        self.E_MAIL = QtWidgets.QRadioButton(self.frame)
        self.E_MAIL.setGeometry(QtCore.QRect(220, 240, 71, 22))
        self.E_MAIL.setObjectName("E_MAIL")
        self.PHONE = QtWidgets.QRadioButton(self.frame)
        self.PHONE.setGeometry(QtCore.QRect(310, 240, 71, 22))
        self.PHONE.setObjectName("PHONE")
        # 密码
        self.LABEL_CODE = QtWidgets.QLabel(self.frame)
        self.LABEL_CODE.setGeometry(QtCore.QRect(50, 380, 121, 41))
        self.LABEL_CODE.setObjectName("LABEL_CODE")
        self.LOG_CODE = QtWidgets.QLineEdit(self.frame)
        self.LOG_CODE.setGeometry(QtCore.QRect(190, 380, 191, 41))
        self.LOG_CODE.setObjectName("LOG_CODE")
        # 再次输入密码
        self.LABEL_CODEAGAIN = QtWidgets.QLabel(self.frame)
        self.LABEL_CODEAGAIN.setGeometry(QtCore.QRect(50, 430, 121, 41))
        self.LABEL_CODEAGAIN.setObjectName("LABEL_CODEAGAIN")
        self.LOG_CODEAGAIN = QtWidgets.QLineEdit(self.frame)
        self.LOG_CODEAGAIN.setGeometry(QtCore.QRect(190, 430, 191, 41))
        self.LOG_CODEAGAIN.setObjectName("LOG_CODEAGAIN")
        # 显示密码
        self.CODE_SHOW = QtWidgets.QCheckBox(self.frame)
        self.CODE_SHOW.setGeometry(QtCore.QRect(390, 390, 99, 22))
        self.CODE_SHOW.setObjectName("CODE_SHOW")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "读者信息界面"))
        self.LABEL_NAME.setText(_translate("Dialog", "姓名:"))
        self.LABEL_AGE.setText(_translate("Dialog", "年龄:"))
        self.LABEL_LOGNAME.setText(_translate("Dialog", "登录名:"))
        self.LABEL_BOOKNUM.setText(_translate("Dialog", "借阅数量:"))
        self.LABEL_ATTACH.setText(_translate("Dialog", "联系方式:"))
        self.LABEL_EEADERID.setText(_translate("Dialog", "读者号:"))
        self.OKButton.setText(_translate("Dialog", "确定"))
        self.OKButton.clicked.connect(lambda : self.OK_Button(Dialog))
        self.MODIFIY.setText(_translate("Dialog", "修改信息"))
        self.MODIFIY.clicked.connect(self.Modifiy_Button)
        self.QQ.setText(_translate("Dialog", "QQ"))
        self.E_MAIL.setText(_translate("Dialog", "E-mail"))
        self.PHONE.setText(_translate("Dialog", "电话"))
        self.LABEL_CODE.setText(_translate("Dialog", "密码:"))
        self.LABEL_CODEAGAIN.setText(_translate("Dialog", "再次输入密码:"))
        self.CODE_SHOW.setText(_translate("Dialog", "显示密码"))
        self.CODE_SHOW.stateChanged.connect(self.show_hide)
        self.CODE_SHOW.setChecked(True)
        self.Print_Page()
    # 确定
    def OK_Button(self,Dialog):
        Dialog.close()
    # 修改
    def Modifiy_Button(self):
        # 检查用户名是否存在
        user_name = self.LOG_NAME.text()
        if user_name.strip() == "":
            QtWidgets.QMessageBox.warning(None, "错误提示", "请输入用户名！", QtWidgets.QMessageBox.Yes)
            self.LOG_NAME.setFocus()
            return
        # 检查密码是否正确
        passwdA = self.LOG_CODE.text()
        passwdB = self.LOG_CODEAGAIN.text()
        if passwdA == "" and passwdB == "":
            QtWidgets.QMessageBox.warning(None, "错误提示", "请输入密码！", QtWidgets.QMessageBox.Yes)
            self.LOG_CODE.setFocus()
            return
        elif passwdA != passwdB:
            QtWidgets.QMessageBox.warning(None, "错误提示", "密码前后不一致！", QtWidgets.QMessageBox.Yes)
            self.LOG_CODE.setText("")
            self.LOG_CODEAGAIN.setText("")
            self.LOG_CODE.setFocus()
            return
        # 检查QQ号码是否正确
        # 要求5~15位，不能以0开头，只能是数字
        # 第一位1-9之间的数字，第二位0-9之间的数字，数字范围4-14个之间
        # 检查电子邮件的邮箱名是否正确
        text_line = self.COMMUNICATE.text().strip()
        import re
        if self.QQ.isChecked():
            QQ_RegExp = "[1-9][0-9]{4,14}"
            s = re.match(QQ_RegExp, text_line)
            if not s:
                QtWidgets.QMessageBox.warning(None, "错误提示", "QQ号码错误,请重新输入！", QtWidgets.QMessageBox.Yes)
                self.COMMUNICATE.setFocus()
                return
        elif self.E_MAIL.isChecked():
            E_MAIL_RegExp = "^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
            s = re.match(E_MAIL_RegExp, text_line)
            if not s:
                QtWidgets.QMessageBox.warning(None, "错误提示", "E-mal邮箱输入错误,请重新输入！", QtWidgets.QMessageBox.Yes)
                self.COMMUNICATE.setFocus()
                return
        else:
            # *手机号码
            # *移动：134[0 - 8], 135, 136, 137, 138, 139, 150, 151, 157, 158, 159, 182, 187, 188
            # *联通：130, 131, 132, 152, 155, 156, 185, 186
            # *电信：133, 1349, 153, 180, 189
            regMOBILE = "^1(3[0-9]|5[0-35-9]|8[025-9])\\d{8}$"  # 移动
            regCM = "^1(34[0-8]|(3[5-9]|5[017-9]|8[278])\\d)\\d{7}$"  # 联通
            regCU = "^1(3[0-2]|5[256]|8[56])\\d{8}$"  # 电信
            regCT = "^1((33|53|8[09])[0-9]|349)\\d{7}$"  # 大陆地区固话及小灵通
            number = "(" + regMOBILE + ")|" + "(" + regCM + ")|" + "(" + regCU + ")|" + "(" + regCT + ")"
            s = re.match(number, text_line)
            if not s:
                QtWidgets.QMessageBox.warning(None, "错误提示", "电话号码输入错误,请重新输入！", QtWidgets.QMessageBox.Yes)
                self.COMMUNICATE.setFocus()
                return
        Age = self.AGE.text().strip()
        if Age == "":
            QtWidgets.QMessageBox.warning(None, "错误提示", "请输入年龄！", QtWidgets.QMessageBox.Yes)
            self.AGE.setFocus()
            return
        # 显示链接数据库的进度条
        Reg_Name = self.LOG_NAME.text().strip()
        password = self.LOG_CODE.text()
        Reader_Number = self.READERID.toPlainText().strip()
        Reader_Name = self.NAME.toPlainText().strip()
        Book_Num_MAX = self.BOOKNUM_HAVE.toPlainText().strip()
        Book_Num_HAVE = self.BOOKNUM_MAX.toPlainText().strip()
        communication = self.COMMUNICATE.text().strip()
        age = self.AGE.text().strip()
        dict_data = {
            "登录名":Reg_Name,
            "密码":password,
            "读者号":Reader_Number,
            "姓名":Reader_Name,
            "最大可借数量":int(Book_Num_MAX),
            "联系方式":communication,
            "年龄":int(age),
            "已借数量":int(Book_Num_HAVE)
        }
        ip_address = "192.168.43.205"
        try:
            result = alter_data(dict_data,ip_address)
            if result:
                QtWidgets.QMessageBox.information(None, "提示信息", "信息上传成功!", QtWidgets.QMessageBox.Yes)
                #切记要与本地的登录名和密码同步
                path_file = "cache"
                new_dict = {
                    "name":dict_data["登录名"],
                    "password": dict_data["密码"]
                }
                with open(os.path.join(path_file, "UserLoginData.json"), "w") as file:
                    json.dump(new_dict, file)
                return
            else:
                QtWidgets.QMessageBox.warning(None, "错误信息", "信息上传失败!", QtWidgets.QMessageBox.Yes)
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(None, "错误信息", "信息上传失败,请检查网络设置!", QtWidgets.QMessageBox.Yes)
            return
    # 将本地缓存的读者信息写在界面上
    def Print_Page(self):
        data = pd.read_json(os.path.join("cache", "UserDataFile.json"),typ='series')
        data = dict(data)
        QQ_RegExp = "[1-9][0-9]{4,14}"  # QQ号码的正则表达式

        if data['联系方式'].isdigit():
            pattern = re.compile(QQ_RegExp)
            res = pattern.findall(data['联系方式'])
            if not res:
                self.PHONE.setChecked(True)
            else:
                self.QQ.setChecked(True)
        else:
            self.E_MAIL.setChecked(True)

        self.NAME.setText(data['姓名'])
        self.AGE.setText(data['年龄'])
        self.LOG_NAME.setText(data['登录名'])
        self.COMMUNICATE.setText(data['联系方式'])
        self.BOOKNUM_MAX.setText(data['已借数量'])
        self.READERID.setText(data['读者号'])
        self.BOOKNUM_HAVE.setText(data['最大可借数量'])
        #　密码
        self.LOG_CODE.setText(data['密码'])
        self.LOG_CODEAGAIN.setText(data['密码'])
    #显示或者隐藏密码
    def show_hide(self):
        if self.CODE_SHOW.isChecked():
            self.LOG_CODE.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.LOG_CODEAGAIN.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.LOG_CODE.setEchoMode(QtWidgets.QLineEdit.Password)
            self.LOG_CODEAGAIN.setEchoMode(QtWidgets.QLineEdit.Password)
# 查看借阅与归还
class ViewBorrowDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 639)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 651, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.LABEL_READERID = QtWidgets.QLabel(self.tab)
        self.LABEL_READERID.setGeometry(QtCore.QRect(50, 20, 131, 41))
        self.LABEL_READERID.setObjectName("LABEL_READERID")
        self.READERID = QtWidgets.QTextBrowser(self.tab)
        self.READERID.setGeometry(QtCore.QRect(250, 20, 221, 41))
        self.READERID.setObjectName("READERID")
        self.INFO_BORROW = QtWidgets.QTableWidget(self.tab)
        self.INFO_BORROW.setGeometry(QtCore.QRect(20, 70, 611, 371))
        self.INFO_BORROW.setObjectName("INFO_BORROW")
        self.INFO_BORROW.setColumnCount(0)
        self.INFO_BORROW.setRowCount(0)
        self.CANCEL_BUTTON = QtWidgets.QPushButton(self.tab)
        self.CANCEL_BUTTON.setGeometry(QtCore.QRect(340, 460, 161, 41))
        self.CANCEL_BUTTON.setObjectName("CANCEL_BUTTON")
        self.CANCEL_BUTTON.clicked.connect(Dialog.close)
        self.OK_BUTTON = QtWidgets.QPushButton(self.tab)
        self.OK_BUTTON.setGeometry(QtCore.QRect(90, 460, 161, 41))
        self.OK_BUTTON.setObjectName("OK_BUTTON")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.LABEL_READER2 = QtWidgets.QLabel(self.tab_2)
        self.LABEL_READER2.setGeometry(QtCore.QRect(50, 20, 131, 41))
        self.LABEL_READER2.setObjectName("LABEL_READER2")
        self.READERID2 = QtWidgets.QTextBrowser(self.tab_2)
        self.READERID2.setGeometry(QtCore.QRect(250, 20, 221, 41))
        self.READERID2.setObjectName("READERID2")
        self.INFO_BORROW_2 = QtWidgets.QTableWidget(self.tab_2)
        self.INFO_BORROW_2.setGeometry(QtCore.QRect(20, 70, 611, 421))
        self.INFO_BORROW_2.setObjectName("INFO_BORROW_2")
        self.INFO_BORROW_2.setColumnCount(0)
        self.INFO_BORROW_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "读者借阅与归还界面"))
        self.LABEL_READERID.setText(_translate("Dialog", "读者编号:"))
        self.CANCEL_BUTTON.setText(_translate("Dialog", "取消"))
        self.OK_BUTTON.setText(_translate("Dialog", "确定归还"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "历史借阅信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "查看借阅与归还"))
        self.LABEL_READER2.setText(_translate("Dialog", "读者编号:"))

# 读书摘要笔记
class BookNote(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 527)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 581, 301))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 141, 41))
        self.label.setObjectName("label")
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(140, 420, 131, 41))
        self.OK.setObjectName("OK")
        self.Cancel = QtWidgets.QPushButton(Dialog)
        self.Cancel.setGeometry(QtCore.QRect(360, 420, 131, 41))
        self.Cancel.setObjectName("Cancel")
        self.Cancel.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "读书摘要笔记"))
        self.label.setText(_translate("Dialog", "读书摘要笔记:"))
        self.OK.setText(_translate("Dialog", "确定"))
        self.Cancel.setText(_translate("Dialog", "取消"))
    def OK_btn(self):
        #将输入的内容提交到服务器上
        pass
#图书查询与借阅
class LitWiget(QtWidgets.QWidget):
    def __init__(self):
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label.setObjectName("label")
    def setText(self,string):
        self.label.setText(string)
    def setPic(self):
        pass
class BookBorrowQuery(object):
    def setupUi(self, BookBorrowQuery):
        BookBorrowQuery.setObjectName("BookBorrowQuery")
        BookBorrowQuery.resize(730, 551)
        self.LABEL_Q = QtWidgets.QLabel(BookBorrowQuery)
        self.LABEL_Q.setGeometry(QtCore.QRect(40, 20, 121, 41))
        self.LABEL_Q.setObjectName("LABEL_Q")
        #查询条件
        self.CONDITION = QtWidgets.QComboBox(BookBorrowQuery)
        self.CONDITION.setGeometry(QtCore.QRect(110, 20, 121, 41))
        self.CONDITION.setObjectName("CONDITION")
        condition = ['书名','作者','出版社','读者对象']
        #添加查询条件
        for item in condition:
            self.CONDITION.addItem(item)
        #查询按钮
        self.QUERY_TEXT = QtWidgets.QLineEdit(BookBorrowQuery)
        self.QUERY_TEXT.setGeometry(QtCore.QRect(240, 20, 161, 41))
        self.QUERY_TEXT.setObjectName("QUERY_TEXT")
        self.QUERY_BTN = QtWidgets.QPushButton(BookBorrowQuery)
        self.QUERY_BTN.setGeometry(QtCore.QRect(420, 20, 131, 41))
        self.QUERY_BTN.setObjectName("QUERY_BTN")

        self.gridLayoutWidget = QtWidgets.QWidget(BookBorrowQuery)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 70, 681, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.widget_3 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget_3)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_4.setObjectName("label_4")

        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.widget_4)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.widget_4, 0, 3, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setObjectName("widget")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_5.setObjectName("widget_5")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.widget_5)
        self.graphicsView_5.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.widget_5, 1, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_6.setObjectName("widget_6")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.widget_6)
        self.graphicsView_6.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.widget_6, 1, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_7.setObjectName("widget_7")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.widget_7)
        self.graphicsView_7.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.widget_7, 1, 2, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_8.setObjectName("widget_8")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.widget_8)
        self.graphicsView_8.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.label_9 = QtWidgets.QLabel(self.widget_8)
        self.label_9.setGeometry(QtCore.QRect(30, 150, 101, 21))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.widget_8, 1, 3, 1, 1)
        #上一页
        self.PREVIEW = QtWidgets.QPushButton(BookBorrowQuery)
        self.PREVIEW.setGeometry(QtCore.QRect(60, 480, 111, 41))
        self.PREVIEW.setObjectName("PREVIEW")
        self.label_10 = QtWidgets.QLabel(BookBorrowQuery)
        self.label_10.setGeometry(QtCore.QRect(290, 480, 51, 41))
        self.label_10.setObjectName("label_10")
        self.MAIN_PAGE = QtWidgets.QLineEdit(BookBorrowQuery)
        self.MAIN_PAGE.setGeometry(QtCore.QRect(190, 480, 91, 41))
        self.MAIN_PAGE.setObjectName("MAIN_PAGE")
        self.label_11 = QtWidgets.QLabel(BookBorrowQuery)
        self.label_11.setGeometry(QtCore.QRect(490, 480, 81, 41))
        self.label_11.setObjectName("label_11")
        #下一页
        self.NEXT = QtWidgets.QPushButton(BookBorrowQuery)
        self.NEXT.setGeometry(QtCore.QRect(580, 480, 111, 41))
        self.NEXT.setObjectName("NEXT")
        self.ALL_PAGE = QtWidgets.QTextBrowser(BookBorrowQuery)
        self.ALL_PAGE.setGeometry(QtCore.QRect(360, 480, 111, 41))
        self.ALL_PAGE.setObjectName("ALL_PAGE")
        #退出功能
        self.EXIT = QtWidgets.QPushButton(BookBorrowQuery)
        self.EXIT.setGeometry(QtCore.QRect(570, 20, 121, 41))
        self.EXIT.setObjectName("EXIT")
        self.EXIT.clicked.connect(BookBorrowQuery.close)

        self.retranslateUi(BookBorrowQuery)
        QtCore.QMetaObject.connectSlotsByName(BookBorrowQuery)

    def retranslateUi(self, BookBorrowQuery):
        _translate = QtCore.QCoreApplication.translate
        BookBorrowQuery.setWindowTitle(_translate("BookBorrowQuery", "图书查询与借阅界面"))
        self.LABEL_Q.setText(_translate("BookBorrowQuery", "查询条件"))
        self.QUERY_BTN.setText(_translate("BookBorrowQuery", "查询"))
        self.label_4.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_5.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_2.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_3.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_6.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_7.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_8.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.label_9.setText(_translate("BookBorrowQuery", "TextLabel"))
        self.PREVIEW.setText(_translate("BookBorrowQuery", "上一页"))
        self.label_10.setText(_translate("BookBorrowQuery", "页   共"))
        self.label_11.setText(_translate("BookBorrowQuery", "页"))
        self.NEXT.setText(_translate("BookBorrowQuery", "下一页"))
        self.EXIT.setText(_translate("BookBorrowQuery", "退出"))
