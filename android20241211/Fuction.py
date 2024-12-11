import subprocess
import time
import re
import sys
import serial
import random
import os
import config
#!/usr/bin/python
# coding=UTF-8

def forget_network():
    print("**********Beginning 删除所有wifi连接记录**********")
    # 获取网络id列表
    ntid = subprocess.run("adb shell cmd wifi list-networks", stdout=subprocess.PIPE, shell=True, text=True,
                          encoding='utf-8')
    output = ntid.stdout   # 输入数据转化成列表
    rows = output.split('\n')  # 输出数据分割成行
    rows_len = len(rows) #获取行数
    if rows_len > 1:
        # 获取每一列的第一个值即是网络ID， 然后挨个删除
        for i in range(1, rows_len - 1):
            columns = rows[i].split()
            print(f"当前第{i}行连接记录:{rows[i]}")
            print(f"当前第{i}行网络ID是:{columns[0]}")
            subprocess.Popen("adb shell cmd wifi forget-network {}".format(columns[0]), shell=True)
            time.sleep(2)
            print(f'网络ID{columns[0]}被删除')
    else:
        sys.exit(1)
    print("**********End 删除所有wifi连接记录**********")

def connect_network(ap):
    subprocess.Popen("adb shell cmd wifi connect-network {}".format(ap), shell=True, text=True, encoding='utf-8')
    time.sleep(10)
    # 运行ifconfig waln0命令获取wlan0信息
    result = subprocess.run("adb shell ifconfig wlan0", shell=True, stdout=subprocess.PIPE, text=True, encoding='utf-8')
    # ifconfig输出信息分行显示,第二行包含需要的IP地址 print(output[1])  inet addr:192.168.4.103  Bcast:192.168.4.255  Mask:255.255.255.0
    output = result.stdout.splitlines()
    ipline = output[1].split()  # print(output[1].split())  第二行分列显示，第二列包含了IP地址 ['inet', 'addr:192.168.4.103', 'Bcast:192.168.4.255', 'Mask:255.255.255.0']
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'  # 创建一个IP对象
    ips = re.findall(ip_pattern, ipline[1])  # 是一个列表类型 print(ips) ['192.168.4.103']
    ips_string = str(ips[0])  # 列表转换成字符串 print(ips_string) 192.168.4.103
    print("当前IP地址是：", ips_string)
    # print(ips_string.split("."))  ['192', '168', '4', '103']
    gateway_ip = ips_string.split(".")[0] + "." + ips_string.split(".")[1] + "." + ips_string.split(".")[2] + "." + "1"
    # print(gateway_ip) 192.168.4.1
    subprocess.Popen("adb shell ping -c 4 {}".format(gateway_ip), shell=True, text=True)
    time.sleep(5)
    print("当前连接到的网络信息是：", ap)
    
def suspend_resume_byBTRC():
    serial2 = serial.Serial('COM131', 9600)
    print(serial2)
    if serial2.isOpen():
        print("open success")
    else:
        print("open failed")

    try:
        count = 0
        while True:
            print("beginning")
            """待机唤醒"""
            random_int = random.randint(10, 30)
            # time.sleep(int(random_int))
            time.sleep(60)
            count = count + 1
            # serial2.write(b'\xA0\x01\x01\xA2')
            serial2.write(b'\xA0\x01\x00\xA1')
            time.sleep(0.4)
            # serial2.write(b'\xA0\x01\x00\xA1')
            serial2.write(b'\xA0\x01\x01\xA2')
            time.sleep(0.4)
            # serial2.write(b'\xA0\x01\x01\xA2')
            serial2.write(b'\xA0\x01\x00\xA1')
            print(f"enter the button {count}")
            
    except KeyboardInterrupt:
        if serial != None:
            serial.close()
   