from operator import index
import requests
import subprocess
import re


"""
先将LAN相关信息提取出来放入到一个空列表中
"""
result = subprocess.run("ipconfig /all",stdout=subprocess.PIPE,text=True,)
output=result.stdout.splitlines()
#print(output)
start_index = output.index('以太网适配器 LAN:')
end_index = output.index('无线局域网适配器 WLAN:')
target_list=[]
for i in range(start_index,end_index):
    target_list.insert(i-start_index,output[i])
#print(target_list)
substring="IPv4 地址"
#使用any函数结合生成器，any函数接受一个迭代器作为参数，返回一个布尔值
if any(substring in s for s in target_list):
    print('*************设备已经连上*************')

    """
    获取IPV4地址
    """
    #获取ipv4那一项的index值
    ipv4_index=target_list.index('   IPv4 地址 . . . . . . . . . . . . : 192.168.1.100(首选) ')
    #拿到index后根据index输出ipv4项目的内容
    ipv4content = target_list[ipv4_index]
    #提取IP地址
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    #转换成字符串
    ipv4addrlist = re.findall(ip_pattern, ipv4content)
    ipv4addr=''.join(ipv4addrlist)
    print('ipv4地址是:',ipv4addr)

    """
    获取网关
    """
    #获取ipv4那一项的index值
    gatway_index=target_list.index('   默认网关. . . . . . . . . . . . . : 192.168.1.1')
    #拿到index后根据index输出ipv4项目的内容
    gatewaycontent = target_list[gatway_index]
    #提取IP地址
    ip_pattern_gateway = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    #转换成字符串
    gateway_addrlist = re.findall(ip_pattern_gateway, gatewaycontent)
    gatway_addr=''.join(gateway_addrlist)
    print('gateway地址是:',gatway_addr)

    """登陆路由器首页"""
    password='1234567890'

    login_url=f"http://{gatway_addr}/login"
    login_data={
        'password':password,
        'login':''
    }

    with requests.session() as session:
        response = session.post(login_url,data=login_data)

        if response.ok:
            print("登陆成功")
        else:
            print("登陆失败")
else:
    print('？？？？？？？？？没有检测到设备，请检查设备连接？？？？？？？？？')
