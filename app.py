from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import glob

# Create the main window
root = Tk()
root.title("Toddler Detection Model")
root.geometry("300x800")

photos = []

def button_click(id):
    print(f"Click {id}")

def create_label(img, row, col):
    image = Image.open(img).resize((150, 150))
    image_tk = ImageTk.PhotoImage(image)
    photos.append(image_tk)

    label = Label(root, image=image_tk)
    label.grid(row=row, column=0, rowspan=2)

    info_label = Label(root, text=img)
    info_label.grid(row=row, column=1, ipadx=10, ipady=10)

    button = Button(root, text="Detect", command = lambda: button_click(img))
    button.grid(row = row + 1, column=1)

r = 0
for file in glob.glob("*.jpg"):
    create_label(file, r, 0)
    r = r + 2
    #print(file)

root.mainloop()