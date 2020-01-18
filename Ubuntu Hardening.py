import os
os.mkdir('/etc/modprobe.d')
print ("Ensuring mounting of cramfs filesystems is disabled")
os.system("modprobe -n -v cramfs")
os.system("install /bin/true")
os.system("lsmod | grep cramfs")
with open('/etc/modprobe.d/CIS.conf', 'w+') as file:
    file.write('install cramfs /bin/true')
