from easysnmp import Session,snmp_get,snmp_walk


ss = snmp_get( '1.3.6.1.2.1.2.2.1.2.1', hostname='192.168.122.60',community='snmpPassword',version=2)

print(ss)



ss = snmp_get( '1.3.6.1.2.1.1.5.0', hostname='192.168.122.60',community='snmpPassword',version=2)
print(ss)



ss = snmp_walk('1.3.6.1.2.1.2.2.1.8', hostname='192.168.122.60',community='snmpPassword',version=2)


for i in ss:
    print(i)
