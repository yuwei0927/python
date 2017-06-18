li1=[1,2,3,4,5,6,7]
li2=li1
li3=li1[:]
print(li1)
print(li2)
print(li3)

print(id(li1))
print(id(li2))
print(id(li3))

li1[3]=35

print(li1)
print(li2)
print(li3)


s1='hello'
s2=s1
s1='go'
print(s1)
print(s2)


st1="abcd"
st2="abcd"
print(id(st1))
print(id(st2))

list1=[1,2,3,4]
list2=[1,2,3,4]
print(id(list1))
print(id(list2))
#列表与字符串是有区别的。 即使列表变量的值相同， 他们也是指向不同的列表值
