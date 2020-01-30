from napalm import get_network_driver
import json
import re
driver = get_network_driver('ios')



iosRouter = driver('192.168.122.60','cisco','cisco')
iosRouter.open()

print(iosRouter.get_facts())

#device.load_merge_candidate(filename=config_file)

iosRouter.load_merge_candidate(config ='hostname RouterIs6')

print(iosRouter.compare_config())


yes = input("\nWould you like to commit these changes?")

if yes =='yes':
    print(iosRouter.commit_config())
else:
    print(iosRouter.discard_config())


iosRouter.close()