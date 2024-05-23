from tkinter import *
root = Tk( )

b=0
for r in range(1, 4):
    for c in range(3):
        b=b+1
        Button(root, text=str(b),borderwidth=1, height=1, width=5).grid(row=r,column=c)

op1 = Button(root, text="+",borderwidth=1, height=1, width=5 ).grid(row=2, column=5)
op2 = Button(root, text="-",borderwidth=1, height=1, width=5 ).grid(row=2, column=6)
op3 = Button(root, text="/",borderwidth=1, height=1, width=5 ).grid(row=3, column=5)
op4 = Button(root, text="x",borderwidth=1, height=1, width=5 ).grid(row=3, column=6)
op5 = Button(root, text="=",borderwidth=1, height=1, width=5).grid(row=1, column=6)
op6 = Button(root, text="AC",borderwidth=1, height=1, width=5).grid(row=1,column=5)


pantalla = Label(root, text="A").grid(row=0, column=0, columnspan=7)
root.mainloop()