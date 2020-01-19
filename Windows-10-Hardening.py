def pause():
    os.system("pause")
    
def clear():
    os.system("cls")
    
def cmd(command):
    os.system(command)
    
def netacc(sub,num):
    print("Configuring "+ sub + ":" + num)
    cmd("net accounts /" + sub + ":" + num)
 
import subprocess
import os
clear()
cmd("@echo off")
cmd("color 0a")
print ("Automated Windows 10 Auditing System")
print ("This script is provided as is with no warranties or guarantees what so ever.")
print ("Created by Anthony Saldana-Valle based off CIS Microsoft Windows 10 Benchmark v1.8.0")
print ("This script should be ran as administrator to avoid issues.")
pause()
netacc("minpwlen","14")
netacc("maxpwage","60")
netacc("minpwage","1")
netacc("uniquepw","24")
netacc("forcelogoff","60")