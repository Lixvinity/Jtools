import os

def create_folder(directory, folder_name):
    # Combine the directory and folder name to form the full path
    folder_path = os.path.join(directory, folder_name)
    
    try:
        # Create the folder
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")

# Example usage:
# Specify the directories and folder names
directories = [r"C:\\", r"C:\\WINJ", r"C:\\WINJ", r"C:\\WINJ\\Prerequisites"]
folder_names = ["WINJ", "Scripts", "Prerequisites", "scripts"]

# Create the folders
for directory, folder_name in zip(directories, folder_names):
    create_folder(directory, folder_name)
