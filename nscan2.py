import subprocess as sp
import os
from colors import color

ping_ok = [0]; no_response = [0]; ping_failed = [0];
sp.run('clear')

with open(os.devnull, 'w') as DEVNULL:
    for ping in range(1,255):
        try:
            addr = "10.194.62." + str(ping)
            res = sp.check_call(
                ['ping', '-c', '1', '-i', '1', '-q', addr],
                stdout=DEVNULL,
                stderr=DEVNULL
                )

            if res == 0:
                ping_ok.append(addr)
                print(f"{color.GREEN}OK{color.END} -> {addr}")

            elif res == 2:
                no_response.append(addr)
                print(f"{color.GREEN}NR{color.END} -> {addr}")
            
            else:
                ping_failed.append(addr)
                print(f"{color.GREEN}PF{color.END} -> {addr}")

                
            
        except sp.CalledProcessError:
            print(f"{color.RED}ERROR{color.END} -> {addr}")
    
print(" PING OK ".center(30, '-'))
for i in ping_ok: print(i)

print(" NO RESPONSE ".center(30, '-'))
for i in no_response: print(i)

print(" PING FAIL ".center(30, '-'))
for i in ping_failed: print(i)


