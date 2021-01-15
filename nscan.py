#!/usr/bin/python3

#   IMPORTS

import subprocess as sp
import os
from colors import color
import socket

#   END IMPORTS


#   DEFINES

def get_ip():   # This function gets your private IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP



def ping_device(IP, END='10'):    # This function does the ping to all ip at the range
    
    host_up = []; no_response = []; ping_failed = []

    with open(os.devnull, 'w') as DEVNULL:
        for num in range(1, int(END)+1):
            try: 
                addr = IP[:10] + str(num)
                res = sp.check_call(
                    ['ping', '-c', '1', '-i', '1', '-q', addr],
                    stdout=DEVNULL,
                    stderr=DEVNULL
                )

                if res == 0:
                    host_up.append(addr)
                    print(f"{color.GREEN}OK{color.END} -> {addr}")

                elif res == 1:
                    no_response.append(addr)
                    print(f"{color.YELLOW}NO RESPONSE{color.END} -> {addr}")

            except sp.CalledProcessError:
                ping_failed.append(addr)
                print(f"{color.RED}PING FAILED{color.END} -> {addr}")
            
    return host_up, no_response, ping_failed
            
            

def to_file(HU, NR, PF):    # This function send the ip list to plain text files.

    HU_file = open("host_up", "w")
    NR_file = open("no_response", "w")
    PF_file = open("ping_failed", "w")

    for addr in HU:
        HU_file.write(addr)
        HU_file.write('\n')
    
    for addr in NR:
        NR_file.write(addr)
        NR_file.write('\n')
    
    for addr in PF:
        PF_file.write(addr)
        PF_file.write('\n')

#   END DEFINES


#   MAIN
ip = get_ip()

lists = ping_device(ip, '15')

to_file(lists[0], lists[1], lists[2])


print(" Hosts UP ".center(50, '-'))
for addr in lists[0]:
    print(addr.center(50, ' '))

print('\n', " Hosts DOWN ".center(50, '-'))
for addr in lists[2]:
    print(addr.center(50, ' '))

