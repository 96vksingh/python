import os
mac=input("mac")
os.system('ifconfig en0 | grep ether')
os.system('sudo ifconfig en0 ether '+mac)
os.system('echo "your changed mac address is"')
os.system('ifconfig en0 | grep ether')
