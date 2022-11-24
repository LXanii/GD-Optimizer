import os

big_ver = "1"
mini_ver = ".0.0"

def gd():
    try:
        os.system('wmic process where name="GeometryDash.exe" CALL setpriority "256"')
        os.system('cls')
        return("Geometry Dash set to High Priority.")
    except:
        return("Process not found. [GeometryDash.exe]")

def dc():
    try:
        os.system('wmic process where name="discord.exe" CALL setpriority "64"')
        os.system('cls')
        return("Discord set to Low Priority.")
    except:
        return("Process not found. [discord.exe]")

print("\033[1;37;40mGD Optimizer Version", "(" + big_ver + mini_ver + ")", "\n\033[1;31;40mWarning: You will need to relaunch \nthis everytime you open GD, or Discord.", "\033[1;37;40m\n" + dc(), "\n" + gd())
close = str(input("\033[1;32;40mPress 'ENTER' to close."))