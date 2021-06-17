from tkinter import *
from projectdb import Database
from tkinter.font import BOLD
from tkinter import messagebox
from projectdb import Database

projectdb=Database('employee.db')

LABEL_FONT = "Adobe Gothic Std"

def populate_list():
    parts_list.delete(0, END)
    for row in projectdb.fetch():
        parts_list.insert(END, row)

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        Nameentry.delete(0, END)
        Nameentry.insert(END, selected_item[1])
        Carentry.delete(0, END)
        Carentry.insert(END, selected_item[2])
        Clockinentry.delete(0, END)
        Clockinentry.insert(END, selected_item[3])
        Clockoutentry.delete(0, END)
        Clockoutentry.insert(END, selected_item[4])
        Dateentry.delete(0, END)
        Dateentry.insert(END, selected_item[5])
    except IndexError:
        pass

def add_item():
    if Nameentry.get() == '' or Carentry.get() == '' or Clockinentry.get() == '' or Clockoutentry.get() == '' or Dateentry.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    projectdb.insert(Nameentry.get(),Carentry.get(),Clockinentry.get(),Clockoutentry.get(), Dateentry.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (Nameentry.get(),Carentry.get(),Clockinentry.get(),Clockoutentry.get(), Dateentry.get()))
    clear_text()
    populate_list()

def remove_item():
    projectdb.remove(selected_item[0])
    populate_list()


def update_item():
    print('hello')


def clear_text():
    Nameentry.delete(0, END)
    Carentry.delete(0, END)
    Clockinentry.delete(0, END)
    Clockoutentry.delete(0, END)
    Dateentry.delete(0, END)


window = Tk()
window.title("Automoblie Workshop Rwanda")
window.config(padx=50, pady=50)
window.geometry("400x500")


namelabel = Label(text="Employee ID 1: ", font=('bold', 14))
namelabel.grid(column=0, row=1)


Car= Label(text="Car : ", font=('bold', 14))
Car.grid(column=0, row=2)

Clockinlabel = Label(text="Clock In:", font=('bold', 14))
Clockinlabel.grid(column=0, row=3)

Clockoutlabel = Label(text="Clock Out: ", font=('bold', 14),)
Clockoutlabel.grid(column=0, row=4)

Datelabel = Label(text="Date: ", font=('bold', 14),)
Datelabel.grid(column=0, row=5)



Nameentry = Entry(width=20)
Nameentry.grid(column=1, row=1, columnspan=2, pady=5)
Nameentry.focus()


Carentry = Entry(width=20)
Carentry.grid(column=1, row=2, columnspan=2, pady=5)


Clockinentry = Entry(width=20)
Clockinentry.grid(column=1, row=3, columnspan=2, pady=5)

Clockoutentry = Entry(width=20)
Clockoutentry.grid(column=1, row=4, columnspan=2, pady=5)

Dateentry = Entry(width=20)
Dateentry.grid(column=1, row=5, columnspan=2, pady=5)



#parts List (listbox)
parts_list = Listbox(window,height=12,width=60)
parts_list.grid(row=9,column=0,columnspan=3,rowspan=8,padx=30,pady=20)
parts_list.bind('<<ListboxSelect>>', select_item)



button1 = Button(text="Add", width=12,  command=add_item)
button1.grid(column=0, row=6, pady=5)

button2 = Button(text="Remove", width=12, command=remove_item)
button2.grid(column=1, row=6, pady=5)


button3 = Button(text="Clear", width=12,  command=clear_text)
button3.grid(column=2, row=6, pady=5)


button4=Button(window,text="Monday")
button4.grid(column=0,row=7)

button5=Button(window,text="Tuesday")
button5.grid(column=1,row=7)

button6=Button(window,text="Wednesday")
button6.grid(column=2,row=7)

button7=Button(window,text="Thursday")
button7.grid(column=3,row=7)

button8=Button(window,text="Friday")
button8.grid(column=0,row=8)

button9=Button(window,text="Saturday")
button9.grid(column=1,row=8)

button10=Button(window,text="Sunday")
button10.grid(column=2,row=8)

button11=Button(window,text="Shift Morning")
button11.grid(column=4,row=2)

button12=Button(window,text="Shift Afternoon")
button12.grid(column=5,row=2)


populate_list()
window.mainloop()