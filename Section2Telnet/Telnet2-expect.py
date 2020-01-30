import telnetlib

session = telnetlib.Telnet(b'192.168.122.60','23')

session.write(b'cisco\n')
session.write(b'cisco\n')
session.expect([b"Router6\S*#"])
session.write(b'ter len 0 \n')
session.expect([b"Router6\S*#"])

session.write(b'show version\n')


something  = session.expect([b"Router6\S*#"],timeout=1)

print('--------------------------------------------------------------')
print(something)
print('--------------------------------------------------------------')
print(something[0])
print('--------------------------------------------------------------')
print(something[1])
print('--------------------------------------------------------------')
print(something[1].group())
print('--------------------------------------------------------------')
print(something[2].decode('ascii'))
print('--------------------------------------------------------------')

print(session.expect([b'aaaaaaaaaaaaaa'],timeout=1))


print('------------------------------new--------------------------------')
session.write(b'\n')
print('--------------------------------------------------------------')
session.expect([b"Router6\\S*#"],timeout=1)
session.write(b'conf t\n')

something  = session.expect([b"Router6\\S*#"],timeout=1)
print(something)
