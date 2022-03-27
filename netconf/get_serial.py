from ncclient import manager
import sys
from lxml import etree

# Set the device variables

DEVICES = ['192.168.51.35']
USER = 'admin'
PASS = 'cisco!123'
PORT = 830
DEVICE_NAMES = {'192.168.51.35': '(nx-osv9000-1)'}


# create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    serial_number = """
    <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <serial/>
    </System>
    """

    for device in DEVICES:
        with manager.connect(host=device, port=PORT, username=USER,
                             password=PASS, hostkey_verify=False,
                             device_params={'name': 'nexus'},
                             look_for_keys=False, allow_agent=False) as m:
            # Collect the NETCONF response
            netconf_response = m.get(('subtree', serial_number))
            print(netconf_response)
            # Parse the XML and print the data
            xml_data = netconf_response.data_ele

            # 这里我们继续对过滤后的内容调用.data.find()函数，该函数的参数始终以.//开头，后面配上{命名空间}标签的形式来匹配出该标签里的实际内容，这里的{http://cisco.com/ns/yang/cisco-nx-os-device}即为命名空间，serial即为标签.
            serial = xml_data.find(".//{http://cisco.com/ns/yang/cisco-nx-os-device}serial").text

            print("The serial number for {} {} is {}".format(DEVICE_NAMES[device], device, serial))


if __name__ == '__main__':
    sys.exit(main())



"""https://github.com/kiskander/nxos-yang-learning-labs/tree/master/01-yang"""