x=1
y=2
z=3

print(x < y and z)
#3

print(y or z)
#2

print(x > y or z)
#3

#expr1 and expr2
#从上面的例子中可以看到，如果expr1是真，则总的表达式返回expr2的值，
#如果expr1为假，那么总的表达式返回expr1的值。也就是说，如果当expr1
#的值为假的时候，expr2是不会被执行到的。

#expr1 or expr2
#如果expr1是真，则总的表达式返回expr1的值，如果expr1为假，那么总的
#表达式返回expr2的值。也就是说，如果当expr1的值为真的时候，expr2是
#不会被执行到的。

#cond and expr1 or expr2
#----------------------------------
# cond  expr1     expr2    最终结果
#  真    真        任何      expr1
#  假    任何       真       expr2
#  假    任何       假       expr2
#  真    假         假       expr2
#  真    假         真       expr2
#----------------------------------
