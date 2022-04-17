import tkinter as tk

def zoomIn(event) :
    global photo
    photo = photo.zoom(2, 2)
    labelImage.configure(image = photo)

def zoomOut(event) :
    global photo
    photo = photo.subsample(2, 2)
    labelImage.configure(image = photo)



window = tk.Tk()
window.geometry("1000x1000")

window.title("확대와 축소")

#2019038094 서도원입니다.

window.bind("<Up>", zoomIn)
window.bind("<Down>", zoomOut)





photo = tk.PhotoImage(file = "HW/HW6/img/london.gif")
labelImage = tk.Label(window, image = photo)
labelImage.pack()






window.mainloop()