import re
import urllib.request
#import os
#import http.server
#import http.client
#from urllib.error import URLError, HTTPError
#import urllib.parse

KernelAddrs = []

def UrlOpen(url):
    req = urllib.request.Request(url)
    key = 'User-agent'
    val = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
    req.add_header(key, val)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def AnalysisURL(url):
    html = UrlOpen(url).decode('utf-8')
    addrs = re.compile(r'''v.\..+\/"''',re.VERBOSE)
    kernel_addr = addrs.findall(html)
    for num in range(len(kernel_addr)):
        KernelAddrs.append(url+kernel_addr[num][:-1])

def SaveFile(file, url):  
    AnalysisURL(url)
    filefp = open(file, 'w')
    for num in range(len(KernelAddrs)):
        html = UrlOpen(KernelAddrs[num]).decode('utf-8')
        name = re.compile(r'''linux.+gz"''',re.VERBOSE)
        filenames = name.findall(html)
        for cnt in range(len(filenames)):
            filefp.writelines(url+filenames[cnt][:-1]+'\n')

    filefp.close()


if __name__ == "__main__":
    file = "linux.txt"
    url = "https://www.kernel.org/pub/linux/kernel/"
    SaveFile(file, url)
