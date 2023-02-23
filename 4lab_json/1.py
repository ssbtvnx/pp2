import json

a=open('2.json')
b=json.load(a)
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in b['imdata']:
    print("{DN:50}{Speed:>30}{MTU:>7}".format(DN = i['l1PhysIf']['attributes']['dn'], Speed=i['l1PhysIf']['attributes']['speed'], MTU=i['l1PhysIf']['attributes']['mtu']))