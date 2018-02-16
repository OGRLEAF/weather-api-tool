# coding=utf-8
import urllib, urllib2, sys, json, os, shutil
from prettytable import PrettyTable

#测试数据
city= "济宁"
appcode = 'fd940d35c8394c988beb13608e8a7bd9'

#阿里云天气API
def getweather(appcode,city):
    host = 'http://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    method = 'GET'
    querys = 'city=' + city
    bodys = {}
    url = host + path + '?' + querys

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    return content;

#保存配置信息
def save():

    city = raw_input("Your City: ")
    #组建字典
    config_content = {'function':'config'}
    config_content['appcode'] = appcode
    config_content['city'] = city

    file = "config.json"
    if (os.path.exists(file)):
        config = open(file).read()
        #print type(config)
        #print config
    else:
        config = open("config.json","w")
        config.write(config_content);
save()
content = getweather(appcode,city)
if (content):
    #print(content)
    #print type(content)
    #data = json.loads(content)                    #将字符串转换为字典（json方式）
    data = eval(content)                           #将字符串转换为字典（eval函数）（正确的方式）
    #print type(data)
    msg = data['msg']

    cityid = data['result']['cityid']
    cityname = data['result']['city']
    date = data['result']['date']
    present_weather = data['result']['weather']
    present_temp = data['result']['temp']
    present_wind = data['result']['winddirect']

    print "获取数据……" + msg  + "\n"  + "城市ID……"  + cityid
    #print "------------------------------------------------"
    #print "|--CITY--|----DATE----|--WEATHER--|--TEMP--|--WIND--|"
    #print "|  " + cityname + "  | " + date + " |           " + present_weather + "       | " + present_temp + "     | " + present_wind + " | "
    table = PrettyTable(["城市","日期","天气","温度","风况"])
    table.add_row([cityname, date, present_weather, present_temp, present_wind])
    print table
