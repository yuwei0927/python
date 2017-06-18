def func(x, y):
    x = 2
    y[0] = 'hello'


x = 1
y = [1,2]
print(x)
print(y)
func(x, y)
print(x)
print(y)
#从结果上可以看到X的值没有改变，但是Y的值却发生了改变。这个是与变量的作用域有关的
