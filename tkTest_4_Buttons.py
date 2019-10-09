##  incorporating datetime, tk form, and button functions

from tkinter import *
import datetime

today = datetime.date.today()
fullDate = today.strftime("%B %d, %Y")
weekDayName = today.strftime("%A")

git = today - datetime.date(2019,4,29)
birthday = datetime.date(2020,10,16) - today

root = Tk()
root.title("Testing Buttons")
root.minsize(400, 300)


def Greeting():
    Label(frame, text="Hello Chuck, Today is " +weekDayName +", " +fullDate +"."
          ).grid(row=1, column=0, padx=10, pady=3)
def Birthday():
    Label(frame, text="Your 45th birthday is in " +str(birthday.days) +" days."
          ).grid(row=4, column=0, padx=10, pady=3)
def GitAccount():
    Label(frame, text="You created your Git account " +str(git.days) +" days ago."
          ).grid(row=6, column=0, padx=10, pady=3)

frame = Frame(root, bd=1, relief=SUNKEN, height=350, width=250)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
button1 = Button(frame, text="Greeting", command=Greeting)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(frame, text="Birthday", command=Birthday)
button2.grid(row=3, column=0, padx=10, pady=10)

button3 = Button(frame, text="Git Account", command=GitAccount)
button3.grid(row=5, column=0, padx=10, pady=10)

root.mainloop()
