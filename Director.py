from PyQt5 import QtCore,QtWidgets,QtGui
from Clock import Clock
import datetime
import os
import requests
import json
from XLS_FILE_PROCESS import process_xls
from connect_db import post_books_data
class Director_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 444)
        self.ManagerButton = QtWidgets.QPushButton(Dialog)
        self.ManagerButton.setGeometry(QtCore.QRect(20, 10, 131, 41))
        self.ManagerButton.setObjectName("pushButton")
        self.ControlerButton = QtWidgets.QPushButton(Dialog)
        self.ControlerButton.setGeometry(QtCore.QRect(20, 60, 131, 41))
        self.ControlerButton.setObjectName("pushButton_2")
        self.ReaderButton = QtWidgets.QPushButton(Dialog)
        self.ReaderButton.setGeometry(QtCore.QRect(20, 110, 131, 41))
        self.ReaderButton.setObjectName("pushButton_3")
        self.BooksBorrowButton = QtWidgets.QPushButton(Dialog)
        self.BooksBorrowButton.setGeometry(QtCore.QRect(20, 160, 131, 41))
        self.BooksBorrowButton.setObjectName("pushButton_4")
        self.BooksBuyButton = QtWidgets.QPushButton(Dialog)
        self.BooksBuyButton.setGeometry(QtCore.QRect(20, 210, 131, 41))
        self.BooksBuyButton.setObjectName("pushButton_5")
        self.BooksManagerButton = QtWidgets.QPushButton(Dialog)
        self.BooksManagerButton.setGeometry(QtCore.QRect(20, 260, 131, 41))
        self.BooksManagerButton.setObjectName("pushButton_6")
        self.BooksManagerButton.clicked.connect(self.Show_BooksManager)
        self.DirectorManagerButton = QtWidgets.QPushButton(Dialog)
        self.DirectorManagerButton.setGeometry(QtCore.QRect(20, 310, 131, 41))
        self.DirectorManagerButton.setObjectName("pushButton_7")
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
        Dialog.setWindowTitle(_translate("Dialog", "图书馆长界面"))
        self.ManagerButton.setText(_translate("Dialog", "管理员管理"))
        self.ControlerButton.setText(_translate("Dialog", "操作员管理"))
        self.ReaderButton.setText(_translate("Dialog", "读者管理"))
        self.BooksBorrowButton.setText(_translate("Dialog", "图书借阅管理"))
        self.BooksBuyButton.setText(_translate("Dialog", "图书的订购与出售"))
        self.BooksManagerButton.setText(_translate("Dialog", "书籍管理"))
        self.DirectorManagerButton.setText(_translate("Dialog", "馆长信息修改"))
    def exit_func(self,Dialog):
        Dialog.close()
    def Show_BooksManager(self):
        Form1 = QtWidgets.QWidget()
        ui = Ui_BooksImport()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
#书籍管理操作
class Ui_BooksImport(object):
    def setupUi(self, BooksImport):
        BooksImport.setObjectName("BooksImport")
        BooksImport.resize(790, 589)
        self.tabWidget = QtWidgets.QTabWidget(BooksImport)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 771, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.ImportBtn = QtWidgets.QPushButton(self.tab)
        self.ImportBtn.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.ImportBtn.setObjectName("ImportBtn")
        self.ImportBtn.clicked.connect(self.ImportManager)

        self.BOOKS_SHOW = QtWidgets.QTableWidget(self.tab)
        self.BOOKS_SHOW.setGeometry(QtCore.QRect(20, 70, 731, 451))
        self.BOOKS_SHOW.setObjectName("BOOKS_SHOW")

        self.CommitJson = QtWidgets.QPushButton(self.tab)
        self.CommitJson.setGeometry(QtCore.QRect(200, 20, 121, 41))
        self.CommitJson.setObjectName("CommitJson")
        self.CommitJson.clicked.connect(self.PostInfo)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.QUERY_TEXT = QtWidgets.QLineEdit(self.tab_2)
        self.QUERY_TEXT.setGeometry(QtCore.QRect(220, 40, 161, 41))
        self.QUERY_TEXT.setObjectName("QUERY_TEXT")

        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(220, 90, 161, 41))
        self.comboBox.setObjectName("comboBox")

        self.EXIT = QtWidgets.QPushButton(self.tab_2)
        self.EXIT.setGeometry(QtCore.QRect(620, 40, 121, 41))
        self.EXIT.setObjectName("EXIT")
        self.QUERY_BTN = QtWidgets.QPushButton(self.tab_2)
        self.QUERY_BTN.setGeometry(QtCore.QRect(470, 40, 131, 41))
        self.QUERY_BTN.setObjectName("QUERY_BTN")
        self.QUERY_BTN.clicked.connect(self.SearchBooks)
        self.LABEL_Q = QtWidgets.QLabel(self.tab_2)
        self.LABEL_Q.setGeometry(QtCore.QRect(20, 40, 121, 41))
        self.LABEL_Q.setObjectName("LABEL_Q")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 721, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.CONDITION = QtWidgets.QComboBox(self.tab_2)
        self.CONDITION.setGeometry(QtCore.QRect(90, 40, 121, 41))
        self.CONDITION.setObjectName("CONDITION")
        Types_List = ['书名', '作者', '出版社', '读者对象']
        for item in Types_List:
            self.CONDITION.addItem(item)
        self.CONDITION.editTextChanged.connect(self.change_text)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(BooksImport)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BooksImport)
    def change_text(self):
        if self.CONDITION.currentText().strip() == "读者对象":
            self.QUERY_TEXT.setEnabled(False)
            self.comboBox.setEnabled(True)
        else:
            self.QUERY_TEXT.setEnabled(True)
            self.comboBox.setEnabled(False)
        pass

    def retranslateUi(self, BooksImport):
        _translate = QtCore.QCoreApplication.translate
        BooksImport.setWindowTitle(_translate("BooksImport", "书籍管理"))
        self.ImportBtn.setText(_translate("BooksImport", "书籍导入"))
        self.CommitJson.setText(_translate("BooksImport", "提交文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BooksImport", "书籍导入"))
        self.EXIT.setText(_translate("BooksImport", "退出"))
        self.QUERY_BTN.setText(_translate("BooksImport", "查询"))
        self.LABEL_Q.setText(_translate("BooksImport", "查询条件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BooksImport", "书籍删除与修改"))
    #导入书籍的操作
    def ImportManager(self):
        files, ok1 = QtWidgets.QFileDialog.getOpenFileName(None,caption="图书文件导入",filter="xls Files (*.xls)|(*.XLS);;xlsx Files (*.xlsx)|(*.XLSX)")
        if files != "":
            data = process_xls(files)
            # 表头
            # LIST_NAME = ['BookName','bookClass', 'editorName', 'press', 'time', 'price', 'summary', 'number']
            Headers = ['书名','类别','著者','出版社','出版时间','价格','摘要','订数']
            self.BOOKS_SHOW.setColumnCount(len(Headers))
            self.BOOKS_SHOW.setRowCount(len(data)-1)
            self.BOOKS_SHOW.setHorizontalHeaderLabels(Headers)
            self.BOOKS_SHOW.verticalHeader().setVisible(True)
            self.BOOKS_SHOW.setHorizontalHeaderLabels(Headers)
            self.BOOKS_SHOW.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.BOOKS_SHOW.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
            self.BOOKS_SHOW.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
            for index in range(self.BOOKS_SHOW.columnCount()):
                headItem = self.BOOKS_SHOW.horizontalHeaderItem(index)
                headItem.setFont(QtGui.QFont("song", 12,QtGui.QFont.Bold))
                headItem.setForeground(QtGui.QBrush(QtCore.Qt.gray))
                headItem.setTextAlignment(QtCore.Qt.AlignLeft |QtCore.Qt.AlignVCenter)
            self.BOOKS_SHOW.setColumnWidth(4, 400)
            self.BOOKS_SHOW.setRowHeight(0, 40)

            # 数据的总量
            Length = len(data)
            LIST_NAME = ['BookName','bookClass','editorName', 'press', 'time', 'price', 'summary', 'number']
            for index in range(Length):
                for k in range(len(LIST_NAME)):
                    self.BOOKS_SHOW.setItem(index,k,QtWidgets.QTableWidgetItem(str(data[index][LIST_NAME[k]])))
            # 将带待发送的信息缓存到本地目录上
            All_data = {
                "number": "1000000002",
                "bookInfo": data
            }
            with open(os.path.join("cache","books.json"),"w",encoding="utf-8") as f:
                json.dump(All_data, f)
        else:
            pass
    #提交书籍的操作
    def PostInfo(self):
            #　将书籍的信息发送给服务器端口
            with open(os.path.join("cache","books.json"),"r",encoding="utf-8") as f:
                All_data = json.load(f)
                ip_address = "192.168.43.205"
                try:
                    result = post_books_data(All_data,ip_address)
                    if result:
                        QtWidgets.QMessageBox.information(None, "提示信息", "图书上传成功!", QtWidgets.QMessageBox.Yes)
                    else:
                        QtWidgets.QMessageBox.warning(None, "错误提示", "图书上传失败!", QtWidgets.QMessageBox.Yes)

                except requests.exceptions.ConnectionError:
                    QtWidgets.QMessageBox.warning(None, "错误提示", "请检查网络设置!", QtWidgets.QMessageBox.Yes)
    #查询图书操作
    def SearchBooks(self):
        post_search = {
            "itemName":[self.CONDITION.currentText().strip()],
            "itemData":[self.QUERY_TEXT.text().strip()]
        }
        ip_address = "192.168.43.205"
        url = "http://" + ip_address + ":8080/LibrarySystem/AlterTable"
        try:
            result = requests.post(url,post_search)

        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(None,"错误提示","请检查网络状态！",QtWidgets.QMessageBox.Yes)
        # if self.CONDITION