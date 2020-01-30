print('\n#############################   Class ########################################\n')


# we going to start by creating a basic class 
class Router1:
        pass

# Here we are assigning r to the class Router1 
r = Router1

# we can add values to the valriable r 
r.value = 5 
print(r.value)

# the advantage of being able to create a class is that you can specify your own varible for the class 
# you can create your own functions 
class Router:
        # you can see here we have define the varible type as string named router
        type = 'router'
        # and we have create a function called action that will return the string something
        def action(self):
                return 'something'
        # when you are in a class you can specify the atribute self meaning 
        # you can call  yourself and all varible and function in the class
        def action2(self):
                return 'this is a ' + self.type

r = Router()
print(r.action())
print(r.action2())
print(r.type)
print(type(r))



# okay let start the fun now 
# we are going to import a couple of libraries 
import time
from datetime import datetime
import os 

class Device():
        def __init__(self,Name:str,Ip:str,Type:str):
                self.ip = Ip                                    # device IP address
                self.name = Name                                # device name
                self.type = Type                                # device type
                self.lastCheck = datetime.now()                 # last time information got update
                self.deviceReachableOnInit = self.pingFunc() # is the device reachable

        def pingFunc(self):
                '''
                check if the device is reachble 
                we will use os library to execute a ping -c 1 meaning number of ping = 1
                ' >/dev/null 2>&1' so that the output of the ping won't be printed 
                '''
                response = os.system('ping -c 1  '+self.ip+' >/dev/null 2>&1')
                if(response==0):
                        self.lastCheck = datetime.now()
                        return True
                else:   
                        self.lastCheck = datetime.now()
                        return False


        def pingDeviceTillUpFunc(self):
                '''
                this is a useless function for now that wait till the device is up 
                with an infite loop 
                '''
                response = os.system('ping -c 1  '+self.ip+' >/dev/null 2>&1')
                while True:
                        if(response==0):
                                return True
                        else:
                                time.sleep(30)

        def __str__(self):
                '''
                is a built-in function in python, used for string representation of the object.
                '''
                return self.ip +' '+self.name+' '+str(self.pingFunc())


D = Device('MS','4.2.2.2','DNS')

print(D.pingFunc())
print(str(D))




print('#################### Inheritance ############################')

# how we can inhert from a diffrent class 
# so we don't have re-write all the infromation 

class Switch(Device):
    def __init__(self,Name:str,Ip:str,Type:str,stpType:str):
        Device.__init__(self,Name,Ip,Type)
        self.stpType = stpType
    def something(self,value):
        # in this function we are giving it variable 
        return 'something' + value


sw = Switch('Test','4.2.2.2','9400','stpType')

# now we will print the function and the variables 

print(sw.name)
print(sw.type)
print(sw.ip)
print(sw.stpType)
print(sw.deviceReachableOnInit)
print(sw.lastCheck)
print(sw.pingFunc())
print(sw.something(' hello'))




print('######## Special Methods ############## __len__ __del__ __str__ #########################')

# built-in function in python, example used for string representation of the object.


class Switch2(Device):
    def __init__(self,Name:str,Ip:str,Type:str,stpType:str,uptime:int):
        Device.__init__(self,Name,Ip,Type)
        self.stpType = stpType
        self.uptime = uptime

    def __str__(self):
        return "SwName:%s , SwitchIp:%s  " %(self.name, self.ip)

    def __len__(self):
        return self.uptime

    def __del__(self):
        print ("Switch deleted")


sw = Switch2('Test','4.2.2.2','9400','stpType',10)


print (sw)
print (len(sw))
del sw





print('#################### super() example 1  ############################')

# the super function is a built-in function that returns the proxy object that allows you to refer parent class by ‘super.’  
# The super function in Python can be used to gain access to inherited methods, which is either from the parent or sibling class.

# we are going to use the supper function inplace of defining the parent class 

class Router2(Device):
    def __init__(self,Name:str,Ip:str,Type:str,routingtable:str,uptime:int):
        super().__init__(Name,Ip,Type)
        self.routingtable = routingtable
        self.uptime = uptime

    def __str__(self):
        return "SwName:%s , SwitchIp:%s  " %(self.name, self.ip)

    def __len__(self):
        return self.uptime

    def __del__(self):
        print ("Switch deleted")

rt = Router2('Test','4.2.2.2','9400','ip route 0.00.0.0 0.0.0..0 1.2.3.4',10)

print(len(rt))
print(rt)
print(rt.name)
print(rt.type)
print(rt.ip)
print(rt.routingtable)
print(rt.deviceReachableOnInit)
print(rt.lastCheck)
print(rt.pingFunc())



print('#################### Python super() function with multilevel inheritance ######################')

# now let have fun with multilevel inheritance 

class DeviceM(object):
        def __init__(self,Name:str,Ip:str,Type:str):
                self.ip = Ip
                self.name = Name 
                self.type = Type
                self.lastCheck = datetime.now()
                self.deviceReachableOnInit = self.pingFunc()
                print ("parent")


        def pingFunc(self):
                response = os.system('ping -c 1  '+self.ip+' >/dev/null 2>&1')
                if(response==0):
                        self.lastCheck = datetime.now()
                        return True
                else:   
                        self.lastCheck = datetime.now()
                        return False



class SwitchM(DeviceM):
    def __init__(self,stpType,**kw):
        self.stpType = stpType
        super().__init__(**kw)

class RouterM(DeviceM):
    def __init__(self,routingTable,**kw):
        self.routingTable = 'routingTable'
        super().__init__(**kw)
        
class layer3Switch(SwitchM, RouterM):
    def __init__(self,Name,Ip,Type,stpType,routingTable,numOfSVI):
        self.numberOfSVI = numOfSVI
        super().__init__(Name=Name,Ip=Ip,Type=Type,stpType=stpType,routingTable=routingTable)
        print ("child")


R = RouterM('123123123123',Name='Name',Ip='4.2.2.4',Type='Type')
print(R.lastCheck)


l3 = layer3Switch('Name','4.2.2.2','Type','stpType','routingTable',5)
print(l3.deviceReachableOnInit)
print(l3.lastCheck)
print(l3.stpType)

print(l3.pingFunc())
print(l3.numberOfSVI)












print('end example to show that everything is an object in python  ')




class mylist(list):
        def __init__(self):
                list.__init__(self)
        

        def __str__(self):
                return 'wohoooooo'



l = mylist()


for i in range(1,50):
        l.append(i)

print(l)

for i in l :
        print(l.pop(),end = ' ')
















