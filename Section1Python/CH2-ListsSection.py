



l=[1,2,3,4]


print(l[0])
print(l[1])
print(l[2])
print(l[3])


print(l[-2])
print(l[len(l)-1])





print( dir(l))

print(type(l))



l.append(5)

print(l)


l1=l.copy()

l.pop()

print(l)
print(l1)

l1 = l

l.pop()

print(l)
print(l1)


l.pop(0)

print(l)
 
l = [0,1,2,3,4,5]


print(l.pop(2))

print(l)



l = list(range(10))

print(l)

print(list(range(10,30,5)))


l.append('string')

l.append({1:'1','2':1})

l.append([1,2,3])


print(l)


print(l.index(7))

print(l.index('string'))



print(l[2:-3:2])

print(l[::3])

print(l[::-2])



print(l.count(1))

l.append(1)

print(l.count(1))


print(dir(l))

#print(help(l.insert))



l.insert(0,1)

print(l)


l = list(range(10))

l.reverse()

print(l)

l.sort()

print(l)

#print(help(l.remove))



l.append(1)

print(l)


l.remove(1)

print(l)



print( 1 in l )

l.remove(1)

print( 1 in l )



print( [  i for i in range(10) if i%2==0])


