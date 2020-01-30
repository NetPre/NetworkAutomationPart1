


import os 




def pingFunc(IP):
        response = os.system('ping -c 1  '+str(IP)+' >/dev/null 2>&1')
        if(response==0):
            #print('IP is Up ', IP)
            return True
        else:
            #print('IP is down ', IP)        
            return False

ipList = ['4.2.2.2','4.2.2.3','4.2.2.6']
for IP in ipList:
    if (pingFunc(IP)):
            print('IP is Up ', IP)
    else:
            print('IP is down ', IP)        



import time

print(pingFunc('4.2.2.2'))

IP = '4.2.2.2'
while True:
    if (pingFunc(IP)):
            print('IP is Up ', IP)
            break
    else:
            print('IP is down ', IP)    
            time.sleep(2)    
