s1='abc'
s2='vdf'

print(max(s1))
print(min(s2))

t1=[1,345,456,456,574,3,5]
t2=(3,54,565,467,873,45,567)

print(max(t1))
print(min(t2))

s3='fdjghskboisndfog'

for i, t in enumerate(s3):
    print(i,t)

print(list(zip(s1,s2)))
#print(zip(s1,s2))

#max及min必须的保证序列的各元素是相同的类型,如下：
num=[1,2,3,4,5,6,'a']
#print(max(num))#这句话会出错
#
#max的内部实现原理如下：
#def max(li):
#    max=li[0]
#    for each in li:
#        if each > max:
#            max = each
#    return max

num1=[1,2,3,4,5,6]
print(sum(num1))
print(sum(num1,-21))
#print(sum(num))#这句话会出错,sum里不同的类型必须是数字(整形，浮点都可以)
t2=['s','d','gh']
t3='dfshfhj'
print(sorted(t2))
print(sorted(t3))
#sorted必须的保证序列的各元素是相同的类型

print(list(reversed(t3)))
#print(reversed(t3))

print(list(enumerate(t3)))
