#!/usr/bin/python
# coding=UTF-8
import serial
import time
import random
import os
import subprocess
import re

ADB_ID = ""
serial2 = serial.Serial('COM20', 9600)
adb_connect = f"adb -s {ADB_ID} shell"
connect_fail="adb.exe: no devices/emulators found"

print(serial2)
if serial2.isOpen():
    print("open success")
else:
    print("open failed")

try:
    count = 0
    fail_count_resume = 0
    os.system(f"adb connect {ADB_ID}")
    time.sleep(2)
    fail_count_suspend = 0
    while True:
        print("beginning")
        """待机"""
        random_int = random.randint(10, 150)
        # time.sleep(int(random_int))
        time.sleep(20)
        daiji_count = 0
        while daiji_count == 0:
            count = count + 1
            # serial2.write(b'\xA0\x01\x01\xA2')
            serial2.write(b'\xA0\x01\x00\xA1')
            time.sleep(0.4)
            # serial2.write(b'\xA0\x01\x00\xA1')
            serial2.write(b'\xA0\x01\x01\xA2')
            time.sleep(0.4)
            # serial2.write(b'\xA0\x01\x01\xA2')
            serial2.write(b'\xA0\x01\x00\xA1')
            print("待机")
            time.sleep(10)
            adb_connect = subprocess.Popen(args=adb_connect, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                              shell=True)
            for line in adb_connect.communicate():
                if re.match(connect_fail, line.decode("utf-8")):
                    print("now the tv is in sleep")
                    daiji_count == 1
                    break
                fail_count_suspend= fail_count_suspend + 1
                print(f"待机失败一次，{fail_count_suspend}")


        """唤醒"""
        random_int = random.randint(10, 150)
        # time.sleep(int(random_int))
        time.sleep(20)
        count = count + 1
        # serial2.write(b'\xA0\x01\x01\xA2')
        serial2.write(b'\xA0\x01\x00\xA1')
        time.sleep(0.4)
        # serial2.write(b'\xA0\x01\x00\xA1')
        serial2.write(b'\xA0\x01\x01\xA2')
        time.sleep(0.4)
        # serial2.write(b'\xA0\x01\x01\xA2')
        serial2.write(b'\xA0\x01\x00\xA1')
        print("待机")
        time.sleep(10)
        adb_connect = subprocess.Popen(args=adb_connect, stdin=None, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        for line in adb_connect.communicate():
            if re.match(connect_fail, line.decode("utf-8")):
                print("now the tv is in not connect")
                while True:
                    pass


        count=count + 1
        print(f"待机失败一次，{fail_count_suspend}")
        print(f"测试次数，{count}")

except KeyboardInterrupt:
    if serial != None:
        pass