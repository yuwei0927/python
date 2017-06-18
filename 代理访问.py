import urllib.request

url = 'http://www.whatismyip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http':'119.254.92.53:80'})

opener = urllib.request.build_opener(proxy_support)

key = 'User-agent'
val = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
    
opener.add_headers = (key, val)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)


html = response.read().decode('utf-8')

print(html)
