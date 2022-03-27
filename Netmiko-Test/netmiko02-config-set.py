from netmiko import ConnectHandler

hosts=['192.168.51.31','192.168.51.32','192.168.51.33','192.168.51.34','192.168.51.35']

def devices_info(host):
    swtich={
    "device_type":"cisco_nxos",
    "username":"admin",
    "password":"cisco!123",
    }
    swtich["ip"]=host
    return swtich


for host in hosts:
    swtich = devices_info(host)

    #print(swtich)

    ssh_connect = ConnectHandler(**swtich)

    result=ssh_connect.send_config_set("vlan 10-20")
    print(result)
