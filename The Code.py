import os
import tkinter as tk
from tkinter import filedialog
import webbrowser
import getpass

class FileReplacerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Replacer")
        master.configure(bg='black')
        master.geometry('400x250')

        self.current_file_path = ""
        self.new_file_path = ""

        # Create buttons and labels
        self.current_file_label = tk.Label(master, text="Current File:", fg='white', bg='black')
        self.current_file_label.pack()

        self.current_file_button = tk.Button(master, text="Select File", command=self.select_current_file, bg='gray', fg='white')
        self.current_file_button.pack()

        self.new_file_label = tk.Label(master, text="New File Name:", fg='white', bg='black')
        self.new_file_label.pack()

        self.new_file_entry = tk.Entry(master, bg='gray', fg='white')
        self.new_file_entry.pack()

        self.execute_button = tk.Button(master, text="Execute", command=self.execute, bg='gray', fg='white')
        self.execute_button.pack()

        self.discord_button = tk.Button(master, text="Join Discord Server", command=self.join_discord_server, bg='gray', fg='white')
        self.discord_button.pack()

    def select_current_file(self):
        # Open a file dialog to select the file to replace
        file_path = filedialog.askopenfilename()
        if file_path.endswith('.mp3'):
            self.current_file_path = file_path
            self.current_file_label.config(text="Current File: " + file_path)
        else:
            tk.messagebox.showerror("Error", "The selected file is not an MP3 file.")

    def execute(self):
        # Check that a file has been selected and a new file name has been entered
        if self.current_file_path == "":
            tk.messagebox.showerror("Error", "No file selected")
            return
        if self.new_file_entry.get() == "":
            tk.messagebox.showerror("Error", "No new file name entered")
            return

        # Check that the selected file is an mp3 file
        if not self.current_file_path.endswith('.mp3'):
            tk.messagebox.showerror("Error", "The selected file is not an MP3 file.")
            return

        # Get the new file name and create the new file path
        new_file_name = self.new_file_entry.get()
        if not new_file_name.endswith('.mp3'):
            new_file_name += '.mp3'
        new_file_path = os.path.join(f"C:/Users/{getpass.getuser()}/AppData/Local/GeometryDash", new_file_name)

        # Replace the file
        try:
            os.replace(self.current_file_path, new_file_path)
            tk.messagebox.showinfo("Success", "File replaced successfully")
        except Exception as e:
            tk.messagebox.showerror("Error", "Failed to replace file: " + str(e))

    def join_discord_server(self):
        # Open the Discord server in a web browser
        webbrowser.open("https://discord.gg/example")

# Create the GUI
root = tk.Tk()
file_replacer_gui = FileReplacerGUI(root)
root.mainloop()
