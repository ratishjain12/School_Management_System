from tkinter import *

gui = Tk()
gui.geometry('500x500')
gui.resizable(0,0)



#----- FUNCTIONS -----
def submit():
    pass






defaultDate = StringVar(gui)
defaultDate.set('1')
defaultMonth = StringVar(gui)
defaultMonth.set('January')
var = IntVar()
labelDate = Label(text = 'Select Date')
labelMonth = Label(text = 'Select Month')
dateMenu = OptionMenu(gui, defaultDate, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
monthMenu = OptionMenu(gui, defaultMonth, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
presentButton = Radiobutton(gui, text = 'Present', variable = var, value = 'present')
absentButton = Radiobutton(gui, text = 'Absent', variable = var, value = 'absent')
submitButton = Button(gui, text = 'Submit', command = submit)
studentIdEntry = Entry(gui)
studentIdLabel = Label(gui, text = 'Enter Student ID')
studentNameEntry = Entry(gui, state = 'disabled')
studentNameLabel = Label(gui, text = 'Student Name')


labelDate.place(rely = 0.3, relx = 0.35)
dateMenu.place(rely = 0.29, relx = 0.51)
labelMonth.place(rely = 0.4, relx = 0.35)
monthMenu.place(rely = 0.39, relx = 0.51)
presentButton.place(rely = 0.53, relx = 0.3, anchor = W)
absentButton.place(rely = 0.53, relx = 0.5, anchor = W)
submitButton.place(rely = 0.6, relx = 0.43)
studentIdEntry.place(rely = 0.1, relx = 0.45)
studentIdLabel.place(rely = 0.1, relx = 0.25)
studentNameEntry.place(rely = 0.19, relx = 0.45)
studentNameLabel.place(rely = 0.19, relx = 0.25)


gui.mainloop()
