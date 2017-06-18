import urllib.request
import os
import sys
import re
import random
import xlrd
import multiprocessing
import time

HeadKey = 'User-Agent'
HeadVal = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

proxies = []

def creatDir(pathname):   #ok
    if not os.path.exists(pathname):
        os.mkdir(pathname)
    os.chdir(pathname)

    
def getProxyFormFile(filename):  #ok
    global proxies
    if not os.path.exists(filename):
        print('Proxy文件不存在，请检查！')
        sys.exit(-1)
    
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    
    nrows = table.nrows #获取当前页中有多少行数据

    for row in range(nrows):
        proxies.append(table.row_values(row))


def changeProxy():   #ok
    global proxies
    proxy = random.choice(proxies)
    #print(proxy)
    proxy_support = urllib.request.ProxyHandler({proxy[0]:proxy[1]})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders =  [(HeadKey, HeadVal)]
    urllib.request.install_opener(opener)
    #print('智能切换代理：%s' % (proxy))

def UrlOpen(url): #ok

    req = urllib.request.Request(url)
    req.add_header(HeadKey, HeadVal)
    
    changeProxy()
    
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    return html

def UrlOpenWithoutProxy(url):   #ok
    req = urllib.request.Request(url)
    req.add_header(HeadKey, HeadVal)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def getTotalPage(url):   #ok
    html = UrlOpen(url)
    page_re = re.compile(r'</span>\d+<span')
    pageurl = page_re.findall(html)[-1]
    
    totalNum = int(pageurl[len('</span>'):-len('<span')])
    #print(totalNum)
    return totalNum

def savePic(picUrl):   #ok
    #print(picUrl)
    filename = picUrl.split("/")[-1]
    with open(filename, 'wb') as f:
        img = UrlOpenWithoutProxy(picUrl)
        f.write(img)


def getPicPerPage(urlList, page):    #ok
    print('当前页面：%d' % page)
    girlsUrl = []
    url = urlList[-1]
    html = UrlOpen(url+ '/page/%d/' % page)
    girl_re = re.compile(r'<li><a href=.+target="_blank"><img width=')
    girlList = girl_re.findall(html)  
    for girl in range(len(girlList)):
        girlUrl= girlList[girl].split('\"')[1]
        #print(girlUrl)
        #print(os.path.basename(girlUrl))
        girlsUrl.append(girlUrl)
    return girlsUrl
        #girlName = os.path.basename(girlUrl)
        #creatDir(girlName)

def getTotalNumPerGirl(url):     #ok
    html = UrlOpen(url)
    girl_re = re.compile(r'<span>\d+</span>')
    pageurl = girl_re.findall(html)[-1] 
    totalNum = int(pageurl[len('<span>'):-len('</span>')])
    #print(totalNum)
    return totalNum

                
def getTotalTitle(url):  #ok
    totalTitle = []
    html = UrlOpen(url)
    title_re = re.compile(r'<li><a title=.+href=.+</a></li>')
    titleurl = title_re.findall(html)  
    for num in range(len(titleurl)-1):
        titleList = titleurl[num].split('\"')
        totalTitle.append([titleList[1], titleList[3]])
    return totalTitle


def getGirlsPic(url, totalPage):
    totalTitle = []
    for i in range(totalPage):
        html = UrlOpen(url+'/%d' % (i+1))
        girl_re = re.compile(r'<img src=.+alt="')
        girl = girl_re.findall(html)[0]   #img src="http://i.meizitu.net/2017/05/06a06.jpg" alt="
        jpgPath = girl.split('\"')[1]
        print(jpgPath)
        savePic(jpgPath)

def getTotalPageForZiPai(url): 
    html = UrlOpen(url)
    page_re = re.compile(r'<span class=\'page-numbers current\'>\d+</span')
    pageurl = page_re.findall(html)[-1]
    
    totalNum = int(pageurl[len('<span class=\'page-numbers current\'>'):-len('</span')])
    print(totalNum)
    return totalNum

def getPicPerPageForZiPai(url, page):
    html = UrlOpen(url+ 'comment-page-%d/#comments' % page)
    jpg_re = re.compile(r'<p><img src=.+alt="美女自拍" /></p>')     #<p><img src="http://wx3.sinaimg.cn/mw1024/9d52c073gy1ffatai9vhuj20ia0odwht.jpg" alt="美女自拍" /></p>
    numurl = jpg_re.findall(html)  
    for pic in range(len(numurl)):
        jpgPath = numurl[pic].split('\"')[1]
        savePic(jpgPath)

'''        
def downloadPic(url, PicSavePath):
    creatDir(PicSavePath)
    totalTitle = getTotalTitle(url)
    #print(totalTitle)

    #抓取最后一个页面的美女    
    creatDir(totalTitle[-1][0])
    totalPage = getTotalPageForZiPai(totalTitle[-1][1]) 
    for i in range(totalPage):
        getPicPerPageForZiPai(totalTitle[-1][1] , totalPage-i)


    creatDir(PicSavePath)
    
    for i in range(len(totalTitle)-1):  #注意最后一个页面的格式与前面的不同，有差异，需要单独分析实现
        creatDir(totalTitle[i][0])    #生成各类型的目录   
        totalPage = getTotalPage(totalTitle[i][1])
        for j in range(totalPage):
            girlsUrl = getPicPerPage(totalTitle[i], j)
            for k in range(len(girlsUrl)):    #girlsUrl[0]=http://www.mzitu.com/91845
                totalPagePerGirl = getTotalNumPerGirl(girlsUrl[k])
                #print(totalPagePerGirl)
                girlName = os.path.basename(girlsUrl[k])
                if k > 0:
                    os.chdir('..')
                creatDir(girlName)   #在各类型下面生成对应美女的目录
                getGirlsPic(girlsUrl[k], totalPagePerGirl)


'''            
def multiProcessWork(titleList, PicSavePath):
    getProxyFormFile(proxyFile)
    creatDir(PicSavePath)
    creatDir(titleList[0])    #生成各类型的目录   
    totalPage = getTotalPage(titleList[1])
    for j in range(totalPage):
        girlsUrl = getPicPerPage(titleList, j)
        for k in range(len(girlsUrl)):    #girlsUrl[0]=http://www.mzitu.com/91845
            totalPagePerGirl = getTotalNumPerGirl(girlsUrl[k])
            #print(totalPagePerGirl)
            girlName = os.path.basename(girlsUrl[k])
            if k > 0:
                os.chdir('..')
            creatDir(girlName)   #在各类型下面生成对应美女的目录
            getGirlsPic(girlsUrl[k], totalPagePerGirl)

def multiProcessWork1(titleList, PicSavePath):
    getProxyFormFile(proxyFile)
    creatDir(PicSavePath)
    creatDir(titleList[0])
    totalPage = getTotalPageForZiPai(titleList[1]) 
    for i in range(totalPage):
        getPicPerPageForZiPai(titleList[1] , totalPage-i)
            
def downloadPic(url, PicSavePath):
    creatDir(PicSavePath)
    totalTitle = getTotalTitle(url)
    threads = []    
    
    #for i in range(len(totalTitle)-1):  #注意最后一个页面的格式与前面的不同，有差异，需要单独分析实现
    #for i in range(1):  #注意最后一个页面的格式与前面的不同，有差异，需要单独分析实现
        #print(i, totalTitle[i])
        #p = multiprocessing.Process(target=multiProcessWork, args = (totalTitle[i], PicSavePath))
        #threads.append(p)
        
    #抓取最后一个页面的美女
    #print(totalTitle[-1])
    p = multiprocessing.Process(target=multiProcessWork1, args = (totalTitle[-1], PicSavePath))
    threads.append(p)
    p.start()
    #multiProcessWork(totalTitle[0], PicSavePath)
    #multiProcessWork1(totalTitle[-1], PicSavePath)
    #print(len(threads))
    #for i in range(len(threads)):
        #threads[i].start()

    time.sleep(30) 
    
    print("END!!!!!!!!!!!!!!!!!")


if __name__ == '__main__':
    PicSavePath = 'D:\妹子网1'
    proxyFile = 'proxy.xlsx'
    url = 'http://www.mzitu.com/'

    getProxyFormFile(proxyFile)
    downloadPic(url, PicSavePath)


