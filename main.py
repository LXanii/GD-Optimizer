import os
import time
import shutil
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GD Optimizer")
        self.geometry("500x500")
        self.resizable(True, True)

        # Create label for version
        self.version = tk.StringVar()
        self.version.set("(1.1.0)")
        self.label_version = tk.Label(self, textvariable=self.version)
        self.label_version.pack()

        # Create button to run optimization
        self.button_optimize = tk.Button(self, text="Optimize", command=self.optimize)
        self.button_optimize.pack()

        # Create button to run temp cleaner
        self.button_clean = tk.Button(self, text="Clean Temp", command=self.clean_temp)
        self.button_clean.pack()

        # Create label for status messages
        self.status = tk.StringVar()
        self.label_status = tk.Label(self, textvariable=self.status)
        self.label_status.pack()

        # Set process priority levels
        self.low = ["Discord.exe", "steamwebhelper.exe", "firefox.exe", "chrome.exe", "Spotify.exe", "MsMpEng.exe", "brave.exe", "WSHelper.exe"]
        self.normal = []
        self.high = []
        self.real = ["GeometryDash.exe"]

    def optimize(self):
        self.status.set("Setting process priorities...")
        self.realpriority()
        self.lowpriority()
        self.status.set("All processes set correctly. Make Sure To Re Run This Everytime You Get In A Call")

    def realpriority(self):
        for i in self.real:
            process_change = 'wmic process where name="' + i + '" CALL setpriority "256"'
            os.system(process_change)

    def lowpriority(self):
        for i in self.low:
            process_change = 'wmic process where name="' + i + '" CALL setpriority "64"'
            os.system(process_change)

    def clean_temp(self):
        self.status.set("Running Temp Cleaner...")

        # Get path to Temp folder
        folder = f'C:/Users/{os.getlogin()}/AppData/Local/Temp'

        # Initialize counters for deleted files and folders
        delete_file_count = 0
        delete_folder_count = 0

        # Iterate through files and directories in Temp folder
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            index_no = file_path.find('\\')
            item_name = file_path[index_no+1:]
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    delete_file_count += 1

                elif os.path.isdir(file_path):
                    if file_path.__contains__('chocolatey'):
                                           continue
                    shutil.rmtree(file_path)
                    delete_folder_count += 1
            except Exception as e:
                self.status.set(f'Access Denied: {item_name}')

        self.status.set(f'{delete_file_count} files and {delete_folder_count} folders deleted.')

if __name__ == "__main__":
    app = App()
    app.mainloop()

