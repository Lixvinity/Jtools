from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
import time
from webptools import dwebp

Custom_Path = False
SAVE_PATH_FOLDER = os.path.expanduser("~\\Downloads")
if Custom_Path == True:
    SAVE_PATH_FOLDER = (r"C:\Users\Master\Desktop\Tools\convertedphotos\Compressed")


DEFAULT_SCALE_PERCENTAGE = 100

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg;*.png;*.ico;*.jpeg;*.webp")])
    
    if not file_paths:
        print(Color.RED + "No files selected. Exiting." + Color.END)
        exit()
    
    return file_paths

def convert_webp_to_png(webp_path):
    output_path = os.path.splitext(webp_path)[0] + ".png"
    dwebp(webp_path, output_path)
    return output_path

def scale_and_save_image(image_path, scale_percentage, compress_quality, file_type):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image {image_path}: {e}")
        return

    original_size = image.size
    original_name, _ = os.path.splitext(os.path.basename(image.filename))

    scaled_width = int(original_size[0] * scale_percentage / 100)
    scaled_height = int(original_size[1] * scale_percentage / 100)
    scaled_size = (scaled_width, scaled_height)

    resized_image = image.resize(scaled_size, Image.LANCZOS)

    if file_type.lower() in ['jpg', 'jpeg'] and resized_image.mode == 'RGBA':
        resized_image = resized_image.convert('RGB')

    save_path = os.path.join(SAVE_PATH_FOLDER, f"{original_name}Jtools_compressed.{file_type}")

    resized_image.save(save_path, optimize=True, quality=compress_quality)
    print(f"Image {image_path} saved to {save_path}")

if __name__ == "__main__":
    print(f"""{Color.BOLD}{Color.BLUE}
          _            _                     _                 
         | |          | |                   | |                
         | |  ______  | |_    ___     ___   | |    ___         
     _   | | |______| | __|  / _ \   / _ \  | |   / __| 
    | |__| |          | |_  | (_) | | (_) | | |   \__ \ 
     \____/            \__|  \___/   \___/  |_|   |___/
                                                                
    {Color.END}""")
    print(f"{Color.YELLOW}J-tools Image compressor/converter 2024{Color.END}")
    print(f"{Color.YELLOW}Version 2.1 - supports Bulk transform and PNG, JPG/JPEG, ICO{Color.END}")
    print (f"{Color.YELLOW}Save folder is {SAVE_PATH_FOLDER}{Color.END}")
    time.sleep(1)

    image_paths = open_file_dialog()
    file_extension = input(f"{Color.GREEN}File extension: {Color.END}").lower()

    if file_extension not in ['jpg', 'jpeg', 'png', 'ico', 'webp']:
        print("Unsupported file extension. Exiting.")
        exit()

    compress_quality = 0
    scale_percentage = input(f"{Color.CYAN}Scale image by what percentage? (Default: {DEFAULT_SCALE_PERCENTAGE}): {Color.END}") or DEFAULT_SCALE_PERCENTAGE

    try:
        scale_percentage = float(scale_percentage)
    except ValueError:
        print(f"{Color.RED}Invalid scale percentage. Using default value (100){Color.END}")
        scale_percentage = DEFAULT_SCALE_PERCENTAGE

    if file_extension in ["jpg", "jpeg"]:
        compress_quality = int(input(f"{Color.CYAN}Image quality: {Color.END}"))

    for path in image_paths:
        if file_extension == ".webp":
            path = convert_webp_to_png(path)
            file_extension = "png"
        scale_and_save_image(path, scale_percentage, compress_quality, file_extension)
