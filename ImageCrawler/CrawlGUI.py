import os
import tkinter as tk
from tkinter import filedialog
import google as GG

# Initiate the window
root = tk.Tk()
root.title("Bulk Image Downloader")
root.resizable(0,0)

# Variables
global imageName
global pathName
global imageNum

completeMessage = tk.StringVar()
folder_path = tk.StringVar()

# Commands
def browse_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def download_button():
    imageName = imageNameBox.get()
    pathName = folder_path
    imageNum = imageNumBox.get()
    GG.imageName = imageName
    GG.pathName = pathName.get()
    GG.MAX_IMAGE_NUM = int(imageNum)
    GG.crawl()
    completeMessage.set("Download complete!")
    openButton["state"] = "normal"

def open_button():
    os.startfile(GG.pathName + "/" + GG.imageName)

# Objects
imageLabel = tk.Label(root, text = "Download images of : ")
pathLabel = tk.Label(root, text = "Download images at : ")
pathName = tk.Label(root, textvariable = folder_path)
numberLabel = tk.Label(root, text = "Number of maximum images : ")
completeLabel = tk.Label(root, textvariable = completeMessage, fg = 'green')

imageNameBox = tk.Entry(root)
imageNumBox = tk.Entry(root)
pathBox = tk.Entry(root)

pathButton = tk.Button(text = "Browse", command = browse_button)
downloadButton = tk.Button(text = "Download!", command = download_button)
openButton = tk.Button(text = "Show in Folder", command = open_button)
quitButton = tk.Button(text = "Quit", command = root.quit)

# Alignment
imageLabel.grid(row = 0, column = 1)
imageNameBox.grid(row = 0, column = 3)
pathLabel.grid(row = 2, column = 1)
pathName.grid(row = 2, column = 3)
pathButton.grid(row = 2, column = 4)
numberLabel.grid(row = 4, column = 1)
imageNumBox.grid(row = 4, column = 3)
completeLabel.grid(row = 5, column = 2)
downloadButton.grid(row = 6, column = 1)
openButton.grid(row = 6, column = 2)
quitButton.grid(row = 6, column = 3)

# Initial Setting
openButton["state"] = "disabled"

root.mainloop()
