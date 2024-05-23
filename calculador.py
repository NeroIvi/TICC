import tkinter as tk

pantalla = tk.Tk()
pantalla.title("Calculadora en python")

b1 = tk.Button(pantalla, text ="1",height= 5, width=10)
b1.grid(row=0, column=1)

b2 = tk.Button(pantalla, text ="2",height= 5, width=10)
b2.grid(row=0, column=2)
pantalla.mainloop() 



