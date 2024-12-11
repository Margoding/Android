import subprocess
import time
import re
import sys
import config
import Fuction

def suspend_resume_wificonnect_disconnect(count):

	Fuction.forget_network()
	while count>0:
		print("第{}次",count)
		count-=1
		Fuction.connect_network(config.ap1)
		Fuction.suspend_resume_byBTRC()
		Fuction.connect_network(config.ap2)
		Fuction.suspend_resume_byBTRC()
		
suspend_resume_wificonnect_disconnect(config.count)
