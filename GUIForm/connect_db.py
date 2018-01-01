import json
import os
import requests
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
# 获取服务器上的读者基本信息,并将读者的基本信息加载
def get_user_basic_data(ip_address):
    with open(os.path.join("cache", "UserLoginData.jsq"), "r") as file:
        datas = json.load(file)
        name = datas['name']
        passwd = datas['password']
        url = "http://" + ip_address + ":8080/LibrarySystem/BasicInfo"
        data = "{loginClass:%d,loginName:\"%s\",loginPw:\"%s\"}" % (3, name, passwd)
        result = requests.post(url, data)
        print(result.content.decode("utf-8"))
        return
# 获取服务器上的用户登陆名
def get_name(type,ip_address):
    pass
# 保存注册信息
def save_db_reader(data_dict,ip_address):
    url = "http://" + ip_address + ":8080/LibrarySystem/Register"
    data = str(data_dict)
    result = requests.post(url, data)
    if result.text.strip()== "false":
        return False
    return True