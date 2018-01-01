from PyQt5 import QtCore, QtGui, QtWidgets
from Clock import Clock
import datetime
from connect_db import get_user_basic_data
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
        # 图书的归还操作
        self.borrowbutton = QtWidgets.QPushButton(Dialog)
        self.borrowbutton.setGeometry(QtCore.QRect(30, 130, 121, 41))
        self.borrowbutton.setObjectName("borrowbutton")
        # 摘要笔记
        self.NoteBook = QtWidgets.QPushButton(Dialog)
        self.NoteBook.setGeometry(QtCore.QRect(30, 180, 121, 41))
        self.NoteBook.setObjectName("NoteBook")
        # 查询图书的操作
        self.viewBooks = QtWidgets.QPushButton(Dialog)
        self.viewBooks.setGeometry(QtCore.QRect(30,230, 121, 41))
        self.viewBooks.setObjectName("viewBooks")
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
        self.borrowInfor.setText(_translate("Dialog", "查看借阅信息"))
        self.borrowbutton.setText(_translate("Dialog", "图书借阅与归还"))
        self.NoteBook.setText(_translate("Dialog", "读书摘要笔记"))
        self.ExitButton.setText(_translate("Dialog", "退出系统"))
        self.viewBooks.setText(_translate("Dialog","图书查询"))
    # 退出系统
    def exit_func(self,Dialog):
        Dialog.close()
    # 显示读者信息
    def print_reader(self):
        ip_address = "192.168.43.205"
        basic_data = get_user_basic_data(ip_address)
        Form1 = QtWidgets.QWidget()
        ui = ReaderInformation_Dialog()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
# 读者信息界面
class ReaderInformation_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 438)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 461, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Name = QtWidgets.QLabel(self.frame)
        self.Name.setGeometry(QtCore.QRect(50, 30, 321, 41))
        self.Name.setObjectName("label")
        self.Age = QtWidgets.QLabel(self.frame)
        self.Age.setGeometry(QtCore.QRect(50, 80, 321, 41))
        self.Age.setObjectName("label_2")
        self.Log_Name = QtWidgets.QLabel(self.frame)
        self.Log_Name.setGeometry(QtCore.QRect(50, 130, 321, 41))
        self.Log_Name.setObjectName("label_3")
        self.Num_Books = QtWidgets.QLabel(self.frame)
        self.Num_Books.setGeometry(QtCore.QRect(50, 220, 321, 41))
        self.Num_Books.setObjectName("label_4")
        self.Communicate = QtWidgets.QLabel(self.frame)
        self.Communicate.setGeometry(QtCore.QRect(50, 270, 321, 41))
        self.Communicate.setObjectName("label_5")
        self.Reader_Number = QtWidgets.QLabel(self.frame)
        self.Reader_Number.setGeometry(QtCore.QRect(50, 170, 321, 41))
        self.Reader_Number.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 340, 201, 41))
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "读者信息界面"))
        self.Name.setText(_translate("Dialog", "姓名:"))
        self.Age.setText(_translate("Dialog", "年龄:"))
        self.Log_Name.setText(_translate("Dialog", "登录名:"))
        self.Num_Books.setText(_translate("Dialog", "可借阅数量:"))
        self.Communicate.setText(_translate("Dialog", "联系方式:"))
        self.Reader_Number.setText(_translate("Dialog", "读者号:"))
        self.pushButton.setText(_translate("Dialog", "确定"))
    def get_information(self):
        return