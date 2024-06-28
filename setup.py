import os
from subprocess import Popen
import sys
import time
import win32com.client

directory_script = r"C:\WINJ\Prerequisites\scripts\CreateDirectories.py"
libs_script = r"C:\WINJ\Prerequisites\scripts\lib.py"
select_tools = r"C:\WINJ\Prerequisites\scripts\SelectPackages.py"


def run_program(directory):
    # Function to run the program
    Popen(directory, shell=True)

print("creating Jtool's directory")
time.sleep(1)
run_program(directory_script)
print("done")
time.sleep(1)
print("starting install on libraries")
time.sleep(3)
run_program(libs_script)

import requests

startup_folder = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

def download_file(url, local_filename):
    """Downloads a file from a URL and saves it locally."""
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"Downloaded {local_filename} from {url}")
    except requests.RequestException as e:
        print(f"Failed to download file: {e}")

download_file(r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/onstart.pyw", f"{startup_folder}/onstart.pyw")
run_program (f"{startup_folder}/onstart.pyw")

icon = r"C:\WINJ\Prerequisites\Jtoolspro.ico"
jtoolshub = r"C:\WINJ\Prerequisites\scripts\JtoolsHub.py"

download_file(r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/JtoolsHub.py", jtoolshub)
download_file(r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/SelectPackages.py", f"C:\WINJ\Prerequisites\scripts\SelectPackages.py")
download_file(r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/lib.py", f"C:\WINJ\Prerequisites\scripts\lib.py")
download_file(r"https://raw.githubusercontent.com/Lixvinity/Jtools/main/Prerequisites/Jtoolspro.ico", icon)
time.sleep(1)
run_program(select_tools)

def create_shortcut(name, target, icon=None):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    shortcut_path = os.path.join(desktop, f"{name}.lnk")
    
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    
    if icon:
        shortcut.IconLocation = icon
    
    shortcut.save()
    print(f"Shortcut '{name}' created on the desktop.")

shortcut_name = "Jtools"
target_path = jtoolshub
icon_path = icon # Optional

create_shortcut(shortcut_name, target_path, icon_path)
