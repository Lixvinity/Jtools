import os
import customtkinter as ctk
from PIL import Image, ImageTk
import csv
from subprocess import Popen
import webbrowser

image_folders = r"C:\WINJ\Prerequisites"
settings_Icon = "SettingsIcon.png"
news_icon = "NewsIcon.png"
feed_icon = "Feed.png"

class App:
    def __init__(self, root):
        self.root = root
        self.settings_window = None  # Variable to track the settings window
        self.News_window = None

        # Create the main window
        root.title("Jtool's hub")
        root.geometry("600x400")
        root.resizable(False, False)

        # Load the images using PIL and convert them to Tkinter-compatible images
        self.settings_image = self.load_image(settings_Icon, (42, 42))
        self.news_image = self.load_image(news_icon, (42, 42))
        self.feed_image = self.load_image(feed_icon, (42, 42))

        # Create a frame for the title
        title_frame = ctk.CTkFrame(root)
        title_frame.pack(fill='x', padx=20, pady=20)

        # Configure the grid to push the buttons to the right
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=0)
        title_frame.grid_columnconfigure(2, weight=0)

        # Add a welcome label to the frame
        welcome_label = ctk.CTkLabel(title_frame, text="Welcome to Jtool's!", font=("Helvetica", 40))
        welcome_label.grid(row=0, column=0, sticky="w", padx=2)

        news_button = ctk.CTkButton(title_frame, image=self.news_image, text="", width=50, height=50, command=self.open_news)
        news_button.grid(row=0, column=1, sticky="e", padx=2)

        website_button = ctk.CTkButton(title_frame, image=self.feed_image, text="", width=50, height=50, command=lambda: (webbrowser.open("https://lixxie.xyz")))
        website_button.grid(row=0, column=2, sticky="e", padx=2)

        # Add a settings button with the image, setting the button dimensions
        settings_button = ctk.CTkButton(title_frame, image=self.settings_image, text="", width=50, height=50, command=self.open_settings)
        settings_button.grid(row=0, column=3, sticky="e", padx=2)

        # Create a frame for the packets
        self.packet_frame = ctk.CTkScrollableFrame(root)
        self.packet_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

        # Load the scripts from the CSV file
        self.load_scripts()

    def load_image(self, icon_name, size):
        image_path = os.path.join(image_folders, icon_name)
        image = Image.open(image_path)
        image = image.resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def run_program(self, directory):
        print(f"Running program: {directory}")
        Popen(directory, shell=True)

    def load_scripts(self):
        # Clear existing widgets in the packet_frame
        for widget in self.packet_frame.winfo_children():
            widget.destroy()

        # Load the scripts from the CSV file
        with open(r'C:\WINJ\Prerequisites\scripts\packets.csv', 'r') as packet_file:
            packet_reader = csv.reader(packet_file)
            packets = 0
            next(packet_reader)  # Skip the header
            for line in packet_reader:
                if not line or all(cell.strip() == "" for cell in line):
                    continue  # Skip empty lines
                script_name = line[0]
                script_path = line[2]
                display_script = line[3].strip().lower() == "true"
                
                if display_script:
                    packet_text = ctk.CTkLabel(self.packet_frame, text=script_name.replace("_", " "))
                    packet_text.grid(row=packets, column=0, padx=5, pady=2.5, sticky="w")

                    # Check if the script file exists
                    if os.path.exists(script_path):
                        packet_button = ctk.CTkButton(self.packet_frame, text="Open", command=lambda script=script_path: self.run_program(script))
                    else:
                        packet_button = ctk.CTkButton(self.packet_frame, text="Open", state="disabled")

                    packet_button.grid(row=packets, column=1, padx=5, pady=2.5, sticky="e")
                    self.packet_frame.grid_columnconfigure(0, weight=1)
                    packets += 1

    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = ctk.CTkToplevel(self.root)
            self.settings_window.title("Jtool's settings")
            self.settings_window.geometry("300x400")
            self.settings_window.resizable(False, False)

            def refresh_list():
                # Clear existing widgets
                for widget in packet_choices.winfo_children():
                    widget.destroy()

                self.switches = {}  # Dictionary to store switch state variables
                with open(r'C:\WINJ\Prerequisites\scripts\packets.csv', 'r') as scripts_file:
                    scripts_reader = csv.reader(scripts_file)
                    scripts = 0
                    next(scripts_reader)  # Skip header
                    for line in scripts_reader:
                        if not line or all(cell.strip() == "" for cell in line):
                            continue  # Skip empty lines

                        # Create and place label
                        script_label = ctk.CTkLabel(packet_choices, text=line[0].replace("_", " "))
                        script_label.grid(row=scripts, column=0, padx=5, pady=2.5, sticky="w")

                        # Create and place switch
                        switch_state = ctk.BooleanVar(value=line[3].strip().lower() == "true")
                        script_switch = ctk.CTkSwitch(packet_choices, text="", variable=switch_state)
                        script_switch.grid(row=scripts, column=1, padx=5, pady=2.5, sticky="e")

                        # Store the variable for later use
                        self.switches[line[0]] = switch_state

                        scripts += 1

            def save_changes():
                # Save the state of each switch
                with open(r'C:\WINJ\Prerequisites\scripts\packets.csv', 'r') as scripts_file:
                    lines = scripts_file.readlines()

                with open(r'C:\WINJ\Prerequisites\scripts\packets.csv', 'w') as scripts_file:
                    header = lines[0]
                    scripts_file.write(header)  # Write the header
                    for line in lines[1:]:
                        columns = line.strip().split(',')
                        script_name = columns[0]
                        if script_name in self.switches:
                            # Update the switch state in the CSV
                            columns[3] = "true" if self.switches[script_name].get() else "false"
                        scripts_file.write(','.join(columns) + '\n')

                # Reload scripts after saving changes
                self.load_scripts()

            settings_label = ctk.CTkLabel(self.settings_window, text="Settings")
            settings_label.pack()

            settings_frame = ctk.CTkFrame(self.settings_window)
            settings_frame.pack()

            packet_choices = ctk.CTkScrollableFrame(self.settings_window)
            packet_choices.pack(fill="both", expand=True)

            save_button = ctk.CTkButton(self.settings_window, text="Save Changes", command=save_changes)
            save_button.pack(pady=10)

            def run_script_reload_pack(path):
                self.run_program(path)
                refresh_list()

            update_script_button = ctk.CTkButton(settings_frame, text="Update packet/scripts", 
                                                 command=lambda: run_script_reload_pack(r"C:\WINJ\Prerequisites\scripts\autoupdater.pyw"))
            update_script_button.grid(row=0, column=0)

            update_library_button = ctk.CTkButton(settings_frame, text="Update libraries", 
                                                  command=lambda: run_script_reload_pack(r"C:\WINJ\Prerequisites\scripts\lib.py"))
            update_library_button.grid(row=1, column=0)

            refresh_list()

            # Bind the close event to a handler
            self.settings_window.protocol("WM_DELETE_WINDOW", self.on_settings_close)
        else:
            self.settings_window.lift()  # Bring the existing window to the front

    def on_settings_close(self):
        # Handle the settings window close event
        self.settings_window.destroy()
        self.settings_window = None


    def open_news(self):
        self.News_window = ctk.CTkToplevel(self.root)
        self.News_window.title("Jtool's News")
        self.News_window.geometry("500x300")
        self.News_window.resizable(False, False)

        notice = ctk.CTkLabel(self.News_window, text="coming soon").pack()





if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue")

    root = ctk.CTk()
    app = App(root)
    root.mainloop()
