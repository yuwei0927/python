#字典的几种创建方法
#字典里内容的顺序会与创建时传入参数的顺序不同
dict1=dict(小甲鱼='让编程改变世界',苍井空='让AV征服所有宅男')
print(dict1)

dict2=dict((('a',56),('c', 87),('f', 83)))
print(dict2)

dict3=dict((['a',56],['c', 87],['f', 83]))
print(dict3)


s1='sdjhf'
s2='dfhjk'
dict4=dict(zip(s1,s2))
print(dict4)


s3='dfsdfk'
dict5=dict(enumerate(s3))
print(dict5)

print(dict5.fromkeys((1,2,3),'number'))
print(dict5)

dict6={}
print(dict6)
dict7=dict6.fromkeys((1,2,3),'number')
print(dict7)
print(dict6)

dict8=dict6.fromkeys(range(10),'good')
print(dict8)

#获取字典中不存在key的值
print(dict4['s'])
#print(dict4['c']) #字典里没有key为c的值，所有会出错，但是可以用下面的方法来代替
print(dict4.get('s'))
print(dict4.get('c'))#当key中没有时，返回一个None
print(dict4.get('c','Key值不存在'))#当key中没有时，返回后面的字符串
print(dict4.get('s','Key值不存在'))

print('c' in dict4)
print('s' in dict4)

#字典的清空方法
dict4.clear()
print(dict4)

a={1:'one', 2:'two'}
b=a
print(b)
a={}
print(a)
print(b)
print('--------------------')
a=b
a.clear()
print(a)
print(b)
#从上面的例子中可以看到，使用clear方法来清空字典更为安全，不会出现信息泄露的问题

print('--------------------')
a={1:'one', 2:'two'}
b=a
c=a.copy()
print(a,b,c)
#当前a,b,c 三个字典的内容都是一样的。
print(id(a))
print(id(b))
print(id(c))
#但是使用copy新生成的字典c的地址是不一样的
b[3]='three'
print(a,b,c)#使用copy新生成的字典c的内容里没有增加

print('--------------------')
a.setdefault('4')
print(a)
a.setdefault(6,'six')
print(a)

b={'4':'strfor'}
a.update(b)
print(a)
b={9:'nine'}
a.update(b)
print(a)

