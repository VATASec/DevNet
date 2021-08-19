import telnetlib 
import getpass
from pprint import pprint
import time

def read_prompt(tn,prompt,delay=2):
    time.sleep(delay)
    return tn.read_until(bytes(prompt,'utf-8'))

def send_command(tn,command,return_char='\n'):
    command += return_char
    tn.write(bytes(command,'utf-8'))

def login(username,password):
    if username :
        read_prompt(tn,"login: ")
        send_command(tn,username)
        if password : 
            read_prompt(tn,"Password:")
            send_command(tn,password)
    output = read_prompt(tn,">",5)
    if output:
        print('done!')
# device information
HOST = "192.168.2.81"
username = input("Enter your username :")
password = getpass.getpass()
#connecting
tn = telnetlib.Telnet(HOST)
login(username,password)
#doing something
send_command(tn,'show configuration | no-more')
d = read_prompt(tn,'>',4)
print(d)


