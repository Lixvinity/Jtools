import os
import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp
#1

# User-defined settings
Custom_Path = False
SAVE_PATH_FOLDER = os.path.expanduser("~\\Downloads")
if Custom_Path:
    SAVE_PATH_FOLDER = r"C:\Users\Master\Desktop\Tools\convertedvideos\Compressed"
os.makedirs(SAVE_PATH_FOLDER, exist_ok=True)  # Ensure the directory exists

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_paths = filedialog.askopenfilenames(title="Select Videos", filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    
    if not file_paths:
        print("No files selected. Exiting.")
        exit()
    
    return file_paths

def compress_video(video_path, compression_factor, fps, quality):
    try:
        video = mp.VideoFileClip(video_path)
    except Exception as e:
        print(f"Error opening video {video_path}: {e}")
        return

    original_name, _ = os.path.splitext(os.path.basename(video.filename))
    save_path = os.path.join(SAVE_PATH_FOLDER, f"{original_name}_compressed.mp4")

    new_width = int(video.size[0] * compression_factor)
    new_height = int(video.size[1] * compression_factor)
    new_size = (new_width, new_height)

    try:
        video_resized = video.resize(new_size)
        video_resized.write_videofile(save_path, codec="libx264", preset=quality, bitrate="500k", audio_codec="aac", fps=fps)
        print(f"Video {video_path} saved to {save_path}")
    except Exception as e:
        print(f"Error saving video {video_path}: {e}")

if __name__ == "__main__":
    print("Video Compressor 2024")
    print("Version 1.0 - supports Bulk compression")
    print(f"Save folder is {SAVE_PATH_FOLDER}")

    video_paths = open_file_dialog()

    while True:
        try:
            fps = int(input("Enter fps: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for fps.")

    while True:
        try:
            compression_factor = float(input("Compression factor (e.g., 0.5 for 50% size reduction): "))
            if compression_factor > 0:
                break
            else:
                print("Compression factor must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the compression factor.")

    print("Enter the speed of your render")
    print("Speed/quality of your render won't affect the compression and won't increase or decrease file size")
    print("4 = fastest speed and lowest quality")
    print("3 = fast speed and lower quality")
    print("2 = medium speed and quality")
    print("1 = slow speed and high quality")
    print("0 = slowest speed and highest quality")

    quality_keys = ("veryfast", "faster", "fast", "medium", "slow", "slower")

    while True:
        try:
            quality = int(input("> Enter render speed (0-4): "))
            if 0 <= quality <= 4:
                quality = quality_keys[quality]
                break
            else:
                print("Please enter a value between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 0 and 4.")

    for path in video_paths:
        compress_video(path, compression_factor, fps, quality)
