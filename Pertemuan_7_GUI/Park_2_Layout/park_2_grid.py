import tkinter as tk
from tkinter import ttk

layar1 = tk.Tk() 
layar1.title("Contoh dari button")

# email
ttk.Label(layar1,text="Email : ").grid(row=0,column=0,sticky="w",padx=5,pady=5)
ttk.Entry(layar1,).grid(row=0,column=1,padx=5,pady=5)
# password
ttk.Label(layar1,text="Password : ").grid(row=1,column=0,sticky="w",padx=5,pady=5)
ttk.Entry(layar1,).grid(row=1,column=1,padx=5,pady=5)


layar1.mainloop() #jalankan code


