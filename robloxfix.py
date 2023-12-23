#JTOOLS
import os
import random
import time
import requests
import shutil
import subprocess
import tempfile



def find_file_in_folder(folder_path, file_name):
    for root, dirs, files in os.walk(folder_path):
        if file_name in files:
            return os.path.join(root, file_name)

    return None  # File not found
def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to: {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
def find_folder(start_folder):
    for root, dirs, files in os.walk(start_folder):
        return root

    return None  # Folder not found
def delete_folder(directory):
    try:
        shutil.rmtree(directory)
        print(f"Folder '{directory}' successfully deleted.")
    except Exception as e:
        print(f"Error deleting folder '{directory}': {e}")
def run_file(file_path):
    try:
        result = subprocess.run([file_path], check=True, shell=True)
        print(f"The file executed successfully with return code {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing the file: {e}")
def download_roblox_run():
    download_file(roblox_installer_url, f"{temp_directory}/RobloxPlayerInstaller.exe")
    run_file(f"{temp_directory}/RobloxPlayerInstaller.exe")



roblox_folder = input(r"Please provide the roblox directory: ")

if roblox_folder is None:
    download_roblox_run()
local_appdata_directory = os.getenv("LOCALAPPDATA")
print (local_appdata_directory)
robloxPLE = ("RobloxPlayerLauncher.exe")
roblox_installer_url = (r"https://setup.rbxcdn.com/RobloxPlayerInstaller.exe")
cache_folder = (f"{local_appdata_directory}/Roblox")
temp_directory = tempfile.gettempdir()

print ("diagnosing problem, please be paitent.")

RPLE_results = find_file_in_folder(roblox_folder, robloxPLE)

if RPLE_results:
    #print(f"File '{robloxPLE}' found at: {RPLE_results}")
    PLE_Found = True
else:
    #print(f"File '{robloxPLE}' not found in the folder.")
    PLE_Found = False

time.sleep(random.randint(6, 8))
print ("trying to apply fix.")

if PLE_Found == False:
    delete_folder(cache_folder)
    download_roblox_run()
else:
    if PLE_Found == True:
        run_file(f"{roblox_folder}/{robloxPLE}")

        
