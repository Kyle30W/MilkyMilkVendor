# --- Currency Converter ---
#
# --- Kyle Wilkinson ---
# --- 9/03/2021 ---

# import libraries

from tkinter import *

# --- Define Functions ---
def MilkPrice():
    milk = float(inpMilk.get())
    price = milk * 2.5
    lblMilk.config(text = "$%.2f"%price)
   

def CheesePrice():
    milk = float(inpCheese.get())
    price = milk * 20
    lblCheese.config(text = "$%.2f"%price)

def CowPrice():
    cow = float(inpCow.get())
    price = cow * 7.5
    lblCow.config(text = "$%.2f"%price)

def CreamPrice():
    cream = float(inpCream.get())
    price = cream * 2.75
    lblCream.config(text = "$%.2f"%price)
    
def Total():
    milk = float(inpMilk.get())
    milkprice = milk * 2.5
    cheese = float(inpCheese.get())
    cheeseprice = cheese * 20
    cow = float(inpCow.get())
    cowprice = cow * 7.5
    cream = float(inpCream.get())
    creamprice = cream * 2.75
    price = cheeseprice + milkprice + cowprice + creamprice
    lblTotal.config(text = "$%.2f"%price)

def change():
    milk = float(inpMilk.get())
    milkprice = milk * 2.5
    cheese = float(inpCheese.get())
    cheeseprice = cheese * 20
    cow = float(inpCow.get())
    cowprice = cow * 7.5
    cream = float(inpCream.get())
    creamprice = cream * 2.75
    price = cheeseprice + milkprice + cowprice + creamprice
    money = float(inpMoney.get())
    change = money - price
    if change < 0:
        Window.destroy()
    elif change > 0:
        lblChange.config(text = "$%.2f"%change)
        
def Callfunctions():
    MilkPrice()
    CheesePrice()
    CowPrice()
    CreamPrice()
    Total()

def Clear():
    inpMilk.delete(0, END)
    inpCheese.delete(0, END)
    inpCow.delete(0, END)
    inpCream.delete(0, END)
    inpMoney.delete(0, END)
    lblMilk.config(text = "")
    lblCheese.config(text = "")
    lblCow.config(text = "")
    lblCream.config(text = "")
    lblTotal.config(text = "")
    lblChange.config(text = "")

def Exit():
    Window.destroy()

# --- Design the Graphical User Interface (GUI) ---
# Build the window
Window = Tk() # This creates a GUI and assigns it a name
Window.title("Milky Milk - Kyle Wilkinson")
Window.configure(bg = "Bisque")
Window.geometry("500x500+0+0") # sets the dimension window. Width, Height, x position, Y position

# Create the widgets - Labels, text boxes, buttons

# - Labels -
lblHeader = Label(Window, text="Milky Milk", fon=("default", 20),fg="black", bg="Bisque")
lblSubHeader = Label(Window, text="Welcome to the shop what would you like?", fon=("default", 8),fg="black", bg="Bisque")
lblSeperate = Label(Window, text="------------------------------------------------------------------------------------------------------------", fon=("default", 14), fg="grey", bg="bisque")

lblMilklabel = Label(Window, text="Litres of milk at $2.50 per Litre", fon=("default", 10),fg="black", bg="Bisque")
lblCheeselabel = Label(Window, text="Killos of cheese at $20 per Killo", fon=("default", 10),fg="black", bg="Bisque")
lblCowlabel = Label(Window, text="Killos of cow at $7.50 per Killo", fon=("default", 10),fg="black", bg="Bisque")
lblCreamlabel = Label(Window, text="Litres of Cream at $2.75 per litre", fon=("default", 10),fg="black", bg="Bisque")

lblMilk = Label(Window, text="", fon=("default", 14),fg="black", bg="white")
lblCheese = Label(Window, text="", fon=("default", 14),fg="black", bg="white")
lblCow = Label(Window, text="", fon=("default", 14),fg="black", bg="white")
lblCream = Label(Window, text="", fon=("default", 14),fg="black", bg="white")

lblMoneylabel = Label(Window, text="How much money are you giving me?", fon=("default", 11), fg="black", bg="Bisque")
lblTotallabel = Label(Window, text="Total = ", fon=("default", 14),fg="black", bg="Bisque")
lblChangelabel = Label(Window, text="Change = ", fon=("default", 14),fg="black", bg="Bisque")

lblTotal = Label(Window, text="", fon=("default", 14), fg="Black", bg="white")
lblChange = Label(Window, text="", fon=("default", 14), fg="Black", bg="white")

#Location
lblHeader.place(x=90, y=30, width=300, height=30)
lblSubHeader.place(x=90, y=60, width=300, height=15)

lblMilklabel.place(x=75, y=100, width=300, height=40)
lblCheeselabel.place(x=75, y=150, width=300, height=40)
lblCowlabel.place(x=75, y=200, width=300, height=40)
lblCreamlabel.place(x=75, y=250, width=300, height=40)

lblMilk.place(x=350, y=100, width=100, height=40)
lblCheese.place(x=350, y=150, width=100, height=40)
lblCow.place(x=350, y=200, width=100, height=40)
lblCream.place(x=350, y=250, width=100, height=40)

lblMoneylabel.place(x=0, y=310, width=250, height=40)
lblTotallabel.place(x=275, y=325, width=75, height=40)
lblChangelabel.place(x=250, y=375, width=100, height=40)

lblTotal.place(x=350, y=325, width=100, height=40)
lblChange.place(x=350, y=375, width=100, height=40)

lblSeperate.place(x=0, y=300, width=500, height=10)

# - Input Boxes -
# Name and Style
inpMilk = Entry(Window, font=("Default", 14), fg="black", bg="white")
inpCheese = Entry(Window, font=("Default", 14), fg="black", bg="white")
inpCow = Entry(Window, font=("Default", 14), fg="black", bg="white")
inpCream = Entry(Window, font=("Default", 14), fg="black", bg="white")

inpMoney = Entry(Window, font=("Default", 14), fg="black", bg="white")

#Location
inpMilk.place(x=60, y=100, width=50, height=40)
inpCheese.place(x=60, y=150, width=50, height=40)
inpCow.place(x=60, y=200, width=50, height=40)
inpCream.place(x=60, y=250, width=50, height=40)

inpMoney.place(x=25, y=360, width=175, height=40)

# - Buttons -
# Name and Style
btnPay = Button(Window, text="PAY", font="24", fg="white", bg="dimgrey", command = change)
btnEnter = Button(Window, text="ENTER", font="24", fg ="white", bg="dimgrey", command = Callfunctions)
btnClear = Button(Window, text="CLEAR", font="24", fg ="white", bg="dimgrey", command = Clear)
btnExit = Button(Window, text="EXIT", font="24", fg ="white", bg="dimgrey", command = Exit)

#Location
btnPay.place(x=50, y=450, width=75, height=40)
btnEnter.place(x=150, y=450, width=75, height=40)
btnClear.place(x=250, y=450, width=75, height=40)
btnExit.place(x=350, y=450, width=75, height=40)

# --- Run the mainloop ---
Window.mainloop()