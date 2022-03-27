from netmiko import ConnectHandler

hosts=[]
with open('hosts') as f:
    for line in f.read().splitlines():
        hosts.append(line)

def device_login(host):
    sw={
        "device_type":"cisco_nxos",
        "username":"admin",
        "password":"cisco!123"
    }
    sw["ip"]=host
    return sw

def get_neighbor(host):
    neighbor_list=[]
    switch = device_login(host)
    ssh_connnect=ConnectHandler(**switch)
    #interface_info=ssh_connnect.send_command('show int bri',use_textfsm=True)
    neighbor_info=ssh_connnect.send_command('show cdp neighbors', use_textfsm=True)
    #print(interface_info)
    #print(neighbor_info)
    for neighbor in neighbor_info:

        if neighbor['local_interface']!='mgmt0':

            neighbor_list.append({neighbor['neighbor']:neighbor['local_interface']})

    return  neighbor_list

def get_version_info(host):
    switch=device_login(host)
    ssh_connection=ConnectHandler(**switch)
    result=ssh_connection.send_command('show version', use_textfsm=True)
    return result



get_version_info('192.168.51.31')




