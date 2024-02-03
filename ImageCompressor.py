from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
import time

DEFAULT_SAVE_PATH = "C:\\Users\\Master\\Desktop\\Tools\\convertedphotos\\Compressed"
DEFAULT_SCALE_PERCENTAGE = 100

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg;*.png;*.ico;*.jpeg*")])
    if not file_paths:
        print("No files selected. Exiting.")
        exit()
    return file_paths

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
        # Convert RGBA to RGB by removing the alpha channel
        resized_image = resized_image.convert('RGB')


    save_path = os.path.join(DEFAULT_SAVE_PATH, f"{original_name}_JTOOL_compressed.{file_type}")

    resized_image.save(save_path, optimize=True, quality=compress_quality)
    print(f"Image {image_path} saved to {save_path}")

if __name__ == "__main__":
    print(r"""
       _            _                     _                 _____    _____   ___    _  _   
      | |          | |                   | |               |_   _|  / ____| |__ \  | || |  
      | |  ______  | |_    ___     ___   | |    ___          | |   | |         ) | | || |_ 
  _   | | |______| | __|  / _ \   / _ \  | |   / __|         | |   | |        / /  |__   _|
 | |__| |          | |_  | (_) | | (_) | | |   \__ \  _     _| |_  | |____   / /_     | |  
  \____/            \__|  \___/   \___/  |_|   |___/ ( )   |_____|  \_____| |____|    |_|  
                                                     |/                                    
                                                                                           """)
    print("J-tools Image compressor/converter 2024")
    print("Version 2.0 - supports Bulk transform and PNG, JPG/JPEG, ICO")
    time.sleep(1)

    image_paths = open_file_dialog()
    file_extension = input("File extension: ").lower()

    if file_extension not in ['jpg', 'jpeg', 'png', 'ico']:
        print("Unsupported file extension. Exiting.")
        exit()

    compress_quality = 0
    scale_percentage = input(f"Scale image by what percentage? (Default: {DEFAULT_SCALE_PERCENTAGE}): ") or DEFAULT_SCALE_PERCENTAGE

    try:
        scale_percentage = float(scale_percentage)
    except ValueError:
        print("Invalid scale percentage. Using default value (100)")
        scale_percentage = DEFAULT_SCALE_PERCENTAGE

    if file_extension in ["jpg", "jpeg"]:
        compress_quality = int(input("Image quality: "))

    for path in image_paths:
        scale_and_save_image(path, scale_percentage, compress_quality, file_extension)
