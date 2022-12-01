from colorama import Fore, init
import os
import time
import wmi

# For 2.0.0, make into a dll with more optimizations

init() # used cuz colors just didnt work before and google said this fixed it

first = True
close = False
pcount = 0
big_ver = "2"
mini_ver = ".0.0"
version = " (" + big_ver + mini_ver + ")"
title = "GD Optimizer Version"
processes = wmi.WMI()

# sets these processes to their respective priorities
low = ["Discord.exe", "steamwebhelper.exe", "firefox.exe", "chrome.exe", "Spotify.exe", "MsMpEng.exe"]
normal = []
high = ["GeometryDash.exe"]

# MsMpEng.exe is windows defender service, which in cases can lag.

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

def priority_change():
    time.sleep(1)
    highpriority()
    #normalpriority() this is used for nothing rn
    lowpriority()
    return(Fore.WHITE + "\nAll processes set correctly.")

# functions above ^^^^^^^

print(title + version, "\n")

for i in low:
    for process in processes.Win32_Process(name=i):
        pcount += 1
    if pcount == 0:
        print(Fore.RED + "No optimizable process found. " + "[" + i + "]")
        low.remove(i)
    else:
        print(Fore.GREEN + str(pcount) + " Processes found. " + "[" + i + "]")
    pcount = 0

for i in high:
    for process in processes.Win32_Process(name=i):
        pcount += 1
    if pcount == 0:
        print(Fore.RED + "No optimizable process found. " + "[" + i + "]")
        if i == "GeometryDash.exe":
            close = True
            high.remove(i)
        else:
            high.remove(i)
    else:
        print(Fore.GREEN + str(pcount) + " Processes found. " + "[" + i + "]")
    pcount = 0

print("\n" + Fore.WHITE + "Optimizing...\n")
time.sleep(2)

while True:
    if close == False:
        if first == True:
            first = False
            time.sleep(1)
        else:
            print(Fore.WHITE + title + Fore.WHITE + version, "\n")
        print(Fore.WHITE + "Looping Discord Priority... \n\n" + Fore.RED + "Do not close this window.")
        time.sleep(5)
        i = "Discord.exe"
        process_change = 'wmic process where name="' + i + '" CALL setpriority "64"'
        os.system(process_change)
        os.system('cls')
    else:
        error = "GeometryDash.exe was not found." + "\n\n" + Fore.RED + "Closing Program..."
        print(Fore.YELLOW + str(error))
        time.sleep(3)
        break
