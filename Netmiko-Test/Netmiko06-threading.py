
from netmiko import ConnectHandler
import threading
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

def connect_to_device(switch,cli):

    try:
        ssh_connect = ConnectHandler(**switch)
    except:
        print(f'{switch["ip"]} Unreachable')

    else:
        result = ssh_connect.send_command(cli, use_textfsm=True)
        print(json.dumps(result,indent=2))

tasks=[]
if __name__ == '__main__':
    for host in hosts:
        switch=devices_info(host)

        coonect_thrading=threading.Thread(target=connect_to_device, args=(switch,'show version'))
        coonect_thrading.start()
        tasks.append(coonect_thrading)

    for task in tasks:
        #hold the thread, make sure all sub threads done
        task.join()

