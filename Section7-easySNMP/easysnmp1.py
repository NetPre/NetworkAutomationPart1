
from easysnmp import Session,snmp_get,snmp_walk





ss = Session(hostname='192.168.122.60',community='snmpPassword',version=2)


ifOperStatus = ss.walk('1.3.6.1.2.1.2.2.1.8')
#print(ifOperStatus)

ifdes = ss.walk('1.3.6.1.2.1.2.2.1.2.')


for key , Item in enumerate(ifOperStatus):
#    print(i)
#    print(i.value)
    if(Item.value)=='1':
        print('interface {} is up'.format(ifdes[key].value))
    elif(Item.value)=='2':
        print('interface {} is down'.format(ifdes[key].value))



getInterfaceEther2staus = ss.get('1.3.6.1.2.1.2.2.1.8.2') 

print(getInterfaceEther2staus.oid)
print(getInterfaceEther2staus.oid_index)
print(getInterfaceEther2staus.snmp_type)
print(getInterfaceEther2staus.value)




