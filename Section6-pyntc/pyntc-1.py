
# https://github.com/networktocode/pyntc
# this is amazing
import json
from pyntc import ntc_device as NTC


router6 = NTC(host='192.168.122.60',username='cisco',password='cisco',device_type='cisco_ios_ssh')

router6.open()

print(json.dumps(router6.facts,indent=2))



print(router6.show('show ip arp'))

print(router6.show_list(['show ip inte bri','sho clock','show ip arp']))


print(router6.running_config)







router6.config('hostname test-Router6')
router6.config_list(['interface loop 111','ip address 111.11.11.11 255.255.255.255','description test loopback','no shut'])

print(router6.show('show run | in hostname'))
print(router6.show('show run interface loop 111'))
router6.save()


router6.backup_running_config('Router6.cfg')

router6.close()

