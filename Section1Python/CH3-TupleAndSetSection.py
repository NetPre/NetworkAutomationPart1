


t = (1,2,3,4,3)


print(t)

print(type(t))


print(dir(t))


print(t.index(3))


print(len(t)-1-t[::-1].index(3))


print(t.count(3))



for i in t:
    print(i)

l = []
for i in t:
    l.append(i)


l.append(1)

print(l)


t = tuple(l)

print(t)





print('#################### SET ######################')

list1 = [1,2,3,4]
list2 = [3,4,5,6]

print(set(list1)^set(list2))
#{1, 2, 5, 6}
print(set(list1)-set(list2))
#{1, 2}
print(set(list2)-set(list1))
#{5, 6}
print(set(list2) & set(list1))
#{3, 4}
print(set(list1+list2))
#{1, 2, 3, 4, 5, 6}




