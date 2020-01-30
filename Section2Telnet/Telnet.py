import telnetlib





def telnetGetOutputs(hostname,username,password,enablePass,showList):
    tn = telnetlib.Telnet(hostname.encode('ascii') , '23')
    t = tn.read_until(b'Username:')
    print(t)
    tn.write(username.encode('ascii')+b'\n')
    t = tn.read_until(b'Password:')
    print(t)
    tn.write(password.encode('ascii')+b'\n')
    if enablePass:
        tn.read_until(b'>')
        tn.write(b'en \n')
        t = tn.read_until(b'Password:')
        tn.write(enablePass.encode('ascii')+b'\n')
    tn.write(b'ter len 0 \n')
    for i in showList:
        tn.write(i.encode('ascii')+b'\n') 
    tn.write(b'exit \n\n')
    output = tn.read_all()
    tn.close()
    return output.decode('ascii')



print(telnetGetOutputs('192.168.122.60','cisco','cisco',None,['show ip inte bri','show process memory','show run ']))


