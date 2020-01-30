import telnetlib




class TelSession():
    def __init__(self, ip , user ,password,enablepass):
        self.session = telnetlib.Telnet(ip.encode('ascii'),'23')
        self.ip = ip
        self.user = user
        if user:
            self.session.read_until(b'name:')
            self.session.write(user.encode('ascii')+b'\n')
        self.session.read_until(b'Password:')
        self.session.write(password.encode('ascii')+b'\n')
        if enablepass:
            self.session.write(b'enable\n')
            self.session.read_until(b'Password:')
            self.session.write(enablepass.encode('ascii')+b'\n')
        self.session.write(b' ter len 0 \n')
        self.prompt = self.session.read_until(b' ter len 0').split()[0]
        #print(self.prompt)
        self.session.read_until(self.prompt)

    def get(self,showlist):
        output = b''
        #print(output)
        for i in showlist:
            #print(i)
            self.session.write(i.encode('ascii')+b'\n')
            # you send a word and you can read till that word 
            #self.session.write(b'!ok\n')
            #output += self.session.read_until(b'!ok')
            
            #or read the device prompt  
            output += self.session.read_until(self.prompt)
        return output.decode('ascii')


    def config(self,configList):
        output = b''
#        output = self.session.read_until(self.prompt)
#        print(output)
        self.session.write(b'conf t\n')
        for i in configList:
            #print(i)
            self.session.write(i.encode('ascii')+b'\n')
            # you send a word and you can read till that word 
            #self.session.write(b'!ok\n')
            #output += self.session.read_until(b'!ok')
            
            #or read the device prompt  
            output += self.session.expect([b'config\S*#'])[2]
            #print(output)
        self.session.write(b'end\n')
        output += self.session.read_until(b'end')
        self.prompt = self.session.read_until(b'#')
        return output.decode('ascii')

    def __del__(self):
        print(' {} eneded session TO {} '.format(self.user,self.ip))
        self.session.close()



t = TelSession('192.168.122.60','cisco','cisco',None)

print(t.get(['show ip inte bri','show interface loop 222','show version']))

print(t.config(['hostname Router6']))
print(t.config(['no interface loop 222']))


print(t.get(['show ip inte bri','show interface loop 222','show version']))


del t

