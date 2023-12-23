import csv
import os
import requests

# Function to download a file from a given URL
def download_file_with_url(url, destination, override=False):
    if not override and os.path.exists(destination):
        print(f"File '{destination}' already exists. Skipping download.")
        return

    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

# CSV file path
csv_file_path = "C:\\WINJ\\Prerequisites\\scripts\\Config.csv"  # Replace with the path to your CSV file

# Function to process tasks from the CSV file
def process_tasks(csv_reader):
    # Skip the header row
    next(csv_reader, None)

    # Iterate through rows and check if the variable is 'True'
    for row in csv_reader:
        task_name = row[0]
        should_download = row[1].strip().lower()  # Stripping leading/trailing spaces and converting to lowercase

        if should_download == 'true':
            url_for_task = get_url_for_task(task_name)  # Replace with your logic to get the URL for each task
            destination_path = os.path.join("C:\WINJ\Scripts", f'{task_name}.py')  # Replace 'download_directory' with the directory where you want to save the downloaded files

            # Download the file, and override if it already exists
            download_file_with_url(url_for_task, destination_path, override=True)
            print(f"File for task '{task_name}' downloaded successfully.")

# Function to get the URL for each task (replace with your logic)
def get_url_for_task(task_name):
    # Replace with your logic to get the URL for each task
    # For example, you can have a dictionary mapping task names to URLs
    url_mapping = {
        'Discord_Webhook_Sender': 'https://github.com/Lixvinity/Jtools/raw/main/WebhookMain.py',
        'Twitch_idler': 'https://github.com/Lixvinity/Jtools/raw/main/TwitchDropSniper.py',
        'Rofixer': 'https://github.com/Lixvinity/Jtools/raw/main/robloxfix.py',
        # Add more mappings as needed
    }
    return url_mapping.get(task_name, '')

# Check if the CSV file exists
if os.path.exists(csv_file_path):
    # Open the CSV file and read the rows
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        process_tasks(csv_reader)
else:
    print(f"CSV file '{csv_file_path}' not found.")
