import tkinter as tk
from tkinter import ttk


def getSapa(event):
    print(f"Hello World!!!!!")

layar1 = tk.Tk() 
layar1.title("Using Command")

lebel = ttk.Label(layar1,text="Arahakn mouse ke sini !")
lebel.bind("<Enter>",getSapa)
lebel.pack(padx=10,pady=10)

layar1.mainloop() #jalankan code


