from PyQt5 import QtCore,QtWidgets,QtGui
from Clock import Clock
import requests
from connect_db import get_user_name,save_db_reader,get_name
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
        self.InforModify.clicked.connect(self.modify_info)
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
    def modify_info(self):
        Form1 = QtWidgets.QWidget()
        ui = ManagerInformation_Dialog()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
# 修改信息界面
class ManagerInformation_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 659)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 20, 481, 620))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # 姓名
        Name_Hight = 30
        self.LABEL_NAME = QtWidgets.QLabel(self.frame)
        self.LABEL_NAME.setGeometry(QtCore.QRect(50, Name_Hight, 121, 41))
        self.LABEL_NAME.setObjectName("LABEL_NAME")
        self.NAME = QtWidgets.QTextEdit(self.frame)
        self.NAME.setGeometry(QtCore.QRect(190, Name_Hight, 191, 41))
        self.NAME.setObjectName("NAME")
        # 年龄
        Age_hight = 80
        self.LABEL_AGE = QtWidgets.QLabel(self.frame)
        self.LABEL_AGE.setGeometry(QtCore.QRect(50, Age_hight, 121, 41))
        self.LABEL_AGE.setObjectName("LABEL_AGE")
        self.AGE = QtWidgets.QLineEdit(self.frame)
        self.AGE.setGeometry(QtCore.QRect(190, Age_hight, 191, 41))
        self.AGE.setObjectName("AGE")
        RegExp = QtGui.QRegExpValidator(QtCore.QRegExp("([0-9])*"))
        self.AGE.setMaxLength(2)
        self.AGE.setValidator(RegExp)
        # 编号
        ID_Hight = 130
        self.LABEL_ID = QtWidgets.QLabel(self.frame)
        self.LABEL_ID.setGeometry(QtCore.QRect(50, ID_Hight, 121, 41))
        self.LABEL_ID.setObjectName("LABEL_ID")
        self.ID = QtWidgets.QTextBrowser(self.frame)
        self.ID.setGeometry(QtCore.QRect(190, ID_Hight, 191, 41))
        self.ID.setObjectName("ID")
        # 工作类型
        WorkType_Hight = 180
        self.LABEL_TYPE = QtWidgets.QLabel(self.frame)
        self.LABEL_TYPE.setGeometry(QtCore.QRect(50, WorkType_Hight, 121, 41))
        self.LABEL_TYPE.setObjectName("LABEL_TYPE")
        self.type = QtWidgets.QTextBrowser(self.frame)
        self.type.setGeometry(QtCore.QRect(190, WorkType_Hight, 191, 41))
        self.type.setObjectName("BOOKNUM")
        # 工资
        WorkSalary_Hight = 230
        self.LABEL_Salary = QtWidgets.QLabel(self.frame)
        self.LABEL_Salary.setGeometry(QtCore.QRect(50, WorkSalary_Hight, 121, 41))
        self.LABEL_Salary.setObjectName("LABEL_Salary")
        self.Salary = QtWidgets.QTextBrowser(self.frame)
        self.Salary.setGeometry(QtCore.QRect(190, WorkSalary_Hight, 191, 41))
        self.Salary.setObjectName("Salary")

        # 联系方式
        Communicate_Hight = 280
        self.LABEL_ATTACH = QtWidgets.QLabel(self.frame)
        self.LABEL_ATTACH.setGeometry(QtCore.QRect(50, Communicate_Hight, 81, 41))
        self.LABEL_ATTACH.setObjectName("LABEL_ATTACH")
        self.COMMUNICATE = QtWidgets.QLineEdit(self.frame)
        self.COMMUNICATE.setGeometry(QtCore.QRect(190, Communicate_Hight + 50, 191, 41))
        self.COMMUNICATE.setObjectName("COMMUNICATE")
        QQ_E_PHONE_Hight = 290
        self.QQ = QtWidgets.QRadioButton(self.frame)
        self.QQ.setGeometry(QtCore.QRect(150, QQ_E_PHONE_Hight, 51, 22))
        self.QQ.setObjectName("QQ")
        self.E_MAIL = QtWidgets.QRadioButton(self.frame)
        self.E_MAIL.setGeometry(QtCore.QRect(220, QQ_E_PHONE_Hight, 71, 22))
        self.E_MAIL.setObjectName("E_MAIL")
        self.PHONE = QtWidgets.QRadioButton(self.frame)
        self.PHONE.setGeometry(QtCore.QRect(310, QQ_E_PHONE_Hight, 71, 22))
        self.PHONE.setObjectName("PHONE")
        #登录名
        LogName_Hight = 380
        self.LABEL_LOGNAME = QtWidgets.QLabel(self.frame)
        self.LABEL_LOGNAME.setGeometry(QtCore.QRect(50, LogName_Hight, 121, 41))
        self.LABEL_LOGNAME.setObjectName("LABEL_LOGNAME")
        self.LOG_NAME = QtWidgets.QLineEdit(self.frame)
        self.LOG_NAME.setGeometry(QtCore.QRect(190, LogName_Hight, 191, 41))
        self.LOG_NAME.setObjectName("LOG_NAME")
        regExp = QtGui.QRegExpValidator(QtCore.QRegExp("([A-Z]|[a-z]|[0-9]|_)*"))
        self.LOG_NAME.setValidator(regExp)
        self.LOG_NAME.setMaxLength(15)
        # 密码
        CODE_Hight = 430
        self.LABEL_CODE = QtWidgets.QLabel(self.frame)
        self.LABEL_CODE.setGeometry(QtCore.QRect(50, CODE_Hight, 121, 41))
        self.LABEL_CODE.setObjectName("LABEL_CODE")
        self.LOG_CODE = QtWidgets.QLineEdit(self.frame)
        self.LOG_CODE.setGeometry(QtCore.QRect(190, CODE_Hight, 191, 41))
        self.LOG_CODE.setObjectName("LOG_CODE")
        # 显示密码
        Show_Hight = 440
        self.CODE_SHOW = QtWidgets.QCheckBox(self.frame)
        self.CODE_SHOW.setGeometry(QtCore.QRect(390, Show_Hight, 99, 22))
        self.CODE_SHOW.setObjectName("CODE_SHOW")
        # 再次输入密码
        AGAIN_Hight = 490
        self.LABEL_CODEAGAIN = QtWidgets.QLabel(self.frame)
        self.LABEL_CODEAGAIN.setGeometry(QtCore.QRect(50, AGAIN_Hight, 121, 41))
        self.LABEL_CODEAGAIN.setObjectName("LABEL_CODEAGAIN")
        self.LOG_CODEAGAIN = QtWidgets.QLineEdit(self.frame)
        self.LOG_CODEAGAIN.setGeometry(QtCore.QRect(190, AGAIN_Hight, 191, 41))
        self.LOG_CODEAGAIN.setObjectName("LOG_CODEAGAIN")
        # 确定
        OK_MODIFY_Hight = 540
        self.OKButton = QtWidgets.QPushButton(self.frame)
        self.OKButton.setGeometry(QtCore.QRect(270, OK_MODIFY_Hight, 141, 41))
        self.OKButton.setObjectName("OKButton")
        # 修改
        self.MODIFIY = QtWidgets.QPushButton(self.frame)
        self.MODIFIY.setGeometry(QtCore.QRect(30, OK_MODIFY_Hight, 141, 41))
        self.MODIFIY.setObjectName("MODIFIY")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理员信息界面"))
        self.LABEL_NAME.setText(_translate("Dialog", "姓名:"))
        self.LABEL_AGE.setText(_translate("Dialog", "年龄:"))
        self.LABEL_LOGNAME.setText(_translate("Dialog", "登录名:"))
        self.LABEL_TYPE.setText(_translate("Dialog", "管理类别:"))
        self.LABEL_Salary.setText(_translate("Dialog", "工资:"))
        self.LABEL_ATTACH.setText(_translate("Dialog", "联系方式:"))
        self.LABEL_ID.setText(_translate("Dialog", "工号:"))
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
        elif get_name(3, user_name):
            QtWidgets.QMessageBox.warning(None, "错误提示", "用户已经存在，请再选其他登录名！", QtWidgets.QMessageBox.Yes)
            self.LOG_NAME.setText("")
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
        Reader_Number = self.ID.toPlainText().strip()
        Reader_Name = self.NAME.toPlainText().strip()
        Book_num = self.BOOKNUM.toPlainText().strip()
        communication = self.COMMUNICATE.text().strip()
        information = "[\"%s\",\"%s\",\"30\",\"%s\",\"%s\",\"0\",\"%s\",\"%s\"]" % (
        Reader_Number, Reader_Name, communication, Book_num, Reg_Name, password)
        dict_data = "{\"registerClass\":3,\"info\":%s}" % information
        ip_address = "192.168.43.205"
        try:
            if save_db_reader(str(dict_data), ip_address):
                QtWidgets.QMessageBox.information(None, "提示信息", "信息修改成功!", QtWidgets.QMessageBox.Yes)
                return
            else:
                QtWidgets.QMessageBox.warning(None, "提示信息", "登陆名已存在，请重新填写信息!", QtWidgets.QMessageBox.Yes)
                self.LOG_NAME.setFocus()
                return
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(None, "错误信息", "信息上传失败,请检查网络设置!", QtWidgets.QMessageBox.Yes)
            return
    # 将本地缓存的读者信息写在界面上
    def Print_Page(self):
        QQ_RegExp = "[1-9][0-9]{4,14}"  # QQ号码的正则表达式
        E_MAIL_RegExp = "^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"  # E-mail 正则表达式
        # *手机号码
        # *移动：134[0 - 8], 135, 136, 137, 138, 139, 150, 151, 157, 158, 159, 182, 187, 188
        # *联通：130, 131, 132, 152, 155, 156, 185, 186
        # *电信：133, 1349, 153, 180, 189
        regMOBILE = "^1(3[0-9]|5[0-35-9]|8[025-9])\\d{8}$"  # 移动
        regCM = "^1(34[0-8]|(3[5-9]|5[017-9]|8[278])\\d)\\d{7}$"  # 联通
        regCU = "^1(3[0-2]|5[256]|8[56])\\d{8}$"  # 电信
        regCT = "^1((33|53|8[09])[0-9]|349)\\d{7}$"  # 大陆地区固话及小灵通
        number = "(" + regMOBILE + ")|" + "(" + regCM + ")|" + "(" + regCU + ")|" + "(" + regCT + ")"
    #显示或者隐藏密码
    def show_hide(self):
        if self.CODE_SHOW.isChecked():
            self.LOG_CODE.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.LOG_CODEAGAIN.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.LOG_CODE.setEchoMode(QtWidgets.QLineEdit.Password)
            self.LOG_CODEAGAIN.setEchoMode(QtWidgets.QLineEdit.Password)