import os
import time
import shutil

folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'

deleteFileCount = 0
deleteFolderCount = 0

big_ver = "1"
mini_ver = ".1.0"
version = "(" + big_ver + mini_ver + ")"

"""
Priority Level Value	Priority Level Name
256	                    Realtime
128	                    High
32768	                Above normal
32	                    Normal
16384	                Below normal
64	                    Low
"""

# sets these processes to their respective priorities
low = ["Discord.exe", "DiscordPTB.exe", "steamwebhelper.exe", "firefox.exe", "chrome.exe"]
normal = []
high = []
real = ["GeometryDash.exe", "WORSTGDPS.exe"]

def lowpriority():
    for i in low:
        process_change = 'wmic process where name="' + i + '" CALL setpriority "64"'
        print(process_change)
        os.system(process_change)
        os.system('cls')

def normalpriority():
    for i in normal:
        process_change = 'wmic process where name="' + i + '" CALL setpriority "32"'
        print(process_change)
        os.system(process_change)
        os.system('cls')

def highpriority():
    for i in high:
        process_change = 'wmic process where name="' + i + '" CALL setpriority "128"'
        print(process_change)
        os.system(process_change)
        os.system('cls')

def realpriority(): # sets to high for some reason lmfao
    for i in real:
        process_change = 'wmic process where name="' + i + '" CALL setpriority "256"'
        print(process_change)
        os.system(process_change)
        os.system('cls')

def process():
    realpriority()
    #highpriority()
    #normalpriority()
    lowpriority()
    return("All processes set correctly.")

print("\033[1;37;40mGD Optimizer Version", version , "\n\033[1;31;40mWarning: You will need to relaunch \nthis everytime you open GD, or join a new discord call.", "\033[1;37;40m\n" + process())
print("Running Temp Cleaner...")
time.sleep(3)

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    indexNo = file_path.find('\\')
    itemName = file_path[indexNo+1:]
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print( '%s file deleted' % itemName )
            deleteFileCount = deleteFileCount + 1

        elif os.path.isdir(file_path):
            if file_path.__contains__('chocolatey'):  continue
            shutil.rmtree(file_path)
            print( '%s folder deleted' % itemName )
            deleteFolderCount = deleteFolderCount + 1

    except Exception as e:
        print('Access Denied: %s' % itemName )

print(str(deleteFileCount)+' files and '+ str(deleteFolderCount)+' folders deleted.')
time.sleep(1)
print("Closing in 5 seconds...")
time.sleep(5)