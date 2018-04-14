import xlrd
import os
import pprint
import json
from XLS_FILE_PROCESS import process_xls
'''
def process_xls(FileDir):
    DataS = xlrd.open_workbook(FileDir)
    sheet1 = DataS.sheet_by_index(0)
    NUM_LISTS = [1, 2, 8, 7, 6, 11, 5]
    LIST_NAME = ['BookName', 'editorName', 'press', 'time', 'price', 'summary', 'number']
    rowData = sheet1.row_values(0)
    for index in range(len(NUM_LISTS)):
        LIST_NAME.append(rowData[NUM_LISTS[index]])
    DICT_INDEX_NAME = dict(zip(NUM_LISTS, LIST_NAME))
    # 所有的图书的集合
    All_DATA = []
    for index in range(1, sheet1.nrows - 1):
        rowData = sheet1.row_values(index)
        # 每一列进行遍历的操作
        # 生成一条记录
        temp = {}
        for k in NUM_LISTS:
            temp[DICT_INDEX_NAME[k]] = rowData[k]
        All_DATA.append(temp)
    return All_DATA
'''
Test_File = "/media/asus/000E5A090009CE72/Users/MobtgZhang/Desktop/数据库作业/图书管理/2017年第二十七批中文图书拟采购目录.XLS"
MyData = xlrd.open_workbook(Test_File)
data = process_xls(Test_File)
pprint.pprint(data)
exit()
if not os.path.exists(Test_File):
    os.mkdir("TestFile")
sheet1 = MyData.sheet_by_index(0)
# 图书表的创建
# 0,1,2,3,4,5,6,7,8,9,10,11
# '序号', '题名', '著者', '标准号', '分类号', '订数', '人民币价格', '出版日期', '出版社', '读者对象', '页码', '摘要'
# 0       1       2      3         4         5      6          7           8        9         10     11
# 1,2,6,7,8,9,11
NUM_LISTS = [1,9,2,8,7,6,11,5]
LIST_NAME = ['BookName','bookClass','editorName','press','time','price','summary','number']
rowData=sheet1.row_values(0)
for index in range(len(NUM_LISTS)):
    LIST_NAME.append(rowData[NUM_LISTS[index]])
DICT_INDEX_NAME = dict(zip(NUM_LISTS,LIST_NAME))
pprint.pprint(DICT_INDEX_NAME)
#所有的图书的集合
All_DATA = []
for index in range(1,sheet1.nrows-1):
    print("AAAA")
    rowData=sheet1.row_values(index)
    #每一列进行遍历的操作
    #生成一条记录
    temp = {}
    for k in NUM_LISTS:
        temp[DICT_INDEX_NAME[k]] = rowData[k]
    All_DATA.append(temp)
pprint.pprint(All_DATA)