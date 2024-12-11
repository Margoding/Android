import subprocess
import time
import re
import sys
import config
import Fuction


def apswitch(count):
	i=0
	time.sleep(5)
	while count > 0:
		i+=1
		count -= 1
		Fuction.forget_network()
		print(f"第{i}次AP切换 ")
		Fuction.connect_network(config.ap1)
		time.sleep(6)
		Fuction.connect_network(config.ap2)
		time.sleep(6)
		Fuction.connect_network(config.ap3)


apswitch(config.count)