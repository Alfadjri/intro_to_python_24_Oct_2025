import tkinter as tk
from tkinter import ttk

layar1 = tk.Tk() # buat jendela baru
layar1.title("Contoh dari lebel")  #buat memberikanlebel jendela

lebel_sambutan = ttk.Label(
    layar1, #lokasi jendela
    text="Selamat datang di GUI Pertama", #pesan nya
    font=("Helvetica",10) # tipe font nya
)

lebel_sambutan.pack(pady=20,padx=20) #style atau layout
layar1.mainloop() #jalankan code


