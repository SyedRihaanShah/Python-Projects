from tkinter import *
from tkinter import filedialog
import qrcode
import os


def code_generate():
    url_var = url.get()
    qr = qrcode.make(str(url_var))
    loc = filedialog.askdirectory()
    os.chdir(loc)
    save_as = name_to_save.get()
    done_label = Label(root, text='Done', bg='red')
    done_label.pack()
    qr.save(f"{save_as}.png")

    



root = Tk()
root.geometry("400x350")
root.title("URL to QR code generater")
# image = PhotoImage(file= 'qr.png')
# root.iconphoto(True,image)

url = StringVar()
name_to_save = StringVar()

Save_As_Label = Label(root,text='Save As').pack()

dataEntry = Entry(root, textvariable=name_to_save, bg='Grey')
dataEntry.config(width=30)

dataEntry.pack()

Inside_QR_Code = Label(root, text="Inside QR Code ").pack()

dataEntry = Entry(textvariable=url, width=30, bg='Grey')
dataEntry.pack()

button = Button(root,text='Get Code', command=code_generate, width= 12, height=3, bg='grey')
button.pack()
root.mainloop()