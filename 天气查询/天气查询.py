#-*- coding:utf8 -*-;
import urllib.request,urllib.parse,json,pickle;
print("============================================天气查询============================================");
while True:
    cityName = input("请输入城市:");
    if cityName=='q':
        print("感谢使用威威天气查询系统，期待您的下次使用!!!");
        break;

    f = open('data.pkl','rb');
    city = pickle.load(f);
    cityCode = city.get(cityName,'0');
    if cityCode=='0':
        print('您输入的城市不存在!');
        exit();
    url = 'http://apis.baidu.com/heweather/weather/free?city=wuhan';
    req = urllib.request.Request(url);
    req.add_header('apikey','9c72cc51f8c5c9cd8313e2827254a333');
    result = urllib.request.urlopen(req);
    content = result.read().decode('UTF-8');
    if(content):
        print(content)
    print("退出查询请输入q");




