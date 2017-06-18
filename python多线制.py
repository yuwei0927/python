import threading

def test(i):
    print(i)


ts=[]

for i in range(0,10):
    th = threading.Thread(target = test, args=[i])
    ts.append(th)

for i in ts:
    i.start()


for i in ts:
    i.join()

print('end!')
