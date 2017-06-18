import urllib.request
import urllib.parse
import json


content=input("请输入需要翻译的内容：")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'

#第一种方法，在申请Request的时候，将Head传入
'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
'''

data = {}
data['type']='AUTO'
data['i']=content
data['doctype']='json'
data['xmlVersion']='1.8'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'

data = urllib.parse.urlencode(data).encode('utf-8')

#req = urllib.request.Request(url, data, head)
req = urllib.request.Request(url, data)

#第二种方法，先申请Request，然后再通过Add方法将Head添加进去。
key = 'User-Agent'
val = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
req.add_header(key, val)

response = urllib.request.urlopen(req)

html  = response.read().decode('utf-8')

#print(html)


target = json.loads(html)
target = target['translateResult'][0][0]['tgt']
print("翻译结果：%s" % (target))
