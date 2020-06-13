from tkinter import *


def registerGuiRun():
    #----- GUI -----
    registerGui = Toplevel()
    registerGui.title('Register')
    registerGui.geometry('600x600')
    registerGui.resizable(0,0)


    #----- FUNCTIONS -----
    def submit():
        pass


    #----- WIDGETS -----
    mainLabel = Label(registerGui, text = 'Student Registration')
    studentId = Entry(registerGui)
    studentIdLabel = Label(registerGui, text = 'Student ID')
    firstname = Entry(registerGui)
    firstnameLabel = Label(registerGui, text = 'First Name')
    lastname = Entry(registerGui)
    lastnameLabel = Label(registerGui, text = 'Last Name')
    std = Entry(registerGui)
    stdLabel = Label(registerGui, text = 'Standard')
    sectionVar = StringVar(registerGui)
    sectionLabel = Label(registerGui, text = 'Section')
    sectionVar.set('A')
    section = OptionMenu(registerGui, sectionVar, 'A', 'B', 'C', 'D')
    section.config(width = 2)
    rollno = Entry(registerGui)
    rollnoLabel = Label(registerGui, text = 'Roll No.')
    dobDateVar = StringVar(registerGui)
    dobDateVar.set('1')
    dobMonthVar = StringVar(registerGui)
    dobMonthVar.set('January')
    dobYearVar = StringVar(registerGui)
    dobYearVar.set('2000')
    dobLabel = Label(registerGui, text = 'DOB')
    dobDate = OptionMenu(registerGui, dobDateVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    dobMonth = OptionMenu(registerGui, dobMonthVar, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    dobYear = OptionMenu(registerGui, dobYearVar, '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
    dobDate.config(width = 2)
    dobMonth.config(width = 10)
    dobYear.config(width = 5)
    genderVar = StringVar(registerGui)
    gender = OptionMenu(registerGui, genderVar, 'M', 'F', 'Other')
    gender.config(width = 5)
    genderLabel = Label(registerGui, text = 'Gender')
    address = Entry(registerGui, width = 50)
    addressLabel = Label(registerGui, text = 'Address')
    fatherName = Entry(registerGui)
    fatherNameLabel = Label(registerGui, text = 'Father\'s Name')
    fatherNo = Entry(registerGui)
    fatherNoLabel = Label(registerGui, text = 'Father\'s No.')
    fatherProfession = Entry(registerGui)
    fatherProfessionLabel = Label(registerGui, text = 'Father\'s Profession')
    motherName = Entry(registerGui)
    motherNameLabel = Label(registerGui, text = 'Mother\'s Name')
    motherNo = Entry(registerGui)
    motherNoLabel = Label(registerGui, text = 'Mother\'s No.')
    motherProfession = Entry(registerGui)
    motherProfessionLabel = Label(registerGui, text = 'Mother\'s Profession')
    submitButton = Button(registerGui, text = 'Submit', command = submit, height = 2, width = 15)


    #----- PLACING WIDGETS -----
    mainLabel.place(relx = 0.4, rely = 0.005)
    firstnameLabel.place(relx = 0.1, rely = 0.05)
    firstname.place(relx = 0.23, rely = 0.05)
    lastnameLabel.place(relx = 0.1, rely = 0.1)
    lastname.place(relx = 0.23, rely = 0.1)
    addressLabel.place(relx = 0.1, rely = 0.15)
    address.place(relx = 0.23, rely = 0.15)
    dobLabel.place(relx = 0.1, rely = 0.21)
    dobDate.place(relx = 0.219, rely = 0.2)
    dobMonth.place(relx = 0.325, rely = 0.2)
    dobYear.place(relx = 0.501, rely = 0.2)
    genderLabel.place(relx = 0.1, rely = 0.275)
    gender.place(relx = 0.219, rely = 0.265)

    fatherNameLabel.place(relx = 0.1, rely = 0.35)
    fatherName.place(relx = 0.3215, rely = 0.35)
    fatherNoLabel.place(relx = 0.1,rely = 0.4)
    fatherNo.place(relx = 0.3215, rely = 0.4)
    fatherProfessionLabel.place(relx = 0.1, rely = 0.45)
    fatherProfession.place(relx = 0.3215, rely = 0.45)
    motherNameLabel.place(relx = 0.1, rely = 0.5)
    motherName.place(relx = 0.3215, rely = 0.5)
    motherNoLabel.place(relx = 0.1,rely = 0.55)
    motherNo.place(relx = 0.3215, rely = 0.55)
    motherProfessionLabel.place(relx = 0.1, rely = 0.6)
    motherProfession.place(relx = 0.3215, rely = 0.6)

    studentIdLabel.place(relx = 0.1, rely = 0.67)
    studentId.place(relx = 0.23, rely= 0.67)
    stdLabel.place(relx = 0.1, rely = 0.72)
    std.place(relx = 0.23, rely = 0.72)
    sectionLabel.place(relx = 0.1, rely = 0.78)
    section.place(relx = 0.225, rely = 0.77)
    rollnoLabel.place(relx = 0.1, rely = 0.845)
    rollno.place(relx = 0.23, rely = 0.845)

    submitButton.place(relx = 0.38, rely = 0.9)


    #----- MAINLOOP -----
    registerGui.mainloop()
