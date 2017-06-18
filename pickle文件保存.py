import pickle
myList = [123, 3.14, '小甲鱼', ['another list']]
pickleFile = open('my_lisk.pkl', 'wb')
pickle.dump(myList, pickleFile)
pickleFile.close()


pickleFile=open('my_lisk.pkl', 'rb')
list2=pickle.load(pickleFile)
pickleFile.close()
print(list2)
