# after configuring mgmt port, we can use this script to change hostnames of switches, gen a switch
import netmiko
from netmiko import ConnectHandler


class Switch:

    def __init__(self, hostname, mgmtIP, version):
        self.hostname = hostname
        self.mgmtIP = mgmtIP
        self.version = version

    def deviceinfo(self):

        return self.hostname, self.mgmtIP, self.version

    def getinfo(self):
        pass

    def baiscconf(self):

        host = {
            "device_type": "cisco_nxos",
            "username": "admin",
            "password": "cisco!123",
        }
        host["ip"] = self.mgmtIP
        try:
            ssh_connect = ConnectHandler(**host)
        except netmiko.ssh_exception.NetmikoTimeoutException:
            print(f"{self.mgmtIP} is unreachable")
        except netmiko.ssh_exception.NetmikoAuthenticationException:
            print(f"{self.mgmtIP} login fail, Ivalid username or password")
        else:
            ssh_connect.send_config_set(f'hostname {self.hostname}')
            print("hostname updated")

    def backupconf(self):
        pass

    def changeversion(self):
        pass

    def reload(self):
        pass


def main():


    pass


if __name__ == '__main__':
    main()
