import re
import urllib.request
from openpyxl import Workbook
import requests

httpProxy = []  #定义http协议的代理IP列表

HeadKey = 'User-Agent'
HeadVal = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

def checkProxyValid(ip, typeName): #验证传入的代理IP是否有效
    try:
        requests.get('http://www.baidu.com', proxies={typeName:typeName+'//'+ip})
    except:
        return False
    else:
        return True

def UrlOpen(url):
    req = urllib.request.Request(url)
    req.add_header(HeadKey, HeadVal)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    return html

def getProxy(url, typeName):     #从IP代理网站上抓取代理IP，存入Proxy列表中
    global httpProxy
    html = UrlOpen(url)
    IP = re.compile(r'''<tr\sclass=.+>\s+
                                    <td\sclass=.+</td>\s+
                                    <td>.+</td>\s+
                                    <td>.+</td>\s+
                                    <td>\s+
                                    <a\shref=.+</a>\s+
                                    </td>\s+
                                    <td\sclass=.+</td>\s+
                                    <td>.+</td>\s+
                                    ''',re.VERBOSE)
    
    proxy_ip = IP.findall(html)
    for num in range(len(proxy_ip)):
        ipList = []
        protocol_list = proxy_ip[num].split()
        protocol = protocol_list[-1].split(">")
        HTTP = protocol[1].split("<")
        PORT_list = proxy_ip[num].split()
        PORT = PORT_list[8].split(">")
        PO = PORT[1].split("<")
        ip_list = proxy_ip[num].split()
        ip = ip_list[7].split(">")        
        IP = ip[1].split("<")
        #print(IP)
        if HTTP[0] == typeName:
            IP_list = IP[0]+":"+PO[0]
            ipList.append(typeName)
            if checkProxyValid(IP_list, typeName):
                ipList.append(IP_list)
                httpProxy.append(ipList)


if __name__ == "__main__":
    file = "proxy.xlsx"
    url = "http://www.xicidaili.com/"
    getProxy(url+'wt/', 'HTTP')
    getProxy(url+'wn/', 'HTTPS')

    wb = Workbook()
    ws = wb.active
    ws.title = 'proxy'

    for row in httpProxy:
        ws.append(row)


    wb.save(file)
    

