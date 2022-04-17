import tkinter as tk
from tkinter import IntVar, messagebox



def chooseCity() :
    if var.get() == 1 :
        label2.configure(text = "바르셀로나", bg="red", fg="black")
        photo.configure(file = "HW/HW7/img/barcelona.gif")
    elif var.get() == 2 :
        label2.configure(text = "베를린", bg="white", fg="black")
        photo.configure(file = "HW/HW7/img/berlin.gif")
    elif var.get() == 3 :
        label2.configure(text = "런던", bg="orange", fg="black" )
        photo.configure(file = "HW/HW7/img/london.gif")
    elif var.get() == 4 :
        label2.configure(text = "파리", bg="black", fg="white")
        photo.configure(file = "HW/HW7/img/paris.gif")
    elif var.get() == 5 :
        label2.configure(text = "베니스", bg="white", fg="black")
        photo.configure(file = "HW/HW7/img/venice.gif")

#2019038094 서도원입니다.

window = tk.Tk()
#시작


window.title("윈도창 연습")
# window.geometry("1000x600")


label1 = tk.Label(window, text = "가장 가고싶은 유럽 도시를 선택하세요!", font = ("궁서", 18), fg = "skyblue")
label2 = tk.Label(window, text = "EUROPE", font = ("Helvetica", 18), bg = "black", fg = "white")

photo = tk.PhotoImage(file = "HW/HW7/img/europe.gif")
labelCity = tk.Label(window, image = photo, width=500, height=300)

button1 = tk.Button(window, text = "Quit", fg = "red", command = quit)


var = IntVar()
rb1 = tk.Radiobutton(window, text = "바르셀로나", variable = var, value = 1, command = chooseCity)
rb2 = tk.Radiobutton(window, text = "베를린", variable = var, value = 2, command = chooseCity)
rb3 = tk.Radiobutton(window, text = "런던", variable = var, value = 3, command = chooseCity)
rb4 = tk.Radiobutton(window, text = "파리", variable = var, value = 4, command = chooseCity)
rb5 = tk.Radiobutton(window, text = "베니스", variable = var, value = 5, command = chooseCity)

label1.pack()

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
rb5.pack()

label2.pack()
labelCity.pack()

button1.pack()





#끝

window.mainloop()