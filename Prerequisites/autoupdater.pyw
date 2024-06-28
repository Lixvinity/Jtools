import csv
import os
import requests
import tempfile

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

def update_tools(csv_path, url):
    """Downloads the latest CSV, updates existing tools and adds new ones based on row content."""
    try:
        # Create a temporary file to store the latest downloaded CSV
        temp_csv_path = tempfile.NamedTemporaryFile(delete=False).name

        # Download the latest CSV from the URL
        download_file(url, temp_csv_path)

        # Read the current CSV
        current_tools = []
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            current_tools = list(reader)

        # Read the latest downloaded CSV
        new_tools = []
        with open(temp_csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            new_tools = list(reader)

        # Convert current tools to a dictionary indexed by (name, link, directory)
        current_tools_dict = {(tool['name'], tool['link'], tool['directory']): tool for tool in current_tools}

        # Update current tools with new or updated entries
        updated_tools = []
        for new_tool in new_tools:
            key = (new_tool['name'], new_tool['link'], new_tool['directory'])
            if key in current_tools_dict:
                # Update existing tool with new values, preserving 'enabled' column
                current_tool = current_tools_dict[key]
                updated_tool = {
                    'name': new_tool['name'],
                    'link': new_tool['link'],
                    'directory': new_tool['directory'],
                    'enabled': current_tool['enabled']  # Preserve existing 'enabled' value
                }
                updated_tools.append(updated_tool)
                # Remove the updated tool from current_tools_dict to track which tools are updated
                del current_tools_dict[key]
            else:
                # Add new tool with default 'enabled' value
                updated_tools.append({
                    'name': new_tool['name'],
                    'link': new_tool['link'],
                    'directory': new_tool['directory'],
                    'enabled': 'False'  # Assuming default state is disabled
                })

        # Append any remaining tools from current_tools_dict (these are unchanged)
        updated_tools.extend(current_tools_dict.values())

        # Write the updated current tools list back to the CSV
        with open(csv_path, mode='w', newline='') as file:
            fieldnames = ['name', 'link', 'directory', 'enabled']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_tools)

        print("Tools updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up temporary file
        if os.path.exists(temp_csv_path):
            os.remove(temp_csv_path)

# Example usage:
csv_path = r"C:\WINJ\Prerequisites\scripts\packets.csv"
url = "https://raw.githubusercontent.com/Lixvinity/Jtools/main/Prerequisites/packets.csv"

download_file("https://github.com/Lixvinity/Jtools/raw/main/Prerequisites/JtoolsHub.py", r"C:\WINJ\Prerequisites\scripts\JtoolsHub.py")

update_tools(csv_path, url)
