from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#主界面显示
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        #设置窗口属性操作
        self.setWindowTitle(self.tr("读者摘要文档编辑器"))
        # 显示中心部件
        self.showWidget = ShowWidget()
        self.setCentralWidget(self.showWidget)
        #各菜单项
        self.fileMenu = QtWidgets.QMenu(self)  #文件菜单
        self.zoomMenu = QtWidgets.QMenu(self)  #缩放菜单
        self.rotateMenu = QtWidgets.QMenu(self)  #旋转
        self.mirrorMenu = QtWidgets.QMenu(self)  #镜像
        #放置图片
        self.img = QtGui.QImage()
        self.filename = ""      #打开文件名
        self.curFilename = ""   #保存文件名
        #查找对话框
        self.linelable = QtWidgets.QLabel(self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.findNextBtn = QtWidgets.QPushButton(self)
        self.cancelBtn = QtWidgets.QPushButton(self)

        self.directLabel = QtWidgets.QLabel(self)
        self.upBtn = QtWidgets.QRadioButton(self)
        self.downBtn = QtWidgets.QRadioButton(self)
        self.lowOrUpperBox = QtWidgets.QCheckBox(self)
        #替换对话框
        self.linelabel21 = QtWidgets.QLabel(self)  #查找
        self.lineEdit21 = QtWidgets.QLineEdit(self)#查找内容
        self.linelabel22 = QtWidgets.QLabel(self)#替换
        self.lineEdit22 = QtWidgets.QLineEdit(self)# 替换内容
        self.findNextBtn2 = QtWidgets.QPushButton(self)#查找下一个
        self.subBtn2 = QtWidgets.QPushButton(self)#替换按钮
        self.cancelBtn2 = QtWidgets.QPushButton(self)
        self.directLabel2 = QtWidgets.QLabel(self)
        self.lowOrUpperBox2 = QtWidgets.QCheckBox(self)
        self.findjudge = False
        #文件菜单项
        self.openFileAction = QtWidgets.QAction(QtGui.QIcon("open.png"),self.tr("打开"),self) #打卡文件操作
        self.NewFileAction = QtWidgets.QAction() #新建文件的操作
        self.SaveAction = QtWidgets.QAction() #保存文件的操作
        self.SaveAsAction = QtWidgets.QAction() #另存为文件
        self.PrintTextAction = QtWidgets.QAction() #打印文本动作
        self.PrintImageAction = QtWidgets.QAction() #打印图片动作
        self.exitAction = QtWidgets.QAction() #退出动作
        #编辑菜单项
        self.copyAction = QtWidgets.QAction() #复制动作
        self.cutAction = QtWidgets.QAction() #剪切操作
        self.pasteAction = QtWidgets.QAction() #粘贴操作
        self.findAction = QtWidgets.QAction() #查找
        self.subAction = QtWidgets.QAction() #替换
        self.aboutAction = QtWidgets.QAction() #关于
        self.zoomInAction = QtWidgets.QAction() #放大
        self.zoomOutAction = QtWidgets.QAction() #缩小
        #旋转菜单栏的操作　图像处理
        self.rotate90Action = QtWidgets.QAction() #90
        self.rotate180Action = QtWidgets.QAction() #180
        self.rotate270Action = QtWidgets.QAction() #270
        #镜像菜单栏
        self.mirrorVerticalAction = QtWidgets.QAction() #垂直镜像
        self.mirrorHorizonAction = QtWidgets.QAction() #水平镜像
        self.undoAction = QtWidgets.QAction() #撤销
        self.redoAction = QtWidgets.QAction() #取消撤销
        #工具栏
        self.fileTool = QtWidgets.QToolBar() #文件---打开、新建、保存、另存为、打印文本图像
        self.zoomTool = QtWidgets.QToolBar() #缩放
        self.rotateTool = QtWidgets.QToolBar() #旋转
        self.mirrorTool = QtWidgets.QToolBar() #镜像
        self.doToolBar = QtWidgets.QToolBar() #撤销、回撤　--操作
        # 文本编辑
        self.fontLabel = QtWidgets.QLabel() #字体设置项
        self.fontComboBox = QtWidgets.QFontComboBox() #字体选框
        self.fontLabel2 = QtWidgets.QLabel() #大小
        self.sizeComboBox = QtWidgets.QComboBox() #大小选框
        self.boldBox = QtWidgets.QToolButton() #加粗按钮
        self.italicBox = QtWidgets.QToolButton() #斜体
        self.underlineBtn = QtWidgets.QToolButton() #下划线
        self.colorBtn = QtWidgets.QToolButton() #字体颜色
        self.colorBackBtn = QtWidgets.QToolButton() #背景颜色按钮
        self.fontToolBar = QtWidgets.QToolBar() #字体工具栏
        #排序设置项
        self.listLabel = QtWidgets.QLabel()
        self.listComboBox = QtWidgets.QComboBox()
        self.actGrp = QtWidgets.QActionGroup(self)
        self.leftAction = QtWidgets.QAction() #居左
        self.rightAction = QtWidgets.QAction() #居右
        self.centerAction = QtWidgets.QAction() #居中
        self.justifyAction = QtWidgets.QAction() #两端对齐
        self.listToolBar = QtWidgets.QToolBar() #排序工具栏

        #排序
        listlabel = QtWidgets.QLabel(self.tr("排序"))
        listComboBox = QtWidgets.QComboBox()
        listComboBox.addItem("Standard")
        listComboBox.addItem("QTextListFormat::ListDisc")#// 圆盘
        listComboBox.addItem("QTextListFormat::ListCircle")# // 圆
        listComboBox.addItem("QTextListFormat::ListSquare")# // 方形
        listComboBox.addItem("QTextListFormat::ListDecimal")# // 十进制
        listComboBox.addItem("QTextListformat::ListLowerAlpha")#; // 小写字母
        listComboBox.addItem("QTextListFormat::ListUpperAlpha")# // 大写字母
        listComboBox.addItem("QTextListformat::ListLowerRoman")# // 小写罗马字符
        listComboBox.addItem("QTextListFormat::ListUpperRoman")# // 大写罗马字符
        #在工具栏上嵌入控件: 字体，大小，粗体，斜体，字体颜色
        # 字体 - -这里的字体，字号仅仅是下拉列表框改变
        fontlabel = QtWidgets.QLabel(self.tr("字体"))
        fontComboBox = QtWidgets.QFontComboBox
        #setFontFilter - -接口过滤(只在下拉列表框中显示某一类字体, 默认情况下为QFontComboBox::AllFonts
        #                                                              // 列出所有字体
        #fontComboBox.setFontFilters(QtWidgets.QFontComboBox.ScalableFonts)
        fontlabel2 = QtWidgets.QLabel(self.tr("字号"))
        sizeComboBox = QtWidgets.QComboBox()
        '''
        / ** QFontDatabase - 实现在字号下拉列表框中填充各种不同的字号条目
        *其用于表示当前系统中所有可用的格式信息, 主要是字体和字号大小
        *provide
        information
        about
        the
        fonts
        avaliable in the
        underlying(潜在)
        window
        system * /
        '''
        db = QtGui.QFontDatabase()
        # standardSize(): return a list of standard font size(返回可用标准字号的列表).
        for size in db.standardSizes():
            # 将它们插入到字号下拉框中
            sizeComboBox.addItem(str(size))
        # 加粗
        self.boldBtn = QtWidgets.QToolButton()
        self.boldBtn.setIcon(QtGui.QIcon("bold.png"))
        # //设置成是否是开关(toggle)按钮(true)---即可复选的
        self.boldBtn.setCheckable(True)
        # 斜体
        self.italicBtn = QtWidgets.QToolButton()
        self.italicBtn.setIcon(QtGui.QIcon("italic.png"))
        self.italicBtn.setCheckable(True)
        # 下划线
        self.underlineBtn = QtWidgets.QToolButton()
        self.underlineBtn.setIcon(QtGui.QIcon("underline.png"))
        self.underlineBtn.setCheckable(True)
        #颜色
        self.colorBackBtn = QtWidgets.QToolButton()
        self.colorBackBtn.setIcon(QtGui.QIcon("color.png"))
        self.colorBackBtn.setCheckable(True)
        # 背景颜色
        self.colorBackBtn = QtWidgets.QToolButton()
        self.colorBackBtn.setIcon(QtGui.QIcon("color.png"))
        self.colorBackBtn.setCheckable(True)

        #　创建动作、菜单、工具栏函数
        self.createActions()
        self.createMenus()
        self.createToolBars()

    #　Some of public functions
    #　创建动作
    def createActions(self):
        #　基于文件操作的动作(Action)的代码
        #  “打开”动作
        # 在创建“打开文件”动作的同时, 指定了此动作使用的图标、名称及父窗口
        self.openFileAction.setShortcut(self.tr("Ctrl+O"))
        self.setStatusTip(self.tr("打开一个文件"))
        self.openFileAction.triggered.connect(self.ShowOpenFile)
        # 新建动作
        self.NewFileAction = QtWidgets.QAction(QtGui.QIcon("new.png"),self.tr("新建"),self)
        self.NewFileAction.setShortcut(self.tr("Ctrl+N"))
        self.NewFileAction.setStatusTip(self.tr("新建一个文件"))
        self.NewFileAction.triggered.connect(self.ShowNewFile)
        # 保存
        self.SaveAction = QtWidgets.QAction(QtGui.QIcon("save.png"),self.tr("保存"),self)
        self.SaveAction.setShortcut(self.tr("Ctrl+S"))
        self.SaveAction.setStatusTip(self.tr("保存一个文件"))
        # 另存为
        self.SaveAsAction = QtWidgets.QAction(self.tr("另存为"),self)
        self.SaveAsAction.setShortcut(self.tr("Ctrl+alt+S"))
        self.SaveAsAction.setStatusTip(self.tr("另存为"))
        self.SaveAsAction.triggered.connect(self.ShowSaveAsFile)
        # 退出动作
        self.exitAction = QtWidgets.QAction(self.tr("退出"))
        self.exitAction.setShortcut(self.tr("Ctrl+Q"))
        self.exitAction.setStatusTip(self.tr("退出程序"))
        self.exitAction.triggered.connect(self.close)
        # 复制动作
        self.copyAction = QtWidgets.QAction(QtGui.QIcon("copy.png"),self.tr("复制"),self)
        self.copyAction.setShortcut(self.tr("Ctrl+C"))
        self.copyAction.setStatusTip(self.tr("复制"))
        #self.copyAction.triggered.connect(self)

    # 创建菜单
    def createMenus(self):
        pass
    # 创建工具栏
    def createToolBars(self):
        pass
    # 加载文件
    def loadFiles(self):
        pass
    # 合并格式
    def mergeFormat(self):
        pass
    #　Some of protected functions
    # 新建文件
    def ShowNewFile(self):
        pass
    # 打开文件
    def ShowOpenFile(self):
        pass
    # 保存文件
    def ShowSaveFile(self):
        pass
    # 另存为
    def ShowSaveAsFile(self):
        pass
    # 查找对话框
    def ShowFindDialog(self):
        pass
    # 查找
    def ShowFindText(self):
        pass
    def ShowFindStr(self):
        pass
    # 替换对话框
    def ShowSubDialog(self):
        pass
    # 替换对话框
    def ShowSubstitute(self):
        pass
    def ShowSubText(self):
        pass
    def ShowSubText2(self):
        pass
    def ShowFindStr2(self):
        pass
    # 打印文本
    def ShowPrintText(self):
        pass
    # 打印图像
    def ShowPrintImage(self):
        pass
    # 放大功能
    def ShowZoomIn(self):
        pass
    # 缩小功能
    def ShowZoomOut(self):
        pass
    # 旋转90
    def ShowRotate90(self):
        pass
    def ShowRotate180(self):
        pass
    def ShowRotate270(self):
        pass
    # 镜像--纵向镜像
    def ShowMirrorVertical(self):
        pass
    # 横向镜像
    def ShowMirrorHorizontal(self):
        pass
    # 显示字体框
    def ShowFontComboBox(self,mystr):
        pass
    # 大小自旋盒
    def ShowSizeSpinBox(self,spinValue):
        pass
    #　加粗功能
    def ShowBoldBtn(self):
        pass
    # 显示斜体
    def ShowItalicBtn(self):
        pass
    # 下划线
    def ShowItalicBtn(self):
        pass
    def ShowColorBtn(self):
        pass
    # 背景颜色
    def ShowBackColorBtn(self):
        pass
    #字符格式化
    def ShowCurrentFormatChanged(self,fmt):
        pass
    #排序
    def ShowList(self,index):
        pass
    # 对齐方式
    def ShowAlignment(self,act):
        pass
    # 显示光标的位置
    def ShowCursorPositionChanged(self):
        pass
#显示中心部件
class ShowWidget(QtWidgets.QWidget):
    def __init__(self):
        super(ShowWidget,self).__init__()
        self.img = QtGui.QImage()
        self.imagelabel = QtWidgets.QLabel(self)
        self.text = QtWidgets.QTextEdit(self)
        self.imagelabel.setScaledContents(True)
        self.text = QtWidgets.QTextEdit(self)
        mainLayout = QtWidgets.QHBoxLayout(self)
        mainLayout.addWidget(self.imagelabel)
        mainLayout.addWidget(self.text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())