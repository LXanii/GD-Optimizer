import os
import time
import wmi

# For 2.0.0, make into a dll with more optimizations

red = "\033[1;31;40m"
white = "\033[1;37;40m"
first = True
close = False
pcount = 0
big_ver = "2"
mini_ver = ".0.0"
version = " (" + big_ver + mini_ver + ")"
title = "GD Optimizer Version"
processes = wmi.WMI()

# sets these processes to their respective priorities
low = ["Discord.exe", "steamwebhelper.exe", "firefox.exe", "chrome.exe"]
normal = []
high = []
real = ["GeometryDash.exe"]

#####################################

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

def priority_change():
    time.sleep(1)
    realpriority()
    #highpriority() these 2 do nothing as of now
    #normalpriority()
    lowpriority()
    return(white + "\nAll processes set correctly.")

# functions above ^^^^^^^

print(title + version, "\n")

for i in low:
    for process in processes.Win32_Process(name=i):
        pcount += 1
    if pcount == 0:
        print("No optimizable process found. " + "[" + i + "]")
        low.remove(i)
    else:
        print(str(pcount) + " Processes found. " + "[" + i + "]")
    pcount = 0

for i in real:
    for process in processes.Win32_Process(name=i):
        pcount += 1
    if pcount == 0:
        print("No optimizable processes found. " + "[" + i + "]")
        if i == "GeometryDash.exe":
            close = True
            real.remove(i)
        else:
            real.remove(i)
    else:
        print(str(pcount) + " Processes found. " + "[" + i + "]")
    pcount = 0

print("\nOptimizing...")
time.sleep(2)

while True:
    if close == False:
        if first == True:
            print(white + title + white + version, red + "\n\nWarning: You will need to relaunch \nthis everytime you open GD.\n", priority_change() + "\n")
            first = False
            time.sleep(1)
        else:
            print(white + title + white + version, red + "\n\nWarning: You will need to relaunch \nthis everytime you open GD.\n")
        print(white + "Looping Discord Priority... \n\n" + red + "Do not exit the program.")
        time.sleep(5)
        i = "Discord.exe"
        process_change = 'wmic process where name="' + i + '" CALL setpriority "64"'
        os.system(process_change)
        os.system('cls')
    else:
        print(red + "\nGeometryDash.exe was not found. \n\nClosing Program...")
        time.sleep(3)
        break
