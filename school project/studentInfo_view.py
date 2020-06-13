from tkinter import *


def viewGuiRun():
    #----- GUI -----
    viewGui = Toplevel()
    viewGui.title('View')
    viewGui.geometry('700x700')
    viewGui.resizable(0, 0)


    #----- FUNCTIONS -----





    #----- WIDGETS -----
    viewByLabel = Label(viewGui, text = "View By", font = 'Helvetica 16 bold')
    searchParameters = StringVar()
    searchParameters.set("Student ID")
    searchBy = OptionMenu(viewGui, searchParameters, "Student ID", "Roll No", "Name", "Class")
    searchBy.config(width = 10)
    searchLabel = Label(viewGui, text = "Search Here:")
    searchEntry = Entry(viewGui, width = 30)
    searchButton = Button(viewGui, text = "Search", width = 10)
    displayArea = Listbox(viewGui, width  = 100, height = 30)
    deleteButton = Button(viewGui, text = "Delete", height = 2, width = 15)
    updateButton = Button(viewGui, text = 'Update', height = 2, width = 15)
    openButton = Button(viewGui, text  = 'Open', height = 2, width = 15)


    #----- PLACING WIDGETS -----
    viewByLabel.place(relx = 0.13, rely = 0.095)
    searchBy.place(relx  = 0.26, rely = 0.095)
    searchEntry.place(relx = 0.44, rely = 0.1)
    searchButton.place(relx = 0.73, rely = 0.1)
    displayArea.place(relx = 0.0715, rely = 0.2)
    openButton.place(relx = 0.1, rely = 0.9)
    updateButton.place(relx = 0.425, rely = 0.9)
    deleteButton.place(relx = 0.745, rely = 0.9)





    #----- MAINLOOP -----
    viewGui.mainloop()
