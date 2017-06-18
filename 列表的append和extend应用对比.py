li1=[1,2,3,4,5]
li2=[2,3,4,5,6]
li3=[3,4,5,6,7]
li4=[4,5,6,7,8]
for x in li1:
    li4.append(x)
li2.append(li1)
li3.extend(li1)
print(li2)
print(li3)
print(li4)
