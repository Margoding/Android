import subprocess
import time
import re
import sys
import config
import Fuction

def wificonnect(ap):
	Fuction.forget_network()
	Fuction.connect_network(ap)
	
wificonnect(config.ap1)


