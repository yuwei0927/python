import re
print(re.search(r'FishC', 'I love FishC.com'))

#.是通配符
print(re.search(r'.', 'I love FishC.com'))

print(re.search(r'Fish.', 'I love FishC.com'))

print(re.search(r'\.', 'I love FishC.com'))

print(re.search(r'\d', 'I love 123 FishC.com'))

print(re.search(r'\d\d\d', 'I love 123 FishC.com'))

print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.168.111.111'))
print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.168.1.1'))


print(re.search(r'[aeiou]', 'I love FishC.com'))

print(re.search(r'[aeiouAEIOU]', 'I love FishC.com'))

print(re.search(r'[a-z]', 'I love FishC.com'))

print(re.search(r'[0-9]', 'I love 123 FishC.com'))

print(re.search(r'[2-9]', 'I love 123 FishC.com'))

#正则表达式里的{}表示重复次数
print(re.search(r'ab{3}c', 'dsfabbbc'))
print(re.search(r'ab{3,10}c', 'dsfabbbbbbc')) #表示b的重复次数是从3到10都可以


print(re.search(r'Fish(C|D)', 'I love FishC.com'))

print('------------------------------------------')
#用^修饰的字符串，必须在字符串的开头位置，否则找无法找到
print(re.search(r'^FishC', 'I love FishC.com')) #无法找到
print(re.search(r'^FishC', 'FishC.com I love')) #可以找到

print('------------------------------------------')
#用$修饰的字符串，必须在字符串的结束位置，否则找无法找到
print(re.search(r'FishC$', 'I love FishC.com')) #无法找到
print(re.search(r'FishC$', 'I love FishC')) #可以找到

print('------------------------------------------')
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '192.168.1.1'))

print(re.search(r'(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])', '192.168.111.111'))

print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '192.168.1.1'))

print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '216.24.1.1'))



