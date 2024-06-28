import tkinter as tk
import csv
from subprocess import Popen

def run_program(directory):
    # Function to run the program
    Popen(directory, shell=True)

def create_app(csv_file):
    # Create main application window
    root = tk.Tk()
    root.title("Jtools hub")

    # Create a main frame
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)

    # Read CSV file
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        row_num = 0
        for row in reader:
            if row['enabled'].lower() == 'true':
                # Add label with program name
                ToolName = row['name'].replace("_", " ")
                label = tk.Label(main_frame, text=ToolName)
                label.grid(row=row_num, column=0, padx=5, pady=5, sticky="w")

                # Add button to run the program
                button = tk.Button(main_frame, text="Start", command=lambda dir=row['directory']: run_program(dir))
                button.grid(row=row_num, column=1, padx=5, pady=5, sticky="e")

                row_num += 1

    root.mainloop()

# Path to the CSV file
csv_file = 'C:\WINJ\Prerequisites\scripts\packets.csv'

create_app(csv_file)
