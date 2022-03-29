from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file='config.yaml')
leaf=nr.filter(F(groups__contains='leaf'))
spine=nr.filter(~F(group__contains='spine'))
results=leaf.run(netmiko_send_command,command_string='show ip int bri')

print_result(results)