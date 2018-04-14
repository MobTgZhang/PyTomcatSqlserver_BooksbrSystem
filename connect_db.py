import json
import os
import requests
import pprint
# 处理中文乱码的问题
# 获取服务器中的读者编号
def get_number_usr(type,ip_address):
    url = "http://" + ip_address + ":8080/LibrarySystem/RegisterFirst"
    data = str(type)
    result = requests.post(url,data= data)
    return result.text
# 获取服务器上的姓名和密码,检查登陆是否成功
def get_user_name(type,name,passwd,ip_address):
    url = "http://" + ip_address + ":8080/LibrarySystem/Login"
    data = "{loginClass:%d,loginName:\"%s\",loginPw:\"%s\"}"%(type,name,passwd)
    result = requests.post(url,data)
    return result.text.strip() == "true"
#向服务器端发送基本信息，然后获取信息
def Post_Data(dict_data):
    '''
    :param dict_data:
    dict_data = {
        'SearchClass':number,
        'start':start,
        'end':end,
        'itemName':itemName
        'itemDate':itemDate
    }
    :return:
    '''
    #SearchClass, start, end, itemName, itemDate
    pass
# 获取服务器上的读者基本信息,并将读者的基本信息加载
def get_user_basic_data(Type,ip_address):
    with open(os.path.join("cache", "UserLoginData.json"), "r") as file:
        datas = json.load(file)
        name = datas['name']
        passwd = datas['password']
        try:
            url = "http://" + ip_address + ":8080/LibrarySystem/ConditionSearchTable"
            data = "{\"SearchClass\":%d,\"start\":%d,\"end\":%d,\"itemName\":[\"登录名\",\"密码\"],\"itemDate\":[\"%s\",\"%s\"]}" % (Type,1,2, name, passwd)
            data = data.encode("utf-8")
            result = requests.post(url, data)
            data = eval(result.text)
            #解析服务器端口发送过来的信息
            itemData = data[0]['itemDate']
            itemName = data[0]['itemName']
            #将数据变为字典格式
            dict_data = dict(zip(itemName,itemData))
            # 将读取到的读者基本信息缓存到文件Reader.json
            with open(os.path.join("cache", "UserDataFile.json"),"w",encoding="utf-8") as file:
                json.dump(dict_data, file)
            return True
        except requests.ConnectionError:
            return False
# 保存注册信息
def save_db_reader(data_dict,ip_address):
    url = "http://" + ip_address + ":8080/LibrarySystem/Register"
    data = str(data_dict)
    data = data.encode("utf-8")
    result = requests.post(url, data)
    if result.text.strip()== "false":
        return False
    return True
#修改用户信息名称
def alter_data(dict_data,ip_address):
    '''
        dict_data = {
            "登陆名":Reg_Name,
            "密码":password,
            "读者号":Reader_Number,
            "姓名":Reader_Name,
            "最大可借数量":int(Book_Num_MAX),
            "联系方式":communication,
            "年龄":int(age),
            "已借数量":int(Book_Num_HAVE)
        }
    '''
    url = "http://" + ip_address + ":8080/LibrarySystem/AlterTable"
    # 将传入的字符穿转化为可读取的json 格式
    # [\"读者号\",\"姓名\",\"年龄\",\"联系方式\",\"最大可借数量\",\"已借数量\"]
    upload_str = "{\"tableClass\":%d," \
                 "\"alterData\":[\"%s\",\"%s\",%d,\"%s\",%d,%d,\"%s\",\"%s\"]," \
                 "\"alterConditionName\":[\"读者号\"]," \
                 "\"alterConditionData\":[\"%s\"]}" %\
                 (4,dict_data['读者号'],dict_data['姓名'],dict_data['年龄'],dict_data['联系方式'],
                  dict_data['最大可借数量'],dict_data['已借数量'],dict_data['登录名'],dict_data['密码'],dict_data['读者号'])
    try:
        upload_str = upload_str.encode("utf-8")
        result = requests.post(url,upload_str)
        return result.text.strip() == "true"
    except requests.ConnectionError:
        return False
#将书籍信息post给服务器端口
def post_books_data(books_data,ip_address):
    All_Data = json.dumps(books_data)
    url = "http://" + ip_address + ":8080/LibrarySystem/ImportBook"
    try:
        result = requests.post(url,All_Data)
        return result.text.strip() == "true"
    except requests.exceptions.ConnectionError:
        return False