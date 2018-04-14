import xlrd
import pprint
import json
# 将书籍生成对应的格式
def process_xls(FileDir):
    DataS = xlrd.open_workbook(FileDir)
    sheet1 = DataS.sheet_by_index(0)
    NUM_LISTS = [1,9,2,8,7,6,11,5]
    LIST_NAME = ['BookName', 'bookClass', 'editorName', 'press', 'time', 'price', 'summary', 'number']
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
            if DICT_INDEX_NAME[k] =="number":
                temp[DICT_INDEX_NAME[k]] = int(rowData[k])
        All_DATA.append(temp)
    return All_DATA