import csv
import os
import requests

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

def manage_tools(csv_path):
    """Reads a CSV file, manages tool installation/removal based on user input, and updates the CSV file."""
    try:
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            tools = list(reader)

        for tool in tools:
            name = tool['name']
            link = tool['link']
            directory = tool['directory']
            enabled = tool['enabled'].lower() == 'true'
            
            # Ask the user if they want to install the tool
            response = input(f"Do you want to install {name}? (yes/no): ").strip().lower()
            
            if response == 'yes':
                try:
                    response = requests.get(link)
                    response.raise_for_status()
                    with open(directory, 'wb') as file:
                        file.write(response.content)
                    print(f"{name} has been installed at {directory}")
                    tool['enabled'] = 'True'
                except requests.RequestException as e:
                    print(f"Failed to download {name}: {e}")
                    tool['enabled'] = 'False'
            else:
                tool['enabled'] = 'False'
                if os.path.exists(directory):
                    os.remove(directory)
                    print(f"{name} has been removed from {directory}")

        with open(csv_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'link', 'directory', 'enabled'])
            writer.writeheader()
            writer.writerows(tools)
        #print(f"Updated CSV file at {csv_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Define URLs and paths
csv_url = "https://raw.githubusercontent.com/Lixvinity/Jtools/main/Prerequisites/packets.csv"
csv_local_path = r'C:\WINJ\Prerequisites\scripts\packets.csv'

# Download the CSV file
download_file(csv_url, csv_local_path)

# Manage tools based on the downloaded CSV
manage_tools(csv_local_path)
