
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
    f.write("install " + fs + "/bin/true\n")
    cmd("rmmod " + fs)

import os
clear()
print ("Non-Automated Ubuntu Auditing System")
print ("This script is provided as is with no warranties or guarantees what so ever")
print ("Created by Anthony Saldana-Valle based off CIS Ubuntu 16.04 Benchmark v1.1.0")
pause()
print("CHECKING FILESYSTEMS")
f= open("/etc/modprobe.d/cis.conf","w+")
checkfs("cramfs")
checkfs("freevxfs")
checkfs("jffs2")
checkfs("hfs")
checkfs("hfsplus")
checkfs("udf")
f.close
