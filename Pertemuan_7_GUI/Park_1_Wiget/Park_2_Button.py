import tkinter as tk
from tkinter import ttk

def sambutan():
    print("Tombol behasil di click! Sebuah aksi akan muncul")

layar1 = tk.Tk() 
layar1.title("Contoh dari button")  

tombol_aksi = ttk.Button(
    layar1,
    text="Klick Saya!",
    command=sambutan
)


tombol_aksi.pack(padx=20,pady=20)
layar1.mainloop() #jalankan code


