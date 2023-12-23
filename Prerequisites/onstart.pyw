import requests
import subprocess
import os

def download_and_open_file(url, destination_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        with open(destination_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded successfully to {destination_path}")

        # Debug: Print the content of the downloaded file
        with open(destination_path, 'rb') as file:
            file_content = file.read()
            print(f"\nFile content:\n{file_content.decode('utf-8')}")

        # Open the file using the default Python interpreter for .pyw files
        python_executable = 'pythonw.exe' if os.name == 'nt' else 'pythonw'
        subprocess.run([python_executable, destination_path])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace the URL with the URL of the .pyw file you want to download
    file_url = "https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/autoupdater.pyw"
    
    # Replace the destination path with the path where you want to save the .pyw file
    destination_path = r"C:\WINJ\Prerequisites\scripts\autoupdater.pyw"
    
    # Download and open the .pyw file
    download_and_open_file(file_url, destination_path)

