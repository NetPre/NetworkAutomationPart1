from netmiko import ConnectHandler

'''
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.60',
    'username': 'cisco',
    'password': 'cisco',
    'secret':'cisco'
    }


net_connect = ConnectHandler(**device)
'''

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

    return showArp



routersList= ['192.168.122.10','192.168.122.20','192.168.122.60','192.168.122.50','1.1.1.123']

for i in routersList:
    print(getShowArp(i))
