print('\n#############################   Now Strings ########################################\n')


# so this is how you specify a variable 
# a varible can be a string a integer a float 
x = 'hello '

print(dir(x))

print(type(x))
print(len(x))




x = 'hello how are you my name is carl how is your day going'

# the find function we will find the index were the string is located 
print(x.find('you'))
print(x[x.find('you'):])

# reverse find 
print(x.rfind('you'))
print(x[x.rfind('you'):])

# change the string carater all to lower case 
print('Carl'.lower())

# change all the string carater to upper case 
print('Carl'.upper())

# the replace function will replace all the string with the second string
x = x.replace('you','me')
print(x)


print(x)
# we print the first element 
print(x[0])
# print the 4th element 
print(x[4])
# print the last element 
print(x[-1])
# this the same as the previous 
print(x[len(x)-1])
# this is the second last element 
print(x[-2])


# checking if all characters are upper case or lower case 
print('C'.isupper())
print('Cc'.isupper())
print('cC'.isupper())
print('CC C'.isupper())

print('cC'.islower())
print('c'.islower())


print("############################ check if all the element are digits ")
print('1'.isdigit())
print('12'.isdigit())
print('1A'.isdigit())

print('1'.isnumeric())
print('1A'.isnumeric())


print("######### the diffrence between the isdigit and is numeric")
print('½'.isdigit())
print('½'.isnumeric())

print('0.5'.isdigit())
print('0.5'.isnumeric())


print("######### swapcase will convert upper case to lower case and the vise versa ")
print('Carl'.swapcase())
print(','.join(['a','b','c']))



# strip space from left and right 
print('    hello man    '.strip())
# left strip
print('    hello man    '.lstrip())
# right strip 
print('    hello man    '.rstrip())


x = ''' helklasd cartl how are you how is your day
i am training to be a network automation enginer
i don't have a social life '''

# split string per space into a list
print(x.split())
# split strings per lines into a list 
print(x.splitlines())


# split string with the deliminater is '\n'
print(x.split('\n'))
# split string with the deliminater is 'n'
print(x.split('n'))



# check if the string start with is and then we test with carl 
print('carl is her'.startswith('is'))
print('carl is her'.startswith('carl'))

# check if the string end with her
print('carl is her'.endswith('her'))


