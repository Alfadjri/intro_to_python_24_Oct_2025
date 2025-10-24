import tkinter as tk
from tkinter import ttk,messagebox

layar = tk.Tk()
layar.title("Kalkulator Sederhanan!!!!")

def pembagian():
    try:
        x = float(value1.get())
        y = float(value2.get())
        hasil = x / y
        hasil_lebel.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
        hasil_lebel.config(text=f"Hasil : {hasil}")
    except ValueError:
        messagebox.showerror("Input Salaha","Harap masukan angka valid")
    except ZeroDivisionError:
        messagebox.showerror("Kesalahan matematis","Tidak bisa membagi dengan bilangan nol (0)")

ttk.Label(layar,text="Masukan Angka 1 : ").grid(row=0,column=0,sticky="w",padx=5,pady=5)
value1 = ttk.Entry(layar)
value1.grid(row=0,column=1,padx=5,pady=5)
ttk.Label(layar,text="Masukan Angka 1 : ").grid(row=1,column=0,sticky="w",padx=5,pady=5)
value2 = ttk.Entry(layar)
value2.grid(row=1,column=1,padx=5,pady=5)
hasil_lebel = ttk.Label(layar,text="")
ttk.Button(layar,text="Bagi",command=pembagian).grid(row=4,column=0,columnspan=2,padx=5,pady=5)
layar.mainloop()