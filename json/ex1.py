import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<25}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for entry in data['imdata']:
    dn = entry['fabricEthEstc']['attributes']['dn']
    description = entry['fabricEthEstc']['attributes'].get('descr', '')
    speed = entry['fabricEthEstc']['attributes'].get('speed', 'inherit')
    mtu = entry['fabricEthEstc']['attributes'].get('mtu', '')

    print("{:<50}{:<25}{:<8}{:<6}".format(dn, description, speed, mtu))
