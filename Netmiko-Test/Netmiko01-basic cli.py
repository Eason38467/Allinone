from netmiko import ConnectHandler


#这里讲下getpass模块。getpass是Python的内建模块，无须通过pip下载安装即可使用。它和input()函数一样，都是Python的交互式功能，用来提示用户输入密码，区别是如果用input()输入密码，用户输入的密码是明文可见的，如果你身边坐了其他人，密码就这么暴露了。而通过getpass输入的密码则是隐藏不可见的，安全性很高，所以强烈建议使用getpass来输入密码，使用input()来输入用户名。
import getpass

device_info = {
    "device_type":"cisco_nxos",
    "ip":"192.168.51.31",
    "username":"admin1",
    "password":"cisco!123",
               }

ssh_connect = ConnectHandler(**device_info)
show_info = ssh_connect.send_command("show version")
print(show_info)

config_commands = ['int lo 1', 'ip addr 1.1.1.1/24']
output = ssh_connect.send_config_set(config_commands)
print(output)


