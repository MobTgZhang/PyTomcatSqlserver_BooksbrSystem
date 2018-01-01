from PyQt5 import QtCore,QtWidgets
import datetime
from Clock import Clock
class ContorlerDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 444)
        self.ButtonBooked = QtWidgets.QPushButton(Dialog)
        self.ButtonBooked.setGeometry(QtCore.QRect(20, 20, 141, 41))
        self.ButtonBooked.setObjectName("ButtonBooked")
        self.ButtonSaled = QtWidgets.QPushButton(Dialog)
        self.ButtonSaled.setGeometry(QtCore.QRect(20, 70, 141, 41))
        self.ButtonSaled.setObjectName("ButtonSaled")
        self.ButtonModify = QtWidgets.QPushButton(Dialog)
        self.ButtonModify.setGeometry(QtCore.QRect(20, 120, 141, 41))
        self.ButtonModify.setObjectName("ButtonModify")
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
        Dialog.setWindowTitle(_translate("Dialog", "操作员界面"))
        self.ButtonBooked.setText(_translate("Dialog", "参与的订购"))
        self.ButtonSaled.setText(_translate("Dialog", "参与的出售"))
        self.ButtonModify.setText(_translate("Dialog", "修改信息"))
    def exit_func(self,Dialog):
        Dialog.close()