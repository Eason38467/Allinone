import netmiko
from ping3 import ping
import threading

# 定义在用的IP列表
OnLineHost = []

# 定义offline 或者为用的IP 列表
OffLineHost = []

def genHostIP(IP):

    #获取网段
    network=IP.split('/')[0]
    #获取掩码
    mask = int(IP.split('/')[1])
    #获取主机数量
    hostnumber= 2**(32-mask)-2
    #获取IP地址范围，xxx.xxx.xxx.xxx
    #每个地址段的数量是2**8 个

    tempip=network.split('.')[0]+'.'+network.split('.')[1]+'.'+network.split('.')[2]
    hosts=[]
    minhostip=int(network.split('.')[3])
    i=0
    while i < hostnumber:
        if minhostip <254:
            minhostip = minhostip + 1
            hostip = tempip + '.' + str(minhostip)
            hosts.append(hostip)
            i=i+1
        else:
            break

    return hosts


def pingHost(hosts):

    second = ping(hosts,unit='ms',timeout=1)
        #ping方法 如果IP不通，返回None，通过if语句分别记录通和不通的主机
        #{second:.2f}  小数点后保留两位

    if second !=None:
        print(f"{hosts} is alive, it took {second:.2f} ms")
        OnLineHost.append(hosts)
    else:
        print(f"{hosts} offline")
        OffLineHost.append(hosts)

#create empty thread pool
tasks=[]

if __name__ == '__main__':
    IP='192.168.50.0/24'

    hosts = genHostIP(IP)


    for host in hosts:

        #creat multi threads ,
        ping_thread = threading.Thread(target=pingHost, args=(host,))
        #start each threads
        ping_thread.start()
        #drop threads into thread pool
        tasks.append(ping_thread)

    for task in tasks:
        #hold the thread, make sure all sub threads done
        task.join()

    print(OnLineHost)
    print(len(OnLineHost))
    print(len(OffLineHost))
    print(OffLineHost)

