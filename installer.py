import os

installs = ["colorama", "time", "wmi"]

for i in installs:
    print(i.upper() + "\n")
    os.system("pip install " + i)

close = input("\nPython Requirements Installed. You may now open the optimizer.")