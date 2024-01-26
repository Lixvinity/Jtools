#       _            _                     _                 _____    _____   ___    _  _   
#      | |          | |                   | |               |_   _|  / ____| |__ \  | || |  
#      | |  ______  | |_    ___     ___   | |    ___          | |   | |         ) | | || |_ 
#  _   | | |______| | __|  / _ \   / _ \  | |   / __|         | |   | |        / /  |__   _|
# | |__| |          | |_  | (_) | | (_) | | |   \__ \  _     _| |_  | |____   / /_     | |  
#  \____/            \__|  \___/   \___/  |_|   |___/ ( )   |_____|  \_____| |____|    |_|  
#                                                     |/                                                                                                                             
from PIL import Image
import os
import time

print(r"""\ 
       _            _                     _                 _____    _____   ___    _  _   
      | |          | |                   | |               |_   _|  / ____| |__ \  | || |  
      | |  ______  | |_    ___     ___   | |    ___          | |   | |         ) | | || |_ 
  _   | | |______| | __|  / _ \   / _ \  | |   / __|         | |   | |        / /  |__   _|
 | |__| |          | |_  | (_) | | (_) | | |   \__ \  _     _| |_  | |____   / /_     | |  
  \____/            \__|  \___/   \___/  |_|   |___/ ( )   |_____|  \_____| |____|    |_|  
                                                     |/                                    
                                                                                           """)
time.sleep(1)


def Scale_Image(image, scale_percentage, imagequality, filetype):
    original_size = image.size
    original_name, _ = os.path.splitext(os.path.basename(image.filename))
    print(f"Original Size: {original_size}")
    
    # Calculate scaled dimensions based on percentage
    scaled_width = int(original_size[0] * scale_percentage / 100)
    scaled_height = int(original_size[1] * scale_percentage / 100)
    
    scaled_size = (scaled_width, scaled_height)
    print(f"Scaled image size: {scaled_size}")
    
    resized_image = image.resize(scaled_size, Image.LANCZOS)
    resized_image.save(f"C:\\Users\\Master\\Desktop\\Tools\\convertedphotos\\Compressed\\{original_name}_JTOOL_compressed.{filetype}",optimize=True,quality=imagequality)
scale_percentage = float(1.0)
Compress_Quality = 0




image_path = input("Image path: ")
foo = Image.open(image_path)

file_extention = input("file extention: ") 

if file_extention.lower() == "jpg":
    Compress_Quality = input("Image quality: ")
    Compress_Quality = int(Compress_Quality)

scale_percentage = input("Scale image by what percentage?: ")
scale_percentage = float(scale_percentage)

# Call the Scale_Image function with the image and scale percentage
Scale_Image(foo, scale_percentage, Compress_Quality, file_extention)
