# import tkinter as tk

# pantalla = tk.Tk()
# pantalla.title("Calculadora en python")

# b1 = tk.Button(pantalla, text ="1",height= 5, width=10)
# b2 = tk.Button(pantalla, text ="2",height= 5, width=10)
# b1.grid(row = 0, column = 0, pady = 2)
# b2.grid(row = 1, column = 0, pady = 2)
# pantalla.geometry("700x700+100+100")
# pantalla.mainloop() 
from tkinter import *
root = Tk( )
b=0
for r in range(1, 4):
    for c in range(3):
        b=b+1
        Button(root, text=str(b),
        borderwidth=1 ).grid(row=r,column=c)

pantalla = Label(root, text="A").grid(row=0, column=0, columnspan=6)
root.mainloop()


