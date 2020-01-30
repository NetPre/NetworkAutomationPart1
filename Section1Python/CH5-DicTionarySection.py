




d = {'a':1 , 'b':2 , 11:1,1.2:1,(1,2,3):1,1:[1,2,3,4],}


print(d)


print(d['a'])

print(d[1])

print(d[(1,2,3)])


t = (1,2,3,4)

d[t]='new'

print(d)




for i in d:
    print(i)
    print(d[i])



print(d.pop('a'))

print( dir(d))

print(d.get(123))

d.clear()
print(d)


del d





d = {'1':10,'11':2,'3':3,'4':4}

print(d.items())

print(d.keys())

print(d.values())


print(sorted(d.keys()))
print(sorted(d.keys(), key = lambda k: int(k)))

print(sorted(d.values()))
print(sorted(d.items(),key=lambda k: int(k[0])))
print(sorted(d.items(),key=lambda k: k[1]))

