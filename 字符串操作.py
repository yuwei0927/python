s="version"
num =1.0
f="%s" %s
f1="%s %d" % (s, num)
print(f)

print(f1)


word="version1.0"

print(word.center(30))

print(word.center(30, "*"))

print(word.ljust(4))

print(word.ljust(20))

print(word.rjust(20))


s="\thello\tworld"
print(s)

#去掉字符串首尾的转意符
print(s.strip())

#
print(s.lstrip())

print(s.rstrip())


str=["hello","world","hello","china"]
r="".join(str)
print(r)
r1=",".join(str)
print(r1)

s="hello,world"
s1="hello,world*abc"
print(s.split(","))
print(s1.split("*"))


#判断字符串以什么字符开始和结尾
print("ace".startswith("a"))
print("ace".startswith("b"))
print("ace".endswith("a"))
print("ace".endswith("e"))

def reverse_str(s):
    out=""
    li=list(s)
    for i in range(len(li),0,-1):
        out += "".join(li[i-1])
    return out
print(reverse_str("abcdef"))

s2="abacad"
print(s2.find("a"))
print(s2.rfind("a"))  #从右边开始查找

import datetime
t=datetime.datetime.now()
print(t)
#print(t.strftime("%Y-%m-%d %H:%M:%s"))

