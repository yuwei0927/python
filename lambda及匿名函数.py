def ds(x):
    return 2*x+1


def sum1(x,y):
    return x+y

g =lambda x:2*x+1
s =lambda x,y: x+y

print(ds(5))
print(g(5))
print(sum1(5,6))
print(s(5,6))

#filter过滤器
print(list(filter(None, [1, 0, False, True]))) #过滤掉所有非真


def odd(x):
    return x%2

temp=range(10)
show= filter(odd,temp)
print(list(show))


print(list(filter(lambda x : x%2, temp)))

#map映射
print(list(map(lambda x : x*2, temp)))

t= lambda x : x*2
#print(g(temp)) #这句会出错，传入的类型不正确
