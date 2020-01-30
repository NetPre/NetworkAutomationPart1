


with open('/home/carl/Desktop/MyCourseLive/TEXT/showProcessMemory.txt') as reader:
    lines = reader.readlines()

print(lines)

print('--------------------------------------------------------')

head = lines.pop(0).split()
print(head)

print('--------------------------------------------------------')

data = [ line.split() for line in lines]

print(data)

print('--------------------------------------------------------')


print(dict(zip(head,data[0])))
print(dict(zip(head,data[1])))

print('--------------------------------------------------------')



diclist = [ dict(zip(head,i)) for i in data]
print(diclist)

print('--------------------------------------------------------')



for i in sorted(diclist,key= lambda k : int(k['PID'])):
    print(i)

print('--------------------------------------------------------')


a = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 2, a)))

print(list(map(lambda x: x % 2 == 0, a)))
#[False, True, False, True, False, True]


print(list(filter(lambda x : x % 2 == 0, a)))
#[2, 4, 6]


