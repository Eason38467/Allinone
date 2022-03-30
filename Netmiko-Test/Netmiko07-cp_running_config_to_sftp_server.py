from netmiko import ConnectHandler
import time

switch = {
    "device_type": "cisco_nxos",
    "username": "xxxx",
    "password": "xx!xxxxxx",
    "ip": "xxxxxx"
}

now = time.strftime("%Y-%m-%d",time.localtime(time.time()))

filename="N7K" + "_" + now + ".txt"
#"copy running-config sftp://nfs:nfs@10.124.145.88//storage/Backup/Nexus/ACI_N7K/{filename} vrf management"
cmd=f"copy running-config sftp: vrf management"

path='/storage/Backup/Nexus/ACI_N7K/' + filename

if __name__ == '__main__':
    try:
        ssh_connect = ConnectHandler(**switch)
        print(cmd)
    except:
        print(f'{switch["ip"]} Unreachable')

    else:
        result = ssh_connect.send_command_timing(cmd)
        print('path')
        result+= ssh_connect.send_command_timing(path)
        print('server')
        result+= ssh_connect.send_command_timing('10.124.145.88')

        print('username')
        result+= ssh_connect.send_command_timing('nfs')
        print('pass')

        result+=ssh_connect.send_command_timing('nfs')
        print(result)
