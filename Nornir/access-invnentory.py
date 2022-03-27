from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")

print(nr.inventory)
print(nr.inventory.hosts)
print(nr.inventory.groups)

print(nr.inventory.hosts['sw1'])
print(nr.inventory.hosts['sw1'].keys())