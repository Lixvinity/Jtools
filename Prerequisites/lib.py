import subprocess
import sys
import csv

def install_libraries(libraries):
    for library in libraries:
        print(f"staring download for {libraries}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            print(f"Successfully installed {library}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {library}. Error: {e}")

install_libraries("requests")

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

download_file(r"https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/lib.csv",r"C:\WINJ\Prerequisites\scripts\Libs.csv")

csv_file_path = r"C:\WINJ\Prerequisites\scripts\Libs.csv"


with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file and print it
    for row in csv_reader:
        # Print each item in the row (there will only be one item per row)
        for item in row:
            install_libraries(item)
    print("finished")