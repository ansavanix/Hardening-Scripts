import os
print ("Ensuring mounting of cramfs filesystems is disabled")
os.system("modprobe -n -v cramfs")
os.system("install /bin/true")
os.system("lsmod | grep cramfs")
print ("If there is a cramfs device mounted run 'install crafms /bin/true' then 'rmmod cramfs'")
print ("Starting Next Task...")