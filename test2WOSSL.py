import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp as youtube_dl

def download_video():
    url = url_entry.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'nocheckcertificate': True  # Disable SSL verification
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Downloaded and converted to MP3")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {str(e)}")

def choose_download_folder():
    folder = filedialog.askdirectory()
    if folder:
        os.chdir(folder)
        folder_label.config(text=f"Download folder: {folder}")

# Set up the main application window
root = tk.Tk()
root.title("YouTube to MP3 Downloader")

# URL Input
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=1, column=1, padx=10, pady=20)

# Folder selection
folder_button = tk.Button(root, text="Choose Download Folder", command=choose_download_folder)
folder_button.grid(row=2, column=0, padx=10, pady=10)

folder_label = tk.Label(root, text="No folder selected")
folder_label.grid(row=2, column=1, padx=10, pady=10)

# Start the application
root.mainloop()
