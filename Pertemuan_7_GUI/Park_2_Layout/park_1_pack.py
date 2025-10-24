import tkinter as tk
from tkinter import ttk

layar1 = tk.Tk() 
layar1.title("Contoh dari button")

ttk.Label(layar1,text="Lebel 1").pack()
ttk.Button(layar1,text="Button 2").pack()
ttk.Label(layar1,text="label ke tiga").pack(padx=50,pady=50)


layar1.mainloop() #jalankan code


