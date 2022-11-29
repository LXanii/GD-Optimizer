import os
import time
import wmi

# For 2.0.0, make into a dll with more optimizations

pcount = 0

processes = wmi.WMI ()
"""
for process in processes.Win32_Process(name="discord.exe"):
    print(process.ProcessId, process.Name)
    pcount += 1

if pcount == 0:
    print("No optimizable process found. [discord.exe]")
else:
    print("Processes found. [discord.exe]", "(" + str(pcount) + ")")

for process in processes.Win32_Process(name="firefox.exe"):
    print(process.ProcessId, process.Name)
    pcount += 1

if pcount == 0:
    print("No optimizable process found. [firefox.exe]")
else:
    print(str(pcount) + " Processes found. [firefox.exe]")
"""
# finds processes ^^^

red = "\033[1;31;40m"
white = "\033[1;37;40m"
first = True
big_ver = "2"
mini_ver = ".0.0"
version = white + " (" + big_ver + mini_ver + ")"
title = white + "GD Optimizer Version"

# sets these processes to their respective priorities
low = ["Discord.exe", "steamwebhelper.exe", "firefox.exe", "chrome.exe"]
normal = []
high = []
real = ["GeometryDash.exe"]

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
    time.sleep(1)
    realpriority()
    #highpriority() these 2 do nothing as of now
    #normalpriority()
    lowpriority()
    return(white + "\nAll processes set correctly.")

# work here on finding processes vvvv

while True:
    if first == True:
        print(title + version, red + "\n\nWarning: You will need to relaunch \nthis everytime you open GD.\n", process() + "\n")
        first = False
        time.sleep(1)
    else:
        print(title + version, red + "\n\nWarning: You will need to relaunch \nthis everytime you open GD.\n")
    print(white + "Looping Discord Priority... \n\n" + red + "Do not exit the program.")
    time.sleep(5)
    i = "Discord.exe"
    process_change = 'wmic process where name="' + i + '" CALL setpriority "64"'
    os.system(process_change)
    os.system('cls')
