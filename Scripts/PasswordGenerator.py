import random
import string
import time
import pyautogui
import threading
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import tkinter as tk
import hashlib
import webbrowser

# Initialize window
window = ttk.Window(themename="darkly")
window.title("Password generator")
window.geometry("275x475")
window.resizable(False, False)


# Global variables
mouse_positions = []
collecting = True
mouse_positions_lock = threading.Lock()
toggle_style = ("success-square-toggle")

def collect_mouse_positions(interval=20):
    global collecting
    last_position = pyautogui.position()
    while collecting:
        current_position = pyautogui.position()
        if current_position != last_position:
            with mouse_positions_lock:
                mouse_positions.append(current_position)
            last_position = current_position
        time.sleep(interval / 1000)  # Convert ms to seconds
        seed_length = len(mouse_positions)
        # Update seed bar safely
        window.after(0, lambda: update_seed_bar(seed_length))

def update_seed_bar(seed_length):
    seed_bar.configure(value=seed_length)
    check_button_state()
    update_progress_style(seed_length)

def stop_collection():
    global collecting
    collecting = False

def get_mouse_entropy():
    global mouse_positions
    with mouse_positions_lock:
        entropy_string = ''.join(f'{x}{y}' for x, y in mouse_positions)
    return entropy_string

def build_character_set():
    """Builds the character set based on the toggle states."""
    char_set = ''
    if lower_case_Toggle.instate(['selected']):
        char_set += string.ascii_lowercase
    if Upper_case_Toggle.instate(['selected']):
        char_set += string.ascii_uppercase
    if Number_Toggle.instate(['selected']):
        char_set += string.digits
    if symbol_Toggle.instate(['selected']):
        char_set += string.punctuation
    if extended_ascii_Toggle.instate(['selected']):
        char_set += ''.join(chr(i) for i in range(128, 256))
    
    # Debugging: Print the character set being used
    print(f"Character set: {char_set}")
    
    if not char_set:
        char_set = string.ascii_letters + string.digits + string.punctuation  # Default set
    
    return char_set

def generate_password():
    length = int(password_length_scale.get())
    char_set = build_character_set()  # Use the dynamic character set
    
    # Debugging: Print the length and character set
    print(f"Password length: {length}")
    print(f"Character set used for password generation: {char_set}")

    if mouse_positions:
        entropy_string = get_mouse_entropy()
        # Use the entropy string as a seed for the random number generator
        seed_value = int(hashlib.md5(entropy_string.encode()).hexdigest(), 16)
        random.seed(seed_value)
        
        # Generate the password
        password = ''.join(random.choices(char_set, k=length))
        
        # Clear mouse positions and reset the progress bar
        with mouse_positions_lock:
            mouse_positions.clear()
        update_seed_bar(0)  # Reset the progress bar to 0
    else:
        password = ''.join(random.choices(char_set, k=length))
    
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)

def update_length_label(val):
    length_label.config(text=f"Password Length: {int(float(val))}")

def check_button_state():
    """Enables or disables the generate password button based on the seed bar's value."""
    if seed_bar['value'] >= 350:  # 35% of 1000
        generate_password_button.config(state=tk.NORMAL)
    else:
        generate_password_button.config(state=tk.DISABLED)

def update_progress_style(seed_length):
    """Update the progress bar style based on the current seed length."""
    max_value = seed_bar['maximum']
    percentage = (seed_length / max_value) * 100
    
    if percentage >= 75:
        style = "success"
    elif percentage >= 35:
        style = "warning"
    else:
        style = "danger"
    
    seed_bar.config(bootstyle=style)

def load_image_into_ttk(parent, image_path, text="", padding=10, resize=None):
    frame = ttk.Frame(parent, padding=padding)
    
    try:
        # Load and resize image
        image = Image.open(image_path)
        if resize:
            image = image.resize(resize, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        photo = None  # Fallback to no image
    
    if photo:
        # Create image label
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=0, padx=padding, pady=padding)
    
    # Add text label if provided
    if text:
        text_label = ttk.Label(frame, text=text)
        text_label.grid(row=1, column=0, padx=padding, pady=padding)
    
    return frame

# GUI setup
password_options = ttk.Frame(master=window)
password_options.pack(fill="both", expand=True)

Title = ttk.Label(password_options, text="Password Generator")
Title.grid(row=0, column=0, padx=10, pady=10, sticky="n")

options = ttk.Frame(password_options)
options.grid(row=1, column=0, sticky="sew", padx=10, pady=10)

LBG = ttk.Frame(password_options)
LBG.grid(row=2, column=0, sticky="sew", padx=10, pady=10)

password_options.rowconfigure(0, weight=0)
password_options.rowconfigure(1, weight=1)

# Checkbuttons and labels
lower_case_label = ttk.Label(options, text="a-z")
lower_case_label.grid(row=0, column=0, sticky="w", pady=1)

lower_case_Toggle = ttk.Checkbutton(options, bootstyle=toggle_style)
lower_case_Toggle.grid(row=0, column=1, sticky="e", pady=1)

Upper_case_label = ttk.Label(options, text="A-Z")
Upper_case_label.grid(row=1, column=0, sticky="w", pady=1)

Upper_case_Toggle = ttk.Checkbutton(options, bootstyle=toggle_style)
Upper_case_Toggle.grid(row=1, column=1, sticky="e", pady=1)

Number_label = ttk.Label(options, text="0-9")
Number_label.grid(row=2, column=0, sticky="w", pady=1)

Number_Toggle = ttk.Checkbutton(options, bootstyle=toggle_style)
Number_Toggle.grid(row=2, column=1, sticky="e", pady=1)

symbol_label = ttk.Label(options, text="!@#$%...")
symbol_label.grid(row=3, column=0, sticky="w", pady=1)

symbol_Toggle = ttk.Checkbutton(options, bootstyle=toggle_style)
symbol_Toggle.grid(row=3, column=1, sticky="e", pady=1)

extended_ascii_label = ttk.Label(options, text="Extended ASCII")
extended_ascii_label.grid(row=4, column=0, sticky="w", pady=1)

extended_ascii_Toggle = ttk.Checkbutton(options, bootstyle=toggle_style)
extended_ascii_Toggle.grid(row=4, column=1, sticky="e", pady=1)

options.columnconfigure(0, weight=1)
options.columnconfigure(1, weight=1)

length_label = ttk.Label(LBG, text="Password Length: 16")
length_label.grid(row=0, column=0, columnspan=3, sticky="ew")

password_length_scale = ttk.Scale(LBG, from_=8, to_=128, command=update_length_label)
password_length_scale.grid(row=1, column=0, columnspan=3, sticky="ew", pady=4)
password_length_scale.set(16)

seed_bar = ttk.Progressbar(master=LBG, maximum=1000, bootstyle="danger")
seed_bar.grid(row=2, column=0, columnspan=3, sticky="ew")

generate_password_button = ttk.Button(master=LBG, text="Generate Password", command=generate_password, state=tk.DISABLED)
generate_password_button.grid(row=3, column=0, columnspan=2, sticky="ew", pady="5")

keypass_image_location = Image.open(r"C:\WINJ\Prerequisites\Icons\Keepassxc_white.png")
resized_keypass_image = keypass_image_location.resize((21, 21), Image.LANCZOS)
keypass_icon = ImageTk.PhotoImage(resized_keypass_image)

keepassxc_button = ttk.Button(master=LBG, image=keypass_icon, width=20, command=lambda: webbrowser.open(r"https://keepassxc.org/"))
keepassxc_button.grid(row=3, column=2, sticky="ew", padx="2", pady="5")

LBG.columnconfigure(0, weight=1)
LBG.columnconfigure(1, weight=1)
LBG.columnconfigure(2, weight=1)

# Add a text widget to display the generated password
password_display = tk.Text(master=LBG, height=5, width=30)
password_display.grid(row=4, column=0, columnspan=3, pady=10)

# Start collecting mouse positions in a separate thread
thread = threading.Thread(target=collect_mouse_positions)
thread.start()

# Ensure the GUI can be closed properly
window.protocol("WM_DELETE_WINDOW", lambda: [stop_collection(), window.destroy()])

# Check button state initially
check_button_state()

window.mainloop()
