from tkinter import *
from tkinter import filedialog
import qrcode
import os


def code_generate():
    url_var = url.get()
    qr = qrcode.make(str(url_var))
    



root = Tk()
root.geometry("400x350")
root.title("URL to QR code generater")
image = PhotoImage(file='qr.png')
root.iconphoto(True,image)

url = StringVar()
name_to_save = StringVar()

label1 = Label(root,text='Save As').place(x=60,y=15)
dataEntry = Entry(textvariable=name_to_save)
dataEntry.config(width=30)
dataEntry.place(x = 60, y = 35)

label1 = Label(root, text="Inside QR Code ").place(x = 60, y = 55)

dataEntry = Entry(textvariable=url, width=30)
dataEntry.place(x = 60, y = 75)

button = Button(root,text='Get Code', command=code_generate, width= 30, height=5, bg='grey')
button.place(x = 80, y = 105)
root.mainloop()