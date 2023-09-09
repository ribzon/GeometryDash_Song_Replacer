import os
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import getpass
from PIL import Image, ImageTk
import requests
import tempfile
from io import BytesIO
import shutil  # Import the shutil library for file copying

class FileReplacerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Replacer")
        master.geometry('1000x700')
        master.resizable(False, False)  # Lock the window size

        # Download and set background image
        background_url = "https://cdn.discordapp.com/attachments/1026244641370144899/1149982530192285766/image456.png"
        self.set_background_from_url(background_url)

        self.current_file_path = ""
        self.new_file_path = ""

        # Create buttons and labels with increased size and spacing
        self.current_file_label = tk.Label(master, text="Current File:")
        self.current_file_label.pack(pady=20)

        self.current_file_button = tk.Button(master, text="Select File", command=self.select_current_file, height=3, width=20)
        self.current_file_button.pack(pady=10)

        self.new_file_label = tk.Label(master, text="New File Name:")
        self.new_file_label.pack(pady=20)

        self.new_file_entry = tk.Entry(master, width=50)
        self.new_file_entry.pack(pady=10)

        self.execute_button = tk.Button(master, text="Execute", command=self.execute, height=3, width=20)
        self.execute_button.pack(pady=20)

        # Load and display the Discord icon image
        discord_icon_url = "https://cdn.discordapp.com/attachments/1099374101119905902/1149976767860314132/bmc.png"
        image = self.load_image_from_url(discord_icon_url)

        if image:
            image = ImageTk.PhotoImage(image.resize((100, 100)))  # Resize the image
            self.discord_button = tk.Button(master, image=image, command=self.join_discord_server, bg='black', height=120, width=120)
            self.discord_button.pack(pady=20)
            self.discord_button.image = image  # Keep a reference to prevent image garbage collection

    def load_image_from_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_data = response.content
                return Image.open(BytesIO(image_data))
            else:
                print(f"Failed to load image from URL: {url}")
                return None
        except Exception as e:
            print(f"Failed to load image: {e}")
            return None

    def set_background_from_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_data = response.content
                image_path = os.path.join(tempfile.gettempdir(), 'background_image.jpg')
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_data)
                self.master.configure(bg='black')
                self.background_image = ImageTk.PhotoImage(Image.open(image_path))
                background_label = tk.Label(self.master, image=self.background_image)
                background_label.place(relwidth=1, relheight=1)
            else:
                print(f"Failed to download background image from URL: {url}")
        except Exception as e:
            print(f"Failed to set background image: {e}")
            return None

    def select_current_file(self):
        # Open a file dialog to select the file to replace
        file_path = filedialog.askopenfilename()
        if file_path.endswith('.mp3'):
            self.current_file_path = file_path
            self.current_file_label.config(text="Current File: " + file_path)
        else:
            messagebox.showerror("Error", "The selected file is not an MP3 file.")

    def execute(self):
        # Check that a file has been selected and a new file name has been entered
        if self.current_file_path == "":
            messagebox.showerror("Error", "No file selected")
            return
        if self.new_file_entry.get() == "":
            messagebox.showerror("Error", "No new file name entered")
            return

        # Check that the selected file is an mp3 file
        if not self.current_file_path.endswith('.mp3'):
            messagebox.showerror("Error", "The selected file is not an MP3 file.")
            return

        # Get the new file name and create the new file path
        new_file_name = self.new_file_entry.get()
        if not new_file_name.endswith('.mp3'):
            new_file_name += '.mp3'
        new_file_path = os.path.join(f"C:/Users/{getpass.getuser()}/AppData/Local/GeometryDash", new_file_name)

        # Copy the file instead of replacing it
        try:
            shutil.copy(self.current_file_path, new_file_path)
            messagebox.showinfo("Success", "File copied successfully")
        except Exception as e:
            messagebox.showerror("Error", "Failed to copy file: " + str(e))

    def join_discord_server(self):
        # Open the Discord server in a web browser
        webbrowser.open("https://discord.gg/nfyVQ762XM")

# Create the GUI
root = tk.Tk()
file_replacer_gui = FileReplacerGUI(root)
root.mainloop()
