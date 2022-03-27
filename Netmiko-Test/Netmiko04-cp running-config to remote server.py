

# condition: connection failure to some devices
# in this case, sw3 change mgmt ip, sw4 shutdown its mgmt


from netmiko import ConnectHandler

hosts = ['192.168.51.31', '192.168.51.32', '192.168.51.33', '192.168.51.34', '192.168.51.35']


def devices_info(host):
    swtich = {
        "device_type": "cisco_nxos",
        "username": "admin",
        "password": "cisco!123",
    }
    swtich["ip"] = host
    return swtich


if __name__ == '__main__':
    for host in hosts:
        swtich = devices_info(host)

        # print(swtich)
        try:
            ssh_connect = ConnectHandler(**swtich)
        except:
            print(f'{swtich["ip"]} Unreachable')

        else:
            result = ssh_connect.send_command("copy running-config ftp://python:cisco!123@192.168.51.20/home/python/ vrf management","\n")
            print(result)

