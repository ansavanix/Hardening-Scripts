
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
print ("This script should be ran as root")
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
print("Checking Sticky Bit")
cmd("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d -perm -0002 2>/dev/null | xargs chmod a+t")
print("Checking Automount")
cmd("systemctl is-enabled autofs")
cmd("systemctl disable autofs")
print("Checking APT policy")
cmd("apt-cache policy")
print("Manually Review the apt-cache policy")
pause()
print("Checking GPG Keys")
cmd("apt-key list")
print("Manually review GPG Keys")
pause()
print("Ensuring AIDE is installed")
cmd("dpkg -s aide")
cmd("apt-get install aide aide=common")
cmd("aideinit")
print("Checking AIDE configuration")
cmd("crontab -u root -l | grep aide")
cmd("grep -r aide /etc/cron.* /etc/crontab")
print("Ensure a cron job in compliance with site policy is returned")
print("If not run 'crontab -u root -e'")
print("Then add the line '0 5 * * * /usr/bin/aide --config /etc/aide/aide.conf --check'")
pause()
print("Checking Uid and Gid status")
cmd("stat /boot/grub/grub.cfg")
cmd("chown root:root /boot/grub/grub.cfg")
cmd("chmod og-rwx /boot/grub/grub.cfg")
