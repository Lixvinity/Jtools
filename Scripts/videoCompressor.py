import os
import cv2
import tempfile
from PIL import Image, ImageTk
import customtkinter as tk
from customtkinter import filedialog
import moviepy.editor as mp
import threading

# Window setup
window = tk.CTk()
window.title("Jtool's Video Compressor")
window.geometry("800x600")
window.resizable(False, False)
window.iconbitmap(r"C:\WINJ\Prerequisites\Icons\VideoJtools_compressed.ico")
# Global variables
video_paths = []
video_number = 0
fps_counters_str = ["10 FPS", "20 FPS", "24 FPS", "25 FPS", "30 FPS", "48 FPS", "50 FPS", "60 FPS"]
audio_kbps = ['8 kbps', '16 kbps', '24 kbps', '32 kbps', '40 kbps', '48 kbps', '56 kbps', '64 kbps',
              '80 kbps', '96 kbps', '112 kbps', '128 kbps', '144 kbps', '160 kbps', '192 kbps',
              '224 kbps', '256 kbps', '320 kbps']
video_kbps = ['32 kbps', '40 kbps', '48 kbps', '56 kbps', '64 kbps', '80 kbps', '96 kbps', '112 kbps',
              '128 kbps', '144 kbps', '160 kbps', '192 kbps', '224 kbps', '256 kbps', '320 kbps', '448 kbps', '500 kbps']
SAVE_PATH_FOLDER = os.path.expanduser("~\\Downloads")

# Function to compress video
def compress_video(video_path, compression_factor, fps, audio_bitrate, video_bitrate):
    try:
        video = mp.VideoFileClip(video_path)
    except Exception as e:
        print(f"Error opening video {video_path}: {e}")
        return

    original_name, _ = os.path.splitext(os.path.basename(video_path))
    save_path = os.path.join(SAVE_PATH_FOLDER, f"{original_name}_compressed.mp4")

    new_width = int(video.size[0] * compression_factor)
    new_height = int(video.size[1] * compression_factor)
    new_size = (new_width, new_height)

    try:
        video_resized = video.resize(new_size)
        video_resized.write_videofile(
            save_path,
            codec="libx264",
            preset="slow",
            fps=fps,
            audio_codec="aac",
            audio_bitrate=f"{audio_bitrate}k",
            bitrate=f"{video_bitrate}k"
        )
        print(f"Video {video_path} saved to {save_path}")
    except Exception as e:
        print(f"Error saving video {video_path}: {e}")

# Function to get video thumbnail
def get_video_thumbnail(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error: Could not open video {video_path}")
            return None

        ret, frame = cap.read()
        if ret:
            height, width, _ = frame.shape
            input_aspect_ratio = width / height
            target_aspect_ratio = 16 / 9

            if input_aspect_ratio < target_aspect_ratio:
                new_height = width / target_aspect_ratio
                crop_top = int((height - new_height) / 2)
                crop_bottom = int(height - (height - new_height) / 2)
                frame_cropped = frame[crop_top:crop_bottom, :, :]
            else:
                new_width = height * target_aspect_ratio
                crop_left = int((width - new_width) / 2)
                crop_right = int(width - (width - new_width) / 2)
                frame_cropped = frame[:, crop_left:crop_right, :]

            frame_resized = cv2.resize(frame_cropped, (200, 112))

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
            temp_file.close()
            temp_file_path = temp_file.name

            cv2.imwrite(temp_file_path, frame_resized)
            return temp_file_path
        else:
            print(f"Error: Could not read frame from video {video_path}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to create thumbnails
def makethumbnails():
    global video_paths
    for widget in VideoList.winfo_children():
        widget.destroy()

    list_index = 0
    for video_path in video_paths:
        thumbnail_path = get_video_thumbnail(video_path)
        if thumbnail_path:
            thumbnail_image = Image.open(thumbnail_path)
            thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)

            video_thumbnail = tk.CTkLabel(VideoList, image=thumbnail_photo, text=" ")
            video_thumbnail.image = thumbnail_photo
            video_thumbnail.grid(row=list_index, column=0, padx=10, pady=10)
            list_index += 1

# Function to open file dialog
def open_file_dialog():
    global video_paths
    global video_number
    file_paths = filedialog.askopenfilenames(
        title="Select Videos",
        filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    if not file_paths:
        print("No files selected. Exiting.")
        return
    video_Plural = "videos" if len(file_paths) > 1 else "video"
    video_paths = file_paths
    video_number = len(video_paths)
    Loaded_video_label.configure(text=f"{video_number} {video_Plural} loaded")
    makethumbnails()

# Function to list compress
def list_compress(compression_factor, fps_index, audio_index, video_index):
    global video_paths
    fps = parse_fps(fps_counters_str[fps_index])
    audio_bitrate = parse_bitrate(audio_kbps[audio_index])
    video_bitrate = parse_bitrate(video_kbps[video_index])
    for video in video_paths:
        threading.Thread(target=compress_video, args=(video, compression_factor, fps, audio_bitrate, video_bitrate)).start()

# Function to parse fps
def parse_fps(fps_str):
    return int(fps_str.split()[0])

# Function to parse bitrate
def parse_bitrate(bitrate_str):
    return int(bitrate_str.split()[0])

# UI setup
frame = tk.CTkFrame(window)
frame.pack(side='left', fill='y')

compress_details = tk.CTkScrollableFrame(window, height=600)
compress_details.pack(anchor="e", fill='both')

video_label_info = tk.CTkLabel(compress_details, text="Video")
video_label_info.pack()

fps_quality = tk.CTkFrame(compress_details)
fps_quality.pack()

Open_files_button = tk.CTkButton(frame, text="Open Files", command=open_file_dialog)
Open_files_button.pack(pady=5)

Loaded_video_label = tk.CTkLabel(frame, text=f"{video_number} videos loaded")
Loaded_video_label.pack()

VideoList = tk.CTkScrollableFrame(frame)
VideoList.pack(side='left', fill='y')

compress_label = tk.CTkLabel(fps_quality, text="Quality")
compress_label.grid(row=0, column=0, columnspan=2)

bitrateVideo_label = tk.CTkLabel(fps_quality, text="Bitrate")
bitrateVideo_label.grid(row=0, column=3)

fps_label = tk.CTkLabel(fps_quality, text="FPS")
fps_label.grid(row=0, column=2)

Video_compress_slider = tk.CTkSlider(fps_quality, orientation="horizontal", number_of_steps=20, from_=0.01, to=1)
Video_compress_slider.grid(row=1, column=0, columnspan=2, padx=3)

fps_input = tk.CTkOptionMenu(fps_quality, values=fps_counters_str, variable=tk.StringVar(value="30 FPS"))
fps_input.grid(row=1, column=2, padx=3)

Video_Bitrate_input = tk.CTkOptionMenu(fps_quality, values=video_kbps, variable=tk.StringVar(value="500 kbps"))
Video_Bitrate_input.grid(row=1, column=3, padx=3)

audio_compress = tk.CTkFrame(compress_details)
audio_compress.pack()

audio_label = tk.CTkLabel(audio_compress, text="Audio")
audio_label.grid(row=0, column=0, columnspan=2)

audio_quality_selector = tk.CTkOptionMenu(audio_compress, values=audio_kbps, variable=tk.StringVar(value="128 kbps"))
audio_quality_selector.grid(row=1, column=0, padx=3)

compress_value = Video_compress_slider.get()

# Function for compress button callback
def compress_button_callback():
    compression_factor = Video_compress_slider.get()  # Get compression factor from slider
    fps_index = fps_counters_str.index(fps_input.get())  # Get FPS index from dropdown
    audio_index = audio_kbps.index(audio_quality_selector.get())  # Get audio bitrate index from dropdown
    video_index = video_kbps.index(Video_Bitrate_input.get())  # Get video bitrate index from dropdown
    list_compress(compression_factor=compression_factor, fps_index=fps_index, audio_index=audio_index, video_index=video_index)

compress_button = tk.CTkButton(compress_details, text="Compress", command=compress_button_callback)
compress_button.pack(anchor="s", pady=20)

window.mainloop()
