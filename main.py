from PIL import Image
import os
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

root = tkinter.Tk()
root.title("Image Resizer")
frame = ttk.Frame(root, padding=10)
imageList = []
imageTypes = (".png", ".png", ".jpeg", ".webp", ".jpg")

savetype = tkinter.StringVar(root)

currentDir = tkinter.StringVar(root, "...")
maxH = tkinter.StringVar(root, "1080")
maxW = tkinter.StringVar(root, "1920")
qual = tkinter.StringVar(root, "25")

def get_dir():
    currentDir.set(filedialog.askdirectory())

def main():
    if(currentDir.get() == "..." or currentDir.get() == ""):
        messagebox.showerror(title="No Directory", message="No directory selected!")
        return

    saveDir = filedialog.askdirectory(title="Save to")
    imageList = os.listdir(currentDir.get())
    #print(imageList)
    maxHint = int(maxH.get())
    maxWint = int(maxW.get())

    #print(currentDir.get() + "/" + imageList[0]) #full dir
    for image in imageList:
        if(image.lower().endswith(imageTypes)):
            #main conversion loop
            fulldir = currentDir.get() + "/" + image
            #print(fulldir)
            curImage = Image.open(fulldir)
            fileName = image.split(".")
            #print(saveDir + fileName + ".png")
            curImage.thumbnail([maxHint, maxWint])
            curImage.save(saveDir + "/" + fileName[0] + savetype.get(), optimize=True, quality=int(qual.get()))

    messagebox.showinfo(title="Done", message="Completed Successfully!")

frame.grid()
dirEntry = ttk.Entry(frame, textvariable=currentDir).grid(column=0, row=0)
dirButton = ttk.Button(frame, text="dir", command=get_dir).grid(column=1, row=0)

maxHlabel = ttk.Label(frame, text="Max Height").grid(column=0, row=1)
maxWlabel = ttk.Label(frame, text="Max Width").grid(column=0, row=2)
qualabel = ttk.Label(frame, text="Quality / 100").grid(column=0, row=3)

maxHEntry = ttk.Entry(frame, textvariable=maxH).grid(column=1, row= 1)
maxWEntry = ttk.Entry(frame, textvariable=maxW).grid(column=1, row=2)
qualEntry = ttk.Entry(frame, textvariable=qual).grid(column=1, row=3)

filetypeOptionMenu = ttk.OptionMenu(frame, savetype, *imageTypes).grid(column=0, columnspan=2, row=4)

startButton = ttk.Button(frame, command=main, text="Start").grid(column=0, columnspan=2, row=5)

root.mainloop()
