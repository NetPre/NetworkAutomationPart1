from netmiko import ConnectHandler



device = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.60',
    'username': 'cisco',
    'password': 'cisco',
    'secret':'cisco'
    }

net_connect = ConnectHandler(**device)

print(dir(net_connect))

showIPInterBri = net_connect.send_command('show ip inte bri')
print(showIPInterBri)
showIPInterBri = net_connect.send_command('show ip inte bri',delay_factor=1)
print(showIPInterBri)

print(net_connect.send_command_timing('show run',delay_factor=1))
print(net_connect.find_prompt())



print(net_connect.send_config_set(['interface loop 222','ip address 22.22.22.22 255.255.255.255','descri test loopback','no shut']))
print(net_connect.send_config_set(['interface loop 222','no ip address 22.22.22.22 255.255.255.255','hostname R6','no interface loop 222']))

print(net_connect.save_config())


