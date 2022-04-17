import tkinter as tk
from tkinter.filedialog import *

def zoomIn(event) :
    global photo
    photo = photo.zoom(2, 2)
    labelImage.configure(image = photo)

def zoomOut(event) :
    global photo
    photo = photo.subsample(2, 2)
    labelImage.configure(image = photo)

def openGif() :
    fileName = askopenfilename(parent = window, filetypes = (("GIF파일", "*.gif"), ("모든 파일", "*.*")))
    global photo
    photo = tk.PhotoImage(file = "fileName")
    labelImage = tk.Label(window, image = photo)
    labelImage.pack()



window = tk.Tk()
window.geometry("1000x1000")

window.title("확대와 축소")

#2019038094 서도원입니다.

window.bind("<Up>", zoomIn)
window.bind("<Down>", zoomOut)

mainMenu = tk.Menu(window)
window.config(menu = mainMenu)
fileMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = openGif)
fileMenu.add_separator()

photo = tk.PhotoImage(file = "HW/HW7/img/london.gif")
labelImage = tk.Label(window, image = photo)
labelImage.pack()











window.mainloop()