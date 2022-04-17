import tkinter as tk
from tkinter import ttk

tk.window = tk.Tk()
tk.window.title("여행지 조회")
tk.window.iconbitmap('python.ico')

baseTab = ttk.Notebook(tk.window)

tabLondon = ttk.Frame(baseTab)
tabParis = ttk.Frame(baseTab)

baseTab.add(tabLondon, text='런던')
baseTab.add(tabParis, text='파리')

baseTab.pack(expand=1, fill="both")

photoLondon = tk.PhotoImage(file = "HW/HW7/img/london.gif")
labelLondon = tk.Label(tabLondon, image = photoLondon)
labelLondon.pack()

photoParis = tk.PhotoImage(file = "HW/HW7/img/paris.gif")
labelParis = tk.Label(tabParis, image = photoParis)
labelParis.pack()



tk.window.mainloop()

