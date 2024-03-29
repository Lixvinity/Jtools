import os
import requests
import time
import csv

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        #print(f"File downloaded successfully to: {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def install_optional_pack(pack_name, pack_url, install_folder, csvname):
    user_input = input(f"Do you want to install '{pack_name}'? (0 = yes, 1 = no): ")
    if user_input == "0":
        download_file(pack_url, os.path.join(install_folder, f"{pack_name}.py"))
        update_feature_value(csv_file_path, csvname, True)
        print(f"The installation for {pack_name} is complete.")
    else:
        print(f"{pack_name} will not be installed.")
        update_feature_value(csv_file_path, csvname, False)

def update_feature_value(csv_file, feature_name, new_value):
    configurations = {}

    # Read existing configurations from CSV
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Ensure the row has the expected structure
            if len(row) == 2:
                current_feature_name, current_feature_value = row
                configurations[current_feature_name] = current_feature_value.lower() == 'true'

    # Update the specified feature
    configurations[feature_name] = new_value

    # Write updated configurations back to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for current_feature_name, current_feature_value in configurations.items():
            writer.writerow([current_feature_name, str(current_feature_value)])

def create_folder(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        #print(f"Folder '{folder_path}' created successfully.")
    except Exception as e:
        print(f"Error creating folder '{folder_path}': {e}")

# Welcome message
print("Welcome to the Jtool's setup wizard!")
time.sleep(3)

# Get startup folder
startup_folder = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# Set up Jtools folders
Jaytools = 'C:\\WINJ'
Apps = os.path.join(Jaytools, 'Scripts')
prerequisites = os.path.join(Jaytools, 'Prerequisites')
PrereqScripts = os.path.join(prerequisites, 'scripts')
create_folder(Jaytools)
create_folder(Apps)
create_folder(prerequisites)
create_folder(PrereqScripts)
download_file(url=r"https://raw.githubusercontent.com/Lixvinity/Jtools/main/Prerequisites/Config.csv",destination=f"{PrereqScripts}/Config.csv")
csv_file_path = "C:\WINJ\Prerequisites\scripts\Config.csv"
time.sleep(5)

download_file(url=r"https://raw.githubusercontent.com/Lixvinity/Jtools/main/Prerequisites/RoFixerIcon.ico",destination=f"{prerequisites}/Rofixer.ico")
download_file(url=r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/Compress.ico",destination=f"{prerequisites}/Compress.ico")
#print (startup_folder)
download_file(url=r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/onstart.pyw",destination=f"{startup_folder}/onstart.pyw")
# Optional Packs
optional_packs = input("Would you like to download extra tools/packs? (0 = yes, 1 = no): ")

if optional_packs == "0":
    optional_packs = True
else:
    optional_packs = False
    print("Okay, installing the required packages only!")

# Install optional packs
install_optional_pack("DiscordWebhook", r"https://github.com/Lixvinity/Jtools/raw/main/WebhookMain.py", Apps, "Discord_Webhook_Sender")
install_optional_pack("TwitchDropSniper", r"https://github.com/Lixvinity/Jtools/raw/main/TwitchDropSniper.py", Apps, "Twitch_idler")
install_optional_pack("robloxfix", r"https://raw.githubusercontent.com/Lixvinity/Jtools/main/robloxfix.py", Apps, "Rofixer")
install_optional_pack("PasswordGenerator", r"https://github.com/Lixvinity/Jtools/raw/main/PasswordGenerator.py", Apps, "PasswordGen")
install_optional_pack("ImageCompressor", r"https://github.com/Lixvinity/Jtools/raw/main/ImageCompressor.py", Apps, "ImageCompressor")
