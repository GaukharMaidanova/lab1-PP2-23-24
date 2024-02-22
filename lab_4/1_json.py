import json
with open('lab_4\sample-data.json', 'r') as file:
    data = json.load(file)
    
    target_dns = [
    "topology/pod-1/node-201/sys/phys-[eth1/33]",
    "topology/pod-1/node-201/sys/phys-[eth1/34]",
    "topology/pod-1/node-201/sys/phys-[eth1/35]"
    ]
    print("Interface Status")
    print("="*80)
    print("DN                                                 Description           Speed    MTU  ")
    print("-"*46, " ", "-"*14, "       ", "-"*6, " ", "-"*6)
    for item in data['imdata']:
        if 'l1PhysIf' in item:
            l1PhysIf_data = item['l1PhysIf']
            dn = l1PhysIf_data['attributes']['dn']
            if dn in target_dns:
                description = l1PhysIf_data['attributes']['descr']
                speed = l1PhysIf_data['attributes']['speed']
                mtu = l1PhysIf_data['attributes']['mtu']
                print(dn, " "*8, description, " "*18, speed, "  ", mtu)
    