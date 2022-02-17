from tkinter import *
from numpy import pad

from pyparsing import col
import backEnd

def view_command():
    bookList.delete(0, END)
    for row in backEnd.view():
        bookList.insert(END, row)

def search_command():
    bookList.delete(0, END)
    for row in backEnd.search(titleInput.get(), author.get(), year.get(), isbn.get()):
        bookList.insert(END, row)

def insert_command():
    backEnd.insert(titleInput.get(), author.get(), year.get(), isbn.get())
    bookList.delete(0, END)

def get_selected_row(event):
    global index
    index = bookList.curselection()[0]
    return index

def delete_command():
    backEnd.delete(index)
    bookList.delete(0, END)
    for row in backEnd.view():
        bookList.insert(END, row)





window = Tk()
window.title("Book Inventory")
window.geometry("500x350")

#LABELS
titleLabel = Label(window, text = "Title: ", padx= 10,pady=15, font=("bold",11))
titleLabel.grid(row=0, column=0)

yearLabel = Label(window, text = "Year: ", padx= 10,pady=15, font=("bold",11))
yearLabel.grid(row=0, column=3)

authorLabel = Label(window, text = "Author: ", padx= 10,pady=15, font=("bold",11))
authorLabel.grid(row=1, column=0)

isbnLabel = Label(window, text = "ISBN: ", padx= 10,pady=15, font=("bold",11))
isbnLabel.grid(row=1, column=3)


#ENTRIES
titleInput = StringVar()
titleEntry = Entry(window, textvariable=titleInput)
titleEntry.grid(row=0, column=1)

year = StringVar()
yearEntry = Entry(window, textvariable=year)
yearEntry.grid(row=0, column=4)

author = StringVar()
authorEntry = Entry(window, textvariable=author)
authorEntry.grid(row=1, column=1)

isbn = StringVar()
isbnEntry = Entry(window, textvariable=isbn)
isbnEntry.grid(row=1, column=4)


#LISTBOX
bookList = Listbox(window, height = 12, width = 40)
bookList.grid(row=2, column=0, columnspan=3, rowspan=6)

bookList.bind("<<ListboxSelect>>", get_selected_row)

#SCROLLBARS
scrolly = Scrollbar(window)
scrolly.grid(row=2, column=3, sticky="W", rowspan=6)
bookList.configure(yscrollcommand=scrolly.set)
scrolly.configure(command = bookList.yview)

scrollx = Scrollbar(window, orient='horizontal')
scrollx.grid(row=8, column=0, columnspan=3)
bookList.configure(xscrollcommand=scrollx.set)
scrolly.configure(command = bookList.xview)


#BUTTONS
viewButton = Button(window, text="View All", width=20, command= view_command)
viewButton.grid(row=2, column=4, )

searchButton = Button(window, text="Search Entry", width=20, command=search_command)
searchButton.grid(row=3, column=4, )

addButton = Button(window, text="Add Entry", width=20, command=insert_command)
addButton.grid(row=4, column=4, )

updateButton = Button(window, text="Update", width=20)
updateButton.grid(row=5, column=4, )

deleteButton = Button(window, text="Delete", width=20, command=delete_command)
deleteButton.grid(row=6, column=4, )

closeButton = Button(window, text="Close", width=20)
closeButton.grid(row=7, column=4, )




window.mainloop()
