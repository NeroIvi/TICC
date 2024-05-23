import tkinter as tk

pantalla = tk.Tk()
pantalla.title("Calculadora en python")

b1 = tk.Button(pantalla, text ="1")
b1.grid(row=0, column=1)
pantalla.mainloop() 


resultado = tk.Tk()
resultado.grid(row = 0, column =0)

pantalla.title("Mi pantalla en blanco")
pantalla.mainloop()
