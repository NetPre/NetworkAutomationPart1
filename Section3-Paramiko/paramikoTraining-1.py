import paramiko
import time
import re

ip = '192.168.122.60'
username = 'cisco'
password = 'cisco'


remote_conn = paramiko.SSHClient()



remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())


remote_conn.connect(ip, username=username , password=password , look_for_keys= False , allow_agent=False)

sshRemote = remote_conn.invoke_shell()
sshRemote.send('ter len 0 \n')
output = sshRemote.recv(1300).decode('ascii')

routersName = output.split()[0][:-1]
print(routersName)

promptRegex = routersName+r'\S*#$'
print(promptRegex)

sshRemote.send('conf t \n')

sshRemote.send('do show run \n')
sshRemote.send('end \n')
time.sleep(0.2)
output = sshRemote.recv(1300).decode('ascii')
print(output)
while not re.search(promptRegex,output):
    output = sshRemote.recv(1300).decode('ascii')
    print(output)



def getOutput(command,promptRegex,sshRemote):
    sshRemote.send( command+' \n')
    time.sleep(0.2)
    output = sshRemote.recv(1300).decode('ascii')
    #print(output)
    finalOut = output
    while not re.search(promptRegex,output):
        output = sshRemote.recv(1300).decode('ascii')
        #print(output)
        finalOut += output
    return finalOut




print(getOutput('show ip inte bri',promptRegex,sshRemote))

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'*10)
show_list = ['show ip route','show version','show interface status','show run ','show process cpu ']
for i in show_list:
    print(getOutput(i,promptRegex,sshRemote))


sshRemote.close()


