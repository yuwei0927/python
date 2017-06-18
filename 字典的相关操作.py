d={"a":1,"b":2}

print(d.keys())
print(d.values())

for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    print(i)


d1={"a":1,"b":2}
d2={"c":3,"d":4}
d3={"a":5,"e":6}
print(d1)
d1.update(d2)
print(d1)
d1.update(d3)
print(d1)
