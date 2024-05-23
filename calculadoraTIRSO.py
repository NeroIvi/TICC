import tkinter as tk
from tkinter import ttk


pantalla = tk.Tk()

pantalla.geometry('300x200')
pantalla.resizable(False, False)
pantalla.title('CALCULADORA')

boton = ttk.Button(
    pantalla,
    text='1',
)
boton2 = ttk.Button(
    pantalla,
    text='2',
)
boton.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
boton2.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
pantalla.mainloop()