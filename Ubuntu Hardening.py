
def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
    
def clear():
    os.system("clear")

import os
clear()
print ("Non-Automated Ubuntu Auditing System")
print ("This script is provided as is with no warranties or guarantees what so ever")
print ("Created by Anthony Saldana-Valle based off CIS Ubuntu 16.04 Benchmark v1.1.0")
pause()
print("CHECKING CRAMFS STATUS...")
os.system ("modprobe -n -v cramfs")
os.system ("lsmod | grep cramfs")
pause()
print("There should be no output.")
pause()
print("If there is output follow the instructions below.")
print("Create the file /etc/modprobe.d/CIS.conf if it does not already exist")
print("Add the following line'install cramfs /bin/true'")
print("run the command 'rmmod cramfs'")
print("After following these instructions mounting of cramfs filesystems should be disabled")
pause()
clear()