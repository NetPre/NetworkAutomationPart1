from netmiko import ConnectHandler
import re
import json



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

    showArp = re.findall(r'Internet  (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})  ARPA   (\S+)',showArp)
    arpList = []
    for i in showArp:
        arpList.append({'neighborIp':i[0],'neighborMac':i[1],'Interface':i[2]})

    return arpList





#print(getShowArp('192.168.122.60'))




def getShowIpRoute(ip):
    showIpRoute = ''
    try:
        net_connect = ConnectHandler( 
        device_type = 'cisco_ios',
        host= ip,
        username= 'cisco',
        password='cisco',
        secret='cisco')
        showIpRoute=net_connect.send_command('show ip route')
        net_connect.disconnect()
    except Exception as err:
        print(err)

    showIpRoute = re.findall(r'\n[a-zA-Z] \S*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.+(?:\n\s+\[.+){0,})',showIpRoute)
    dicShowIpRoute = {}
    for i in showIpRoute:
        dicShowIpRoute[i[0]]=[]
        for nextHop in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}), (\S+)|.+(connected), (\S+)|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',i[1]):
            if(nextHop[0]):
                dicShowIpRoute[i[0]].append({'nexthopIp':nextHop[0],'nexthopInt':nextHop[1]})
            elif(nextHop[2]):
                dicShowIpRoute[i[0]].append({'nexthopIp':'connected','nexthopInt':nextHop[3]})
            elif(nextHop[4]):
                dicShowIpRoute[i[0]].append({'nexthopIp':nextHop[4],'nexthopInt':''})

    return dicShowIpRoute





#output = getShowIpRoute('192.168.122.60')
#print(json.dumps(output,indent=3))


def getShowIpRoute2(ip):
    showIpRoute = ''
    try:
        net_connect = ConnectHandler( 
        device_type = 'cisco_ios',
        host= ip,
        username= 'cisco',
        password='cisco',
        secret='cisco')
        showIpRoute=net_connect.send_command('show ip route')
        net_connect.disconnect()
    except Exception as err:
        print(err)

    dicShowIpRoute = {}
    start = False
    for line in showIpRoute.splitlines():
        if start and line:
            splitLine = line.split()
            if splitLine[0].isalpha():
                if splitLine[1][0].isdecimal():
                    subnet = splitLine[1]
                    dicShowIpRoute[subnet]=[] 
                    if splitLine[-2]=='connected,':
                        nextHopIp = splitLine[-2]
                        nextHopInt = splitLine[-1]
                    elif(splitLine[-1][0].isdecimal()):
                        nextHopIp = splitLine[-1]
                        nextHopInt = 'No Int'
                    dicShowIpRoute[subnet].append({'nexthopIp':nextHopIp,'nexthopInt':nextHopInt})
                else:
                    subnet = splitLine[2]
                    dicShowIpRoute[subnet]=[] 
                    nextHopIp = splitLine[5]
                    nextHopInt = splitLine[6]
                    dicShowIpRoute[subnet].append({'nexthopIp':nextHopIp,'nexthopInt':nextHopInt})
            else:
                if(splitLine[0][0]=='['):
                    if(splitLine[-1][0].isdecimal()):
                        nextHopIp = splitLine[-1]
                        nextHopInt = 'No Int'
                    else:
                        nextHopIp = splitLine[-2]
                        nextHopInt = splitLine[-1]        
                    dicShowIpRoute[subnet].append({'nexthopIp':nextHopIp,'nexthopInt':nextHopInt})



        if 'Gateway of last resort is not set' in line :
            start = True
    return dicShowIpRoute



dicShowIpRoute = getShowIpRoute2('192.168.122.60')
print(json.dumps(dicShowIpRoute,indent=3))
