import tkinter as tk
from tkinter import ttk

def cetak_pesan():
    data_inputan = input_nama.get()
    print(f"Teks yang di inputkan: {data_inputan}")

layar1 = tk.Tk() 
layar1.title("Contoh dari button")  

input_nama = ttk.Entry(layar1,width=30)
input_nama.pack(padx=20,pady=20)

tombol_catak = ttk.Button(layar1,text="Kirim!",command=cetak_pesan)
tombol_catak.pack()

layar1.mainloop() #jalankan code


