x = 5
def fun1():
    print('fun1 is running...')
    def fun2():
        print('fun2 is running...')
    fun2()

fun1()

#说明：fun2的作用域只在fun1内部！
#python中的闭包:

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder

p = make_adder(23)
q = make_adder(44)

print(p(100))
print( q(100))


print(make_adder(23)(100))
print(make_adder(44)(100))

#global
def sum1():
    global x
    return x+10

print(sum1())

#nonlocal
def fun1():
    y = 10
    def fun2():
        nonlocal y
        y *= y
        return y
    return fun2()

print(fun1())

print('x=',x)
def fun3():
    x = 10
    def fun2():
        global x
        print('x=',x)
        x *= x
        return x
    return fun2()

print(fun3())
    
