import urllib.request
import os
import random

def UrlOpen(url):

    #print(url)
    req = urllib.request.Request(url)
    key = 'User-agent'
    val = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
    req.add_header(key, val)

    #增加代理！
    '''
    proxies = ['119.254.92.53:80']
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http':proxy})

    opener = urllib.request.build_opener(proxy_support)

    opener.add_headers = (key, val)
    urllib.request.install_opener(opener)
    '''
    response = urllib.request.urlopen(req)

    html = response.read()

    
    return html


def GetPage(url):

    html = UrlOpen(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    #print(html[a:b])

    return html[a:b]
    
def FindImgs(url):
    html = UrlOpen(url).decode('utf-8')
    ImgAddrs = []

    a = html.find('img src=')
    
    while a != -1:
        b = html.find('.jpg', a, a+100)
        if b != -1:
            TmpHtml = html[a+9:b+4]
            c = TmpHtml.find('http')
            if c != -1:
                ImgAddrs.append(TmpHtml)
            else:
                ImgAddrs.append('http:'+TmpHtml)
        else:
            b = a + 9

        a = html.find('img src=', b)

    #for i in ImgAddrs:
     #   print(i)


    return ImgAddrs



def SaveImgs(folder, addrs):
    for each in addrs:
        
        filename = each.split("/")[-1]
        with open(filename, 'wb') as f:
            img = UrlOpen(each)
            f.write(img)



def DownloadMM(folder = 'OOXX', pages = 10):

    try:
        os.mkdir(folder)
    except FileExistsError:
        print("当前路径下%s目录存在" %(folder))
        
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    PageNum = int(GetPage(url))

    for i in range(pages):
        PageNum -= i
        PageUrl = url + 'page-' + str(PageNum) + '#comments'
        #print(PageUrl)
        ImgAddrs = FindImgs(PageUrl)

        SaveImgs(folder, ImgAddrs)
    


if __name__ == '__main__':
    DownloadMM(pages = 100)
