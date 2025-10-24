import tkinter as tk
from tkinter import ttk

layar1 = tk.Tk() 
layar1.title("Contoh dari button")
layar1.geometry("1000x500")

tombol_satu = ttk.Button(layar1,text="Tombol di poisisi (x=30,y=50)")
tombol_satu.place(x=30,y=50)
tombol_dua = ttk.Button(layar1,text="Tombol di poisisi (x=150,y=120)")
tombol_dua.place(x=150,y=120)
layar1.mainloop() #jalankan code


