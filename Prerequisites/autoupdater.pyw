import csv
import os
import requests
import tempfile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_file(url, local_filename):
    """Downloads a file from a URL and saves it locally."""
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        logging.info(f"Downloaded {local_filename} from {url}")
    except requests.RequestException as e:
        logging.error(f"Failed to download file: {e}")

def remove_empty_rows(csv_path):
    """Removes empty rows from the CSV file."""
    try:
        # Read the current CSV and filter out empty rows
        with open(csv_path, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            rows = [row for row in reader if any(value.strip() for value in row.values())]

        # Write the filtered rows back to the CSV
        with open(csv_path, mode='w', newline='') as outfile:
            if rows:
                fieldnames = rows[0].keys()
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            else:
                logging.warning("No non-empty rows found. The CSV file is empty after cleanup.")

    except Exception as e:
        logging.error(f"An error occurred while removing empty rows: {e}")

def append_new_rows(csv_path, url):
    """Downloads the latest CSV, compares with the existing CSV, and appends only new rows."""
    temp_csv_path = None
    try:
        # Create a temporary file for the new CSV
        with tempfile.NamedTemporaryFile(delete=False) as temp_csv_file:
            temp_csv_path = temp_csv_file.name

        # Download the latest CSV from the URL
        download_file(url, temp_csv_path)

        # Read the current CSV
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            existing_rows = list(reader)

        # Read the latest downloaded CSV
        with open(temp_csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            new_rows = list(reader)

        # Convert existing rows to a set of tuples for easy comparison
        existing_rows_set = set((row['name'], row['link'], row['directory']) for row in existing_rows)

        # Filter out rows from the new CSV that are not present in the existing CSV
        rows_to_add = [row for row in new_rows if (row['name'], row['link'], row['directory']) not in existing_rows_set]

        if rows_to_add:
            # Append new rows to the existing CSV
            with open(csv_path, mode='a', newline='') as file:
                fieldnames = ['name', 'link', 'directory', 'enabled']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerows(rows_to_add)
            logging.info(f"Added {len(rows_to_add)} new rows to the CSV.")
        else:
            logging.info("No new rows to add.")

        # Remove any empty rows from the CSV
        remove_empty_rows(csv_path)

        # Download files from the updated CSV
        download_files_from_csv(csv_path)

    except requests.RequestException as e:
        logging.error(f"Request error occurred: {e}")
    except (IOError, OSError) as e:
        logging.error(f"File error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        # Clean up temporary file
        if temp_csv_path and os.path.exists(temp_csv_path):
            os.remove(temp_csv_path)

def download_files_from_csv(csv_path):
    """Downloads files from the CSV based on URL and saves them to the specified paths."""
    try:
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                url = row['link']
                save_path = row['directory']
                
                # Ensure the directory exists
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                # Download and save the file
                download_file(url, save_path)

    except Exception as e:
        logging.error(f"An error occurred while downloading files: {e}")

# Example usage
csv_path = r"C:\WINJ\Prerequisites\scripts\packets.csv"
url = "https://raw.githubusercontent.com/Lixvinity/Jtools/main/Prerequisites/packets.csv"

# Updates hub
download_file("https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/JtoolsHub.py", r"C:\WINJ\Prerequisites\scripts\JtoolsHub.py")

# Append new rows to CSV, remove empty rows, and download files
append_new_rows(csv_path, url)
