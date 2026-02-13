from tkinter import *
import re

def validate():
    adress = Adress_user.get()
    pass

root = Tk()

screen_width = root.winfo_screenwidth()
screen_length = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_length}")

head_label = Label(root, text="Enter your adress to get it validate")
head_label.pack()

Adress_user = Entry(root)
Adress_user.pack()

Validate_button = Button(root, text='Validate',command=validate )
Validate_button.pack()



root.mainloop()