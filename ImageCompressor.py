from PIL import Image
import os
import time
import tkinter as tk
from tkinter import filedialog

print(r"""
       _            _                     _                 _____    _____   ___    _  _   
      | |          | |                   | |               |_   _|  / ____| |__ \  | || |  
      | |  ______  | |_    ___     ___   | |    ___          | |   | |         ) | | || |_ 
  _   | | |______| | __|  / _ \   / _ \  | |   / __|         | |   | |        / /  |__   _|
 | |__| |          | |_  | (_) | | (_) | | |   \__ \  _     _| |_  | |____   / /_     | |  
  \____/            \__|  \___/   \___/  |_|   |___/ ( )   |_____|  \_____| |____|    |_|  
                                                     |/                                    
                                                                                           """)
print ("J-tools Image compressor/converter 2024")
print ("Version 1.2 - supports PNG, JPG/JPEG, ICO")
time.sleep(1)


def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.png;*.ico")])
    if not file_path:
        print("No file selected. Exiting.")
        exit()
    return file_path



def scale_image(image, scale_percentage, image_quality, file_type):
    original_size = image.size
    original_name, _ = os.path.splitext(os.path.basename(image.filename))

    scaled_width = int(original_size[0] * scale_percentage / 100)
    scaled_height = int(original_size[1] * scale_percentage / 100)
    scaled_size = (scaled_width, scaled_height)

    resized_image = image.resize(scaled_size, Image.LANCZOS)

    # Convert to RGB mode only if the file type is PNG
    if file_type.lower() == 'jpg' and resized_image.mode == 'RGBA':
        resized_image = resized_image.convert('RGB')
    
    save_path = os.path.join("C:\\Users\\Master\\Desktop\\Tools\\convertedphotos\\Compressed",
                             f"{original_name}_JTOOL_compressed.{file_type}")

    resized_image.save(save_path, optimize=True, quality=image_quality)



scale_percentage = float(1.0)
compress_quality = 0

image_path = open_file_dialog()
foo = Image.open(image_path)

file_extension = input("File extension: ")


if file_extension.lower() == "jpg" or file_extension.lower() == "jpeg":
    compress_quality = int(input("Image quality: "))
    scale_percentage = float(input("Scale image by what percentage?: "))
else:
    compress_quality = 0
    scale_percentage = float(input("Scale image by what percentage?: "))
try:
    scale_percentage = float(scale_percentage)
except ValueError:
    print("Invalid scale percentage. Using default value (100).")
    scale_percentage = 100.0

scale_image(foo, scale_percentage, compress_quality, file_extension,)
