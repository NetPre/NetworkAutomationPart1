import paramiko
import re
import time




class DeviceSsh():
    def __init__(self,ip,user,password):
        self.ip = ip
        self.user = user
        self.password = password
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        self.remote_conn = remote_conn_pre.invoke_shell()
        self.remote_conn.send(" ter len 0 \n")
        output = self.remote_conn.recv(1000).decode('ascii')
        #print (output)
        self.Name = output.split()[0][:-1]
        self.regexPrompt = self.Name+r'\S*#$'
        #print(self.regexPrompt)


    def getoutput(self,out):
        self.remote_conn.send(out+"\n")
        time.sleep(0.1)
        newout = self.remote_conn.recv(1000).decode('ascii')
        out = newout
        while not re.search(self.regexPrompt, newout):
            newout = self.remote_conn.recv(1000).decode('ascii')
            out += newout
        return(out)

    def getoutputs(self,showList):
        finalOut = ''
        for command in showList:
            finalOut += self.getoutput(command)
        return finalOut

    def configer(self,commands):
        self.remote_conn.send("conf t\n")
        for i in commands:
            self.remote_conn.send(i+"\n")
        self.remote_conn.send("end !!! end of config \n")
        time.sleep(0.5)
        newout = self.remote_conn.recv(1400).decode('ascii')
        out = newout
        while not 'end !!! end of config ' in newout:
            newout = self.remote_conn.recv(1400).decode('ascii')
            out += newout
        
        self.Name = re.search(r'(\S+)\(\S+\)#end !!! end of config ', out).group(1)
        self.regexPrompt = self.Name+r'\S*#$'
        print(self.regexPrompt)
        return out

    def __del__(self):
        print(' connection to {} closed by {}'.format(self.ip,self.user))
        self.remote_conn.close()

ip = '192.168.122.60'
USERNAME = "cisco"
PASSWORD = "cisco"

r6 = DeviceSsh(ip,USERNAME,PASSWORD)
#print(r6.getoutput('show run '))
#print(r6.getoutputs(['show ip inte bri','sho run','show process cpu']))



print(r6.configer(['interface loop 222','ip address 22.22.22.22 255.255.255.255','descri test loopback','no shut']))
print(r6.configer(['interface loop 222','no ip address 22.22.22.22 255.255.255.255','hostname R6','no interface loop 222']))


del r6