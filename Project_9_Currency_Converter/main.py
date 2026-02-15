from tkinter import * 
from decimal import Decimal
from forex_python.converter import CurrencyRates

c = CurrencyRates(force_decimal=True)

def Currency_Converter():
    current_currecny = user_currency.get()
    amount_user = amount.get()
    user_second = second_currecny.get()
    converted_amount = c.convert(current_currecny.upper(), user_second.upper(), Decimal(amount_user))
    Converted_label = Label(root, text=f'{amount_user} {current_currecny} in {user_second} is {converted_amount}', font=('Dante', 20))
    Converted_label.place(x = 350, y = 250 )

root = Tk()

root.title("CURRENCY CONVERTER")

user_currency = StringVar()
amount = IntVar()
second_currecny = StringVar()

Head_label = Label(text='CURRENCY CONVERTER', font=('Dante', 40, 'bold'))
Head_label.pack()

Your_currency_label = Label(root,text= 'Enter Your Currency', font=('Dante', 20))
Your_currency_label.place(x = 50, y = 50)

Enter_currency = Entry(root, textvariable= user_currency, bg='#636262')
Enter_currency.place(x = 250 , y = 50)

Amount = Label(root, text='Amount You Want To Convert', font=('Dante', 20))
Amount.place(x = 50, y = 100 )

Amount_Entry = Entry(root, textvariable=amount, bg='#636262')
Amount_Entry.place(x = 350, y = 100)

Second_currency = Label(root, text='In Which Currency You Want To Convert', font=('Dante', 20))
Second_currency.place(x = 50, y = 150)

Second_Entry = Entry(root, textvariable= second_currecny, bg = '#636262')
Second_Entry.place(x = 450, y = 150 )

Converter_Button = Button(root, text='CONVERT', width= 50, command=Currency_Converter)
Converter_Button.place(x = 350, y = 200)


root.mainloop()