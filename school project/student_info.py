from tkinter import *

studentInfoGui = Tk()
studentInfoGui.geometry('500x500')
studentInfoGui.resizable(0,0)
studentInfoGui.title('Student Information')



#----- FUNTIONS -----
def register():
    registerGui = Toplevel(studentInfoGui)
    registerGui.title('Register')
    registerGui.geometry('500x500')
    registerGui.resizable(0,0)


    studentId = Entry(registerGui)
    name = Entry(registerGui)
    std = Entry(registerGui)
    sectionVar = StringVar(registerGui)
    sectionVar.set('A')
    section = OptionMenu(registerGui, sectionVar, 'A', 'B', 'C', 'D')
    rollno = Entry(registerGui)
    dobDateVar = StringVar(registerGui)
    dobDateVar.set('1')
    dobMonthVar = StringVar(registerGui)
    dobMonthVar.set('January')
    dobYearVar = StringVar(registerGui)
    dobYearVar.set('2000')
    dobDate = OptionMenu(registerGui, dobDateVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    dobMonth = OptionMenu(registerGui, dobMonthVar, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    dobYear = OptionMenu(registerGui, dobYearVar, '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
    genderVar = StringVar(registerGui)
    gender = OptionMenu(registerGui, genderVar, 'M', 'F', 'Other')
    address = Entry(registerGui)
    fatherName = Entry(registerGui)
    fatherNo = Entry(registerGui)
    fatherProfession = Entry(registerGui)
    motherName = Entry(registerGui)
    motherNo = Entry(registerGui)
    motherProfession = Entry(registerGui)



    registerGui.mainloop()

def update():
    pass


def remove():
    pass


def view():
    pass


def export():
    pass






registerButton = Button(studentInfoGui, text = 'Register', width = 10, height = 2, command = register)
updateButton = Button(studentInfoGui, text = 'Update', width = 10, height = 2, command = update)
removeButton = Button(studentInfoGui, text = 'Remove', width = 10, height = 2, command = remove)
viewButton = Button(studentInfoGui, text = 'View', width = 10, height = 2, command = view)
exportButton = Button(studentInfoGui, text = 'Export', width = 10, height = 2, command = export)
registerPhoto = PhotoImage(file = 'images\\registerIcon.png')
registerLabel = Label(image = registerPhoto)
viewPhoto = PhotoImage(file = 'images\\viewIcon.png')
viewLabel = Label(image = viewPhoto)
updatePhoto = PhotoImage(file = 'images\\updateIcon.png')
updateLabel = Label(image = updatePhoto)
removePhoto = PhotoImage(file = 'images\\removeIcon.png')
removeLabel = Label(image = removePhoto)
exportPhoto = PhotoImage(file = 'images\\exportIcon.png')
exportLabel = Label(image = exportPhoto)

registerButton.place(relx = 0.115, rely = 0.3)
viewButton.place(relx = 0.415, rely = 0.3)
updateButton.place(relx = 0.715, rely = 0.3)
removeButton.place(relx = 0.265, rely = 0.75)
exportButton.place(relx = 0.565, rely = 0.75)
registerLabel.place(relx = 0.115, rely = 0.1)
viewLabel.place(relx = 0.415, rely = 0.1)
updateLabel.place(relx = 0.715, rely = 0.1)
removeLabel.place(relx = 0.265, rely = 0.55)
exportLabel.place(relx = 0.565, rely = 0.55)



studentInfoGui.mainloop()
