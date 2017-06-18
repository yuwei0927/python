import urllib.request
import os
import sys
import re
import random
import xlrd
import time
import urllib.error

HeadKey = 'User-Agent'
HeadVal = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

proxies = []


def getProxyFormFile(filename):
    if not os.path.exists(filename):
        print('Proxy文件不存在，请检查！')
        sys.exit(-1)
    
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    
    nrows = table.nrows #获取当前页中有多少行数据

    for row in range(nrows):
        proxies.append(table.row_values(row))


def changeProxy():
    proxy = random.choice(proxies)
    #print(proxy)
    proxy_support = urllib.request.ProxyHandler({proxy[0]:proxy[1]})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders =  [(HeadKey, HeadVal)]
    urllib.request.install_opener(opener)
    #print('智能切换代理：%s' % (proxy))

def UrlOpen(url):

    req = urllib.request.Request(url)
    req.add_header(HeadKey, HeadVal)
    
    changeProxy()
    
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    return html

def UrlOpenWithoutDecode(url):
    req = urllib.request.Request(url)
    req.add_header(HeadKey, HeadVal)
    changeProxy()
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def getTotalPage(url):
    html = UrlOpen(url)
    find_string = 'current-comment-page'
    find_start = html.index(find_string) + len(find_string) + 3
    find_end = html.index(']',find_start+1)
    totalNum = int(html[find_start:find_end])
    return totalNum

def savePic(picUrl):
    #print(picUrl)
    filename = picUrl.split("/")[-1]
    try:
        with open(filename, 'wb') as f:
            img = UrlOpenWithoutDecode(picUrl)
            f.write(img)
            #time.sleep(0.3)   # 休眠0.3秒
    except urllib.error.URLError as e:
        print('保存图片失败，重试中...')
        #time.sleep(1)
        #savePic(picUrl)
        return


def getPicPerPage(url, page):
    #print('当前页面：%d' % page)
    cnt = 1
    html = UrlOpen(url+ '/page-%d' % page)
    jpg_re = re.compile(r'<img src="//.*\.(?:jpg|jpeg)')
    numurl = jpg_re.findall(html)  
    for pic in range(len(numurl)):
        jpgPath = numurl[pic].split('\"')[-1]
        print('正在保存第%d页，第%d张图片：%s' % (page, cnt, jpgPath))
        savePic('http:'+jpgPath)
        cnt += 1
        

def downloadPic(url):
    totalPage = getTotalPage(url)
    #totalPage = 23
    #print(totalPage)
    for i in range(totalPage):
        getPicPerPage(url, totalPage-i)

   
if __name__ == '__main__':
    PicSavePath = 'D:\ooxx'
    proxyFile = 'proxy.xlsx'
    url = 'http://jandan.net/ooxx'

    getProxyFormFile(proxyFile)
    if not os.path.exists(PicSavePath):
        os.mkdir(PicSavePath)
    os.chdir(PicSavePath)
    downloadPic(url)


