from tkinter import *
import random

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='How many letters would you like in your password?')
        self.lbl2=Label(win, text='How many symbols would your like in your password?')
        self.lbl3 = Label(win, text='How many numbers would you like in your password?')
        self.lbl4=Label(win, text='Password :')

        self.t1=Entry()
        self.t2=Entry()
        self.t3 = Entry()
        self.t4=Entry()

        self.btn1 = Button(win, text='Generate Password')

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=500, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=500, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=500, y=150)

        self.b1=Button(win, text='Generate Password', command=self.add, fg='blue')
        self.b1.place(x=300, y=200)

        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)

    def add(self):
        self.t4.delete(0, 'end')

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '(', ')', '*', '+', '^']

        num_letters = int(self.t1.get())
        num_symbols = int(self.t2.get())
        num_numbers = int(self.t3.get())

        passwoard_list = []

        for i in range(1, num_letters + 1):
            random_characters = random.choice(letters)
            passwoard_list.append(random_characters)

        for i in range(1, num_symbols + 1):
            random_symbols = random.choice(symbols)
            passwoard_list.append(random_symbols)

        for i in range(1, num_numbers + 1):
            random_numbers = random.choice(numbers)
            passwoard_list.append(random_numbers)

        random.shuffle(passwoard_list)
        passwoard_list.reverse()

        passwoard = ""
        for char in passwoard_list:
            passwoard += char

        result=passwoard
        self.t4.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Password Generator!!')
lbl=Label(window, text="Welcome to the password generator!!", fg='red', font=("Helvetica", 30))
lbl.pack(pady= 100)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl.pack(side=TOP)
window.geometry("800x500")
window.mainloop()
