from PyQt5 import QtCore,QtWidgets
from Clock import Clock
import datetime
class Manager_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 444)
        self.controlerButton = QtWidgets.QPushButton(Dialog)
        self.controlerButton.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.controlerButton.setObjectName("controlerButton")
        self.ReaderButton = QtWidgets.QPushButton(Dialog)
        self.ReaderButton.setGeometry(QtCore.QRect(20, 70, 131, 41))
        self.ReaderButton.setObjectName("ReaderButton")
        self.BorrowViewButton = QtWidgets.QPushButton(Dialog)
        self.BorrowViewButton.setGeometry(QtCore.QRect(20, 120, 131, 41))
        self.BorrowViewButton.setObjectName("BorrowViewButton")
        self.BooksButton = QtWidgets.QPushButton(Dialog)
        self.BooksButton.setGeometry(QtCore.QRect(20, 170, 131, 41))
        self.BooksButton.setObjectName("BooksButton")
        self.InforModify = QtWidgets.QPushButton(Dialog)
        self.InforModify.setGeometry(QtCore.QRect(20, 220, 131, 41))
        self.InforModify.setObjectName("InforModify")
        # 退出系统
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(500, 380, 121, 41))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("退出系统")
        self.exitButton.clicked.connect(lambda: self.exit_func(Dialog))
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
        Dialog.setWindowTitle(_translate("Dialog", "管理员界面"))
        self.controlerButton.setText(_translate("Dialog", "操作员管理"))
        self.ReaderButton.setText(_translate("Dialog", "读者管理"))
        self.BorrowViewButton.setText(_translate("Dialog", "借阅查询与管理"))
        self.BooksButton.setText(_translate("Dialog", "书籍管理"))
        self.InforModify.setText(_translate("Dialog", "信息修改"))
    def exit_func(self,Dialog):
        Dialog.close()