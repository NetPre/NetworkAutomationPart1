from netmiko import ConnectHandler



def getShowArp(ip):
    showArp = ''
    try:
        net_connect = ConnectHandler( 
        device_type = 'cisco_ios',
        host= ip,
        username= 'cisco',
        password='cisco',
        secret='cisco')
        showArp=net_connect.send_command('show ip arp')
        net_connect.disconnect()
    except Exception as err:
        print(err)

    print (showArp)



routersList= ['192.168.122.10','192.168.122.20','192.168.122.60','192.168.122.50']

from datetime import datetime
import threading
import multiprocessing

t = datetime.now()
for i in routersList:
    getShowArp(i)
print(datetime.now()-t)
t = datetime.now()

threads = []

for i in routersList:
    thread = threading.Thread(target=getShowArp,args=(i,))
    thread.start()
    threads.append(thread)

for i in threads:
    i.join()

print(datetime.now()-t)
t = datetime.now()

ProcessZ = []
for i in routersList:
    Process = multiprocessing.Process(target=getShowArp,args=(i,))
    Process.start()
    ProcessZ.append(Process)

for i in ProcessZ:
    i.join()



print(datetime.now()-t)
