import tkinter as tk
from tkinter import ttk


def getSapa():
    print(f"Hello World!!!!!")

layar1 = tk.Tk() 
layar1.title("Using Command")

btn = ttk.Button(layar1,text="Sapa !",command=getSapa)
btn.pack(padx=10,pady=10)

layar1.mainloop() #jalankan code


