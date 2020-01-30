import paramiko
import re
import time


def getoutput(out,prompt):
    remote_conn.send(out+"\n")
    time.sleep(0.1)
    newout = remote_conn.recv(1000).decode('ascii')
    out = newout
    while not re.search(prompt+r'\S*#$', newout):
        newout = remote_conn.recv(1000).decode('ascii')
        out += newout
    return(out)

ip = '192.168.122.60'
USERNAME = "cisco"
PASSWORD = "cisco"
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
remote_conn.send(" ter len 0 \n")
output = remote_conn.recv(1000).decode('ascii')
print (output)

prompt  = re.findall(r'\S+',output)[0][:-1]
print(prompt)


print(getoutput('show run ',prompt))
print(getoutput('show ip inte bri ',prompt))
print(getoutput('show version ',prompt))
print(getoutput('show process cpu ',prompt))
print(getoutput('show process memory ',prompt))

remote_conn.close()