
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
    
def checkpartition(partition):
    cmd("mount | grep " + partition)
    
def fixpartition(partition):
    cmd("mount -o remount,nodev,nosuid " + partition)
        
    

import os
clear()
print ("Non-Automated Ubuntu Auditing System")
print ("This script is provided as is with no warranties or guarantees what so ever")
print ("Created by Anthony Saldana-Valle based off CIS Ubuntu 16.04 Benchmark v1.1.0")
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
print("Ensuring Partition Security")
checkpartition("/tmp")
fixpartition("/tmp")
checkpartition("/var")
fixpartition("/var")
checkpartition("/var/tmp")
cmd("mount -o remount,nodev,nosuid,noexec /var/tmp")
checkpartition("/var/log")
checkpartition("/var/log/audit")
checkpartition("/home")
cmd("mount -o remount,nodev /home")
checkpartition("/dev/shm")
cmd("mount -o remount,nodev,noexec /dev/shm")
cmd("mount")