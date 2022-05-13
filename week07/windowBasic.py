import tkinter as tk
from tkinter import IntVar, messagebox


def yeezy() :
    messagebox.showinfo("BLACK SKINHEAD", "YEEZY SEAZON APPRAROACHING")

def album() :
    if var.get() == 1 :
        label2.configure(text = "My Beautiful Dark Twited Fantasy", bg="red", fg="black")
        photo.configure(file = "week6/kanye/mbdtf.gif")
    elif var.get() == 2 :
        label2.configure(text = "Yeezus", bg="white", fg="black")
        photo.configure(file = "week6/kanye/yeezus.gif")
    elif var.get() == 3 :
        label2.configure(text = "The Life Of Pablo", bg="orange", fg="black" )
        photo.configure(file = "week6/kanye/pablo2.gif")
    elif var.get() == 4 :
        label2.configure(text = "Donda", bg="black", fg="white")
        photo.configure(file = "week6/kanye/donda.gif")
    elif var.get() == 5 :
        label2.configure(text = "None of the above..", bg="white", fg="black")
        photo.configure(file = "week6/kanye/2.gif")





window = tk.Tk()
#시작


window.title("윈도창 연습")
# window.geometry("1000x600")

photo = tk.PhotoImage(file = "week6/kanye/2.gif")
photo1 = tk.PhotoImage(file = "week6/kanye/mbdtf.gif")
photo2 = tk.PhotoImage(file = "week6/kanye/yeezus.gif")
photo3 = tk.PhotoImage(file = "week6/kanye/pablo.gif")
photo4 = tk.PhotoImage(file = "week6/kanye/donda.gif")

button1 = tk.Button(window, text = "Quit", fg = "red", command = quit)
button2 = tk.Button(window, text = "Credits", fg = "black", command = yeezy)

var = IntVar()
rb1 = tk.Radiobutton(window, text = "My Beautiful Dark Twited Fantasy", variable = var, value = 1, command = album)
rb2 = tk.Radiobutton(window, text = "Yeezus", variable = var, value = 2, command = album)
rb3 = tk.Radiobutton(window, text = "The Life Of Pablo", variable = var, value = 3, command = album)
rb4 = tk.Radiobutton(window, text = "Donda", variable = var, value = 4, command = album)
rb5 = tk.Radiobutton(window, text = "None of the above..", variable = var, value = 5, command = album)


label1 = tk.Label(window, text = "Which is the Best album of Kanye West?", font = ("Hevetica", 18), bg = "black", fg = "white")
label2 = tk.Label(window, text = "ALBUM", font = ("Helvetica", 18), bg = "black", fg = "white")


label3 = tk.Label(window, text = "ye")
labelImage = tk.Label(window, image = photo, width=500, height=300)
label5 = tk.Label(window, image = photo2)



label1.pack()

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
rb5.pack()




label2.pack()
labelImage.pack()


# label3.pack()

# label5.pack(side = "left")
button2.pack()
button1.pack()



#끝

window.mainloop()