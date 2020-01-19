def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
    
def clear():
    os.system("clear")
    
def cmd(command):
    os.system(command)
    
def checkfs(fs):
    print("Checking " + fs)
    cmd("modprobe -n -v " + fs)
    cmd("lsmod | grep " + fs)
    f.write("install " + fs + " /bin/true\r\n")
    cmd("rmmod " + fs)
        
    

import os
clear()
print (" Generic Automated Linux Auditing System")
print ("This script is provided as is with no warranties or guarantees what so ever.")
print ("Created by Anthony Saldana-Valle based off CIS Independent Linux Benchmark v2.0.0.")
print ("This script should be ran as root.")
print ("Have a second terminal open in case manual remediation is required.")
pause()
print("CHECKING FILESYSTEMS")
f= open("/etc/modprobe.d/CIS.conf","w+")
checkfs("cramfs")
checkfs("freevxfs")
checkfs("jffs2")
checkfs("hfs")
checkfs("hfsplus")
checkfs("udf")
f.close