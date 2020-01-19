def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
    
def clear():
    os.system("cls")
    
def cmd(command):
    os.system(command)
 
import subprocess
import os
clear()
print ("Automated Windows 10 Auditing System")
print ("This script is provided as is with no warranties or guarantees what so ever.")
print ("Created by Anthony Saldana-Valle based off CIS Microsoft Windows 10 Benchmark v1.8.0")
print ("This script should be ran as administrator to avoid issues.")
pause()