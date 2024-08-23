import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import json
import hashlib
import os
import datetime

TITLE_TEXT = "Blog Post Maker"
TAGS = ("Python", "Web", "Artificial Intelligence", "Security", "Censorship", 
        "Open Source", "Privacy", "Big Tech", "Unreal Engine", "Programming")

# Initialize the main window
window = ttk.Window(themename="cyborg")
window.geometry("375x775")
window.title(TITLE_TEXT)

# Title Label
title_label = ttk.Label(window, text=TITLE_TEXT, font=("Helvetica", 20))
title_label.pack(pady=10)

# LabelFrame for title input
post_title_input = ttk.LabelFrame(window, text="Title")
post_title_input.pack(padx=10, pady=10, fill="x")

# Entry widget for title
title_entry = ttk.Entry(post_title_input)
title_entry.pack(padx=10, pady=10, fill="x")

# Create a Frame for the tags with a horizontal scrollbar
scroll_frame = ttk.Frame(window)
scroll_frame.pack(padx=10, pady=10, fill="x")

# Create a Canvas within the Frame
canvas = tk.Canvas(scroll_frame, height=50)
canvas.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the canvas
h_scrollbar = ttk.Scrollbar(scroll_frame, orient="horizontal", command=canvas.xview)
h_scrollbar.pack(side="bottom", fill="x")
canvas.configure(xscrollcommand=h_scrollbar.set)

# Create a Frame within the canvas to hold the checkboxes
checkbox_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")

# Add checkboxes to the frame within the canvas
tag_vars = {}
for tag in TAGS:
    tag_var = tk.BooleanVar()
    tag_checkbox = ttk.Checkbutton(
        checkbox_frame,
        text=tag,
        variable=tag_var,
        bootstyle="outline-toolbutton"
    )
    tag_checkbox.pack(side="left", padx=2)
    tag_vars[tag] = tag_var

# Update the scroll region after all widgets are added
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

checkbox_frame.bind("<Configure>", update_scroll_region)

# Remove Date Entry as it's not needed
# Date Entry removed

# Details Frame
details_frame = ttk.Frame(window)
details_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Content LabelFrame within the details frame
post_content_input = ttk.LabelFrame(details_frame, text="Content")
post_content_input.grid(column=0, row=0, columnspan=2, rowspan=2, sticky="nsew", padx=5, pady=5)

# Configure columns and rows to expand
details_frame.columnconfigure(0, weight=1)
details_frame.columnconfigure(1, weight=1)
details_frame.rowconfigure(0, weight=1)
details_frame.rowconfigure(1, weight=1)
details_frame.rowconfigure(2, weight=1)

# Text fields for Icon and Banner URLs
icon_url_label = ttk.Label(details_frame, text="Icon URL:")
icon_url_label.grid(column=0, row=2, sticky="e", padx=5, pady=5)

icon_url_entry = ttk.Entry(details_frame)
icon_url_entry.grid(column=1, row=2, sticky="w", padx=5, pady=5)

banner_url_label = ttk.Label(details_frame, text="Banner URL:")
banner_url_label.grid(column=0, row=3, sticky="e", padx=5, pady=5)

banner_url_entry = ttk.Entry(details_frame)
banner_url_entry.grid(column=1, row=3, sticky="w", padx=5, pady=5)

# A Text widget for content input
content_text = tk.Text(post_content_input, wrap="word", height=10)
content_text.pack(fill="both", expand=True, padx=5, pady=5)

# Function to save the blog post
def save_post():
    # Collect data from input fields
    title = title_entry.get()
    
    # Get the current date from the system clock
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    
    content = content_text.get("1.0", tk.END).strip()
    icon_url = icon_url_entry.get()
    banner_url = banner_url_entry.get()
    
    # Get selected tags
    tags_selected = [tag for tag, var in tag_vars.items() if var.get()]
    
    # Create the JSON data
    post_data = {
        "bannerImage": banner_url,
        "icon": icon_url,
        "title": title,
        "date": date,
        "content": f"<p>content</p>",
        "tags": tags_selected
    }
    
    # Convert JSON data to string
    json_data = json.dumps(post_data, indent=4)
    
    # Compute hash of the JSON data
    json_hash = hashlib.sha256(json_data.encode()).hexdigest()
    
    # Define the file path in the Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_folder, f"{json_hash}.json")
    
    # Save the JSON data to the file
    try:
        with open(file_path, 'w') as file:
            file.write(json_data)
        messagebox.showinfo("Save Post", f"Post saved successfully to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save post: {e}")

# Save button
create_button = ttk.Button(window, text="Save Post", command=save_post)
create_button.pack(pady=10)

# Run the application
window.mainloop()
