
from netmiko import ConnectHandler
import json

hosts = ['192.168.51.31', '192.168.51.32', '192.168.51.33', '192.168.51.34', '192.168.51.35', '192.168.51.36']


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
            result = ssh_connect.send_command("show version", use_textfsm=True)
            print(json.dumps(result,indent=2))

