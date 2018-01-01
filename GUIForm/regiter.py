from PyQt5 import QtCore, QtGui, QtWidgets
from connect_db import get_name,get_number_usr,save_db_reader
class Register_Dialog(object):
    def setupUi(self, Dialog):
        regExp = QtGui.QRegExpValidator(QtCore.QRegExp("([A-Z]|[a-z]|[0-9]|_)*"))
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 550)
        # 按钮
        self.postButton = QtWidgets.QPushButton(Dialog)
        Button_Hight = 500
        self.postButton.setGeometry(QtCore.QRect(40, Button_Hight,100, 30))
        self.postButton.setObjectName("postButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(280, Button_Hight,100, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(160, Button_Hight,100,30))
        self.clearButton.setObjectName("clearButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 21))
        self.label.setObjectName("label")
        self.Read_Num = QtWidgets.QLabel(Dialog)
        self.Read_Num.setGeometry(QtCore.QRect(70, 180, 61, 41))
        self.Read_Num.setObjectName("Read_Num")

        # 检查并生成一个读者编号
        ip_address = "192.168.43.205"
        Number = get_number_usr(3,ip_address)
        self.ReaderNum = QtWidgets.QTextBrowser(Dialog)
        self.ReaderNum.setGeometry(QtCore.QRect(150, 190, 211, 31))
        self.ReaderNum.setObjectName("ReaderNum")
        self.ReaderNum.setText(Number)

        # 姓名
        Name_Hight = 230
        self.Name_Text = QtWidgets.QTextEdit(Dialog)
        self.Name_Text.setGeometry(QtCore.QRect(150, Name_Hight, 211, 41))
        self.Name_Text.setObjectName("Name_Text")
        self.Name_label = QtWidgets.QLabel(Dialog)
        self.Name_label.setGeometry(QtCore.QRect(70, Name_Hight, 41, 21))
        self.Name_label.setObjectName("Name_label")
        self.Name_label.setText("姓名")
        # 年龄
        self.Age_label = QtWidgets.QLabel(Dialog)
        self.Age_label.setGeometry(QtCore.QRect(370, Name_Hight, 41, 21))
        self.Age_label.setObjectName("Name_label")
        self.Age_label.setText("年龄")
        self.Age_text = QtWidgets.QLineEdit(Dialog)
        self.Age_text.setGeometry(QtCore.QRect(420, Name_Hight, 50, 41))
        self.Age_text.setObjectName("Age_text")
        RegExp = QtGui.QRegExpValidator(QtCore.QRegExp("([0-9])*"))
        self.Age_text.setValidator(RegExp)
        self.Age_text.setMaxLength(2)

        #联系方式
        Connect_Height = 360
        self.connect_Num = QtWidgets.QLabel(Dialog)
        self.connect_Num.setGeometry(QtCore.QRect(70, Connect_Height, 71, 30))
        self.connect_Num.setObjectName("connect_Num")
        self.QQ = QtWidgets.QRadioButton(Dialog)
        self.QQ.setGeometry(QtCore.QRect(150,Connect_Height, 50, 30))
        self.QQ.setObjectName("QQ")
        self.QQ.setText("QQ")
        self.QQ.setChecked(True)
        self.E_mail = QtWidgets.QRadioButton(Dialog)
        self.E_mail.setGeometry(QtCore.QRect(200,Connect_Height,65, 30))
        self.E_mail.setObjectName("E_mail")
        self.E_mail.setText("E-mail")
        self.phone = QtWidgets.QRadioButton(Dialog)
        self.phone.setGeometry(QtCore.QRect(265, Connect_Height, 65, 30))
        self.phone.setObjectName("phone")
        self.phone.setText("phone")

        self.communicate_edit = QtWidgets.QLineEdit(Dialog)
        self.communicate_edit.setGeometry(QtCore.QRect(150, Connect_Height + 30, 200,30))
        self.communicate_edit.setObjectName("communicate_edit")
        # 可借阅图书数量
        Books_Height = 290
        self.Nums_Books = QtWidgets.QLabel(Dialog)
        self.Nums_Books.setGeometry(QtCore.QRect(60, Books_Height, 81, 31))
        self.Nums_Books.setObjectName("Nums_Books")
        self.Books_Num = QtWidgets.QTextBrowser(Dialog)
        self.Books_Num.setGeometry(QtCore.QRect(150, Books_Height, 211, 41))
        self.Books_Num.setObjectName("Books_Num")
        self.Books_Num.setText("5")

        # 登录名以及设置的格式
        Long_In_Higeht = 40
        self.lLogIn = QtWidgets.QLabel(Dialog)
        self.lLogIn.setGeometry(QtCore.QRect(60, Long_In_Higeht, 51, 17))
        self.lLogIn.setObjectName("lLogIn")
        self.Log_Name = QtWidgets.QLineEdit(Dialog)
        self.Log_Name.setGeometry(QtCore.QRect(150, Long_In_Higeht, 211, 41))
        self.Log_Name.setObjectName("Log_Name")
        # 格式
        self.Log_Name.setValidator(regExp)
        self.Log_Name.setMaxLength(15)

        # 密码
        passwdAHight = 90
        self.passwd_A = QtWidgets.QLabel(Dialog)
        self.passwd_A.setGeometry(QtCore.QRect(80, passwdAHight, 51, 17))
        self.passwd_A.setObjectName("passwd_A")
        # self.passwd_A.setAlignment(QtCore.Qt.AlignCenter)
        self.passwdA = QtWidgets.QLineEdit(Dialog)
        self.passwdA.setGeometry(QtCore.QRect(150,passwdAHight, 211, 41))
        self.passwdA.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdA.setObjectName("passwdA")
        self.passwdA.setValidator(regExp)
        self.passwdA.setMaxLength(15)
        self.show_passwd = QtWidgets.QCheckBox(Dialog)
        self.show_passwd.setGeometry(QtCore.QRect(370,passwdAHight,211,41))
        self.show_passwd.setText("显示密码")
        self.show_passwd.stateChanged.connect(self.show_passwdQ)
        # 再次输入密码
        self.passwd_B = QtWidgets.QLabel(Dialog)
        self.passwd_B.setGeometry(QtCore.QRect(37, 150, 91, 20))
        self.passwd_B.setObjectName("passwd_B")
        self.passwdB = QtWidgets.QLineEdit(Dialog)
        self.passwdB.setGeometry(QtCore.QRect(150, 140, 211, 41))
        self.passwdB.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdB.setObjectName("passwdB")
        self.passwdB.setValidator(regExp)
        self.passwdB.setMaxLength(15)
        # 信息显示
        self.Information = QtWidgets.QLabel(Dialog)
        self.Information.setGeometry(QtCore.QRect(50, 420, 361, 50))
        self.Information.setText("登录名和密码限制在15字以内并且仅限:\n      下划线大小写字母和数字")
        self.Information.setObjectName("Information")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "读者注册页面"))
        self.postButton.setText(_translate("Dialog", "提交"))
        self.postButton.clicked.connect(self.post_infor)
        self.cancelButton.setText(_translate("Dialog", "取消"))
        self.cancelButton.clicked.connect(Dialog.close)
        self.clearButton.setText(_translate("Dialog", "清除"))
        self.clearButton.clicked.connect(self.clear_infor)
        self.label.setText(_translate("Dialog", "读者信息注册"))
        self.Read_Num.setText(_translate("Dialog", "读者号"))
        self.Name_label.setText(_translate("Dialog", "姓名"))
        self.connect_Num.setText(_translate("Dialog", "联系方式"))
        self.Nums_Books.setText(_translate("Dialog", "可借阅数量"))
        self.lLogIn.setText(_translate("Dialog", "登录名"))
        self.passwd_A.setText(_translate("Dialog", "密码"))
        self.passwd_B.setText(_translate("Dialog", "再次输入密码"))
    def clear_infor(self):
        self.passwdA.setText("")
        self.passwdB.setText("")
        self.Log_Name.setText("")
        self.communicate_edit.setText("")
        self.Name_Text.setText("")
    def post_infor(self):
        # 检查用户名是否存在
        user_name = self.Log_Name.text()
        if user_name.strip()=="":
            QtWidgets.QMessageBox.warning(None, "错误提示", "请输入用户名！", QtWidgets.QMessageBox.Yes)
            self.Log_Name.setFocus()
            return
        elif get_name(3, user_name):
            QtWidgets.QMessageBox.warning(None, "错误提示", "用户已经存在，请再选其他登录名！", QtWidgets.QMessageBox.Yes)
            self.Log_Name.setText("")
            self.Log_Name.setFocus()
            return
        # 检查密码是否正确
        passwdA = self.passwdA.text()
        passwdB = self.passwdB.text()
        if passwdA=="" and passwdB=="":
            QtWidgets.QMessageBox.warning(None, "错误提示", "请输入密码！", QtWidgets.QMessageBox.Yes)
            self.passwdA.setFocus()
            return
        elif passwdA!=passwdB:
            QtWidgets.QMessageBox.warning(None,"错误提示","密码前后不一致！",QtWidgets.QMessageBox.Yes)
            self.passwdA.setText("")
            self.passwdB.setText("")
            self.passwdA.setFocus()
            return
        # 检查QQ号码是否正确
        # 要求5~15位，不能以0开头，只能是数字
        # 第一位1-9之间的数字，第二位0-9之间的数字，数字范围4-14个之间
        # 检查电子邮件的邮箱名是否正确
        text_line = self.communicate_edit.text().strip()
        import re
        if self.QQ.isChecked():
            QQ_RegExp= "[1-9][0-9]{4,14}"
            s = re.match(QQ_RegExp, text_line)
            if not s:
                QtWidgets.QMessageBox.warning(None,"错误提示","QQ号码错误,请重新输入！",QtWidgets.QMessageBox.Yes)
                self.communicate_edit.setFocus()
                return
        elif self.E_mail.isChecked():
            E_MAIL_RegExp = "^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
            s = re.match(E_MAIL_RegExp, text_line)
            if not s:
                QtWidgets.QMessageBox.warning(None,"错误提示","E-mal邮箱输入错误,请重新输入！",QtWidgets.QMessageBox.Yes)
                self.communicate_edit.setFocus()
                return
        else:
            # *手机号码
            # *移动：134[0 - 8], 135, 136, 137, 138, 139, 150, 151, 157, 158, 159, 182, 187, 188
            # *联通：130, 131, 132, 152, 155, 156, 185, 186
            # *电信：133, 1349, 153, 180, 189
            regMOBILE = "^1(3[0-9]|5[0-35-9]|8[025-9])\\d{8}$" #移动
            regCM = "^1(34[0-8]|(3[5-9]|5[017-9]|8[278])\\d)\\d{7}$" # 联通
            regCU = "^1(3[0-2]|5[256]|8[56])\\d{8}$" # 电信
            regCT = "^1((33|53|8[09])[0-9]|349)\\d{7}$" #大陆地区固话及小灵通
            number = "(" + regMOBILE +")|" + "(" + regCM + ")|" + "(" + regCU +")|" + "(" + regCT + ")"
            s = re.match(number,text_line)
            if not s:
                QtWidgets.QMessageBox.warning(None,"错误提示","电话号码输入错误,请重新输入！",QtWidgets.QMessageBox.Yes)
                self.communicate_edit.setFocus()
                return
        Age = self.Age_text.text().strip()
        if Age =="":
            QtWidgets.QMessageBox.warning(None, "错误提示", "请输入年龄！", QtWidgets.QMessageBox.Yes)
            self.Age_text.setFocus()
            return
        #显示链接数据库的进度条
        Reg_Name = self.Log_Name.text().strip()
        password = self.passwdA.text()
        Reader_Number = self.ReaderNum.toPlainText().strip()
        Reader_Name = self.Name_Text.toPlainText().strip()
        Book_num = self.Books_Num.toPlainText().strip()
        communication = self.communicate_edit.text().strip()
        information = "[\"%s\",\"%s\",\"30\",\"%s\",\"%s\",\"0\",\"%s\",\"%s\"]"%(Reader_Number,Reader_Name,communication,Book_num,Reg_Name,password)
        dict_data = "{\"registerClass\":3,\"info\":%s}"%information
        ip_address = "192.168.43.205"
        if save_db_reader(str(dict_data),ip_address):
            QtWidgets.QMessageBox.information(None,"提示信息","信息上传成功!",QtWidgets.QMessageBox.Yes)
            return
        else:
            QtWidgets.QMessageBox.warning(None, "提示信息", "登陆名已存在，请重新填写信息!", QtWidgets.QMessageBox.Yes)
            self.Log_Name.setFocus()
            return
        # 显示密码
    def show_passwdQ(self):
        if self.show_passwd.isChecked():
            self.passwdA.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.passwdB.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwdA.setEchoMode(QtWidgets.QLineEdit.Password)
            self.passwdB.setEchoMode(QtWidgets.QLineEdit.Password)