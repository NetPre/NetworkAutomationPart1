from napalm import get_network_driver
import json
import re
driver = get_network_driver('ios')



iosRouter = driver('192.168.122.60','cisco','cisco')
iosRouter.open()

print('#####################################'*5)
#showIpRoute = iosRouter.get_route_to(destination='6.6.6.6')
#print(json.dumps(showIpRoute,indent = 2))
#showIpRoute = iosRouter.get_route_to(destination='5.5.5.5')
#print(json.dumps(showIpRoute,indent = 2))
#showIpRoute = iosRouter.get_route_to(destination='3.3.3.3')
#print(json.dumps(showIpRoute,indent = 2))
print('#####################################'*5)

#subnets = iosRouter.cli(['show ip route'])
#subnets = re.findall(r'\n[a-zA-Z] \S*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',subnets['show ip route'])
print('#####################################'*5)

#for subnet in subnets:
#    showIpRoute = iosRouter.get_route_to(destination=subnet)
#    print(json.dumps(showIpRoute,indent = 2))


print('############### get_interfaces_counters ######################'*5)
intOutput = iosRouter.get_interfaces_counters()
print(json.dumps(intOutput,indent = 2))
print(intOutput['Ethernet1/2']['tx_broadcast_packets'])
print('################## get_arp_table ###################'*5)
showArp = iosRouter.get_arp_table()
print(json.dumps(showArp,indent = 2))
print('#################### ping #################'*5)
print(json.dumps(iosRouter.ping('4.4.4.4'),indent = 2))
print('################### traceroute ##################'*5)
print(json.dumps(iosRouter.traceroute('3.3.3.3'),indent = 2))
print('####################### get_interfaces ##############'*5)
print(json.dumps(iosRouter.get_interfaces(),indent = 2))
print('####################### getconfig ##############'*5)
print(json.dumps(iosRouter.get_config(),indent = 2))
print('#####################################'*5)

iosRouter.close()