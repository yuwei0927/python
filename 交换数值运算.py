x=1
y=2
print('x=%d'%x)
print('y=%d'%y)
x,y = y,x
print('x=%d'%x)
print('y=%d'%y)

#返回三个数字中的最小值，使用三元操作符
#small = x if (x < y and x < z) else (y if y < z else z)