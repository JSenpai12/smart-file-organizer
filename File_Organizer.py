#!/user/bin/env python3

import os
import shutil
import multiprocessing
import time 

class FileOrganizer:
    def __init__(self, source_folder):
        self.source_folder = source_folder
        self.parent, self.folder = os.path.split(self.source_folder)
    
    def start_time(self):
        start = time.time()
        return start
    
    def end_time(self):
        end = time.time()
        return end
    
    #* List files
    def get_files(self):
        return os.listdir(self.source_folder)
    
    def get_destination_folder(self, filename):

        # * Link to Pictures Folder
        if filename.endswith((".jpg", ".png", ".jpeg")):
            return f"{self.parent}/Pictures"

        # * Link to Documents Folder
        elif filename.endswith((".pdf", ".docx", ".txt", ".pptx")):
            return f"{self.parent}/Documents"
        
        # * Link to Music Folder
        elif filename.endswith((".mp3", ".wav")):
            return f"{self.parent}/Music"
        
        # * Link to Videos Folder
        elif filename.endswith((".mp4", ".mov", ".avi")):
            return f"{self.parent}/Videos"
        
        # * Others are stayed in downloads
        else:
            return f"{self.parent}/Downloads"
    
    # * If folder does not exist, Create one
    def ensure_folder_exists(self, folder_name):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
    
    def move_file(self, filename):
        source = os.path.join(self.source_folder, filename) # something like: "/home/user/source/file.txt"

        if not os.path.isfile(source): 
            return # skip folders or invalid items
        
        folder = self.get_destination_folder(filename)
        self.ensure_folder_exists(filename)

        destination = os.path.join(folder, filename)
        shutil.move(source, destination)
    
    def organize(self):
        for file in self.get_files():
            p = multiprocessing.Process(target=self.get_files)
            p.start()
            p.join()
            print(f"Moving: {file}")
            self.move_file(file)
    
    def delete_empty_folders(self):
        current_folder = os.getcwd()
        for item in os.listdir(current_folder):
            full_path = os.path.join(current_folder, item)

            if os.path.isdir(full_path) and not os.listdir(full_path):
                os.rmdir(full_path)


# organizer = FileOrganizer("/home/jhon-mekier/Downloads")
# organizer.organize()


# NOTE 
# //* os: file/folder discovery, checks, folder creation, safe paths
# //* shutil: move/copy/delete files and folders

import tkinter as tk
from tkinter import ttk


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.bg_color = "#ffffff"
        self.header_bg = "#f5f5f5"
        self.button_bg = "#262626"
        self.button_fg = "#ffffff"
        self.button_hover = "#404040"

        self.root.configure(bg=self.bg_color)

        self.current_frame = None

        self.create_widgets()

    # ---------------- MAIN SCREEN ----------------
    def create_widgets(self):

        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(fill="both", expand=True, padx=32, pady=20)

        title = tk.Label(
            self.content_frame,
            text="Paste Downloads folder path here:",
            font=("Arial", 14),
            bg=self.bg_color
        )
        title.pack(pady=10)

        self.path_entry = tk.Entry(self.content_frame, font=("Arial", 10))
        self.path_entry.pack(fill="x", pady=10)
        self.path_entry.insert(0, self.load_last_path())

        self.organize_btn = tk.Button(
            self.content_frame,
            text="Organize",
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground=self.button_hover,
            command=self.organizeFiles
        )
        self.organize_btn.pack(pady=10)

        self.status_label = tk.Label(
            self.content_frame,
            text="",
            bg=self.bg_color,
            fg="gray"
        )
        self.status_label.pack()

    # ---------------- SWITCH FRAME ----------------
    def switch_to_success(self):

        # destroy old frame
        if self.content_frame:
            self.content_frame.destroy()

        self.success_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.success_frame.pack(fill="both", expand=True)

        tk.Label(
            self.success_frame,
            text="✔",
            font=("Arial", 40),
            fg="green",
            bg="#f4f4f4"
        ).pack(pady=10)

        tk.Label(
            self.success_frame,
            text="Files are now moved!",
            font=("Arial", 16, "bold"),
            bg="#f4f4f4"
        ).pack(pady=5)

        tk.Label(
            self.success_frame,
            text="Your files were successfully organized.",
            bg="#f4f4f4",
            fg="gray"
        ).pack(pady=5)

        ttk.Button(
            self.success_frame,
            text="OK",
            command=self.root.destroy
        ).pack(pady=15)
    
    # ---------------- SAVE LAST PATH  -----------
    def save_last_path(self, path):
        with open("last_path.txt", "w") as f:
            f.write(path)
    
    # ---------------- LOAD LAST PATH --------------
    def load_last_path(self):
        try:
            with open("last_path.txt", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return ""

    # ---------------- ACTION ----------------
    def organizeFiles(self):
        source_folder = self.path_entry.get()

        self.save_last_path(source_folder)

        if not source_folder:
            self.status_label.config(text="Please enter a path")
            return

        self.status_label.config(text="Organizing...")

        # simulate delay (optional)
        self.root.after(500, self.switch_to_success)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()