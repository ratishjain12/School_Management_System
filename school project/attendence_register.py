from tkinter import *
from database import db,cursor
from tkinter import messagebox



def registerGuiRun():
    #----- GUI -----
    registerGui = Toplevel()
    registerGui.title('Register')
    registerGui.geometry('600x600')
    registerGui.resizable(0,0)


    #----- FUNCTIONS -----
    def verifyStudent():
    	studentId = studentIdEntry.get().strip()
    	try:
    		cursor.execute('select * from studentdata where studentId = %s'%(studentId))
    	except:
    		messagebox.showerror('Attendence', 'Please enter a valid Student ID')

    	data = cursor.fetchall()
    	if len(data) != 0:
    		studentNameEntry.config(state = 'normal')
    		name = data[0][1] + ' ' + data[0][2]
    		studentNameEntry.delete(0, END)
    		studentNameEntry.insert(0, name)
    		studentNameEntry.config(state = 'disabled', disabledforeground  = 'black')


    	else:
    		messagebox.showerror('Attendence', 'No data found')


    def check():
        if len(studentIdEntry.get().strip()) == 0:
            messagebox.showerror('Attendence', "Please enter a Student ID")
            

        elif len(yearEntry.get().strip()) != 4:
            messagebox.showerror('Attendence', 'Please enter a valid year')

            

        issue_counter = 0
        variables = [ janVar, febVar, marVar, aprVar, mayVar, junVar, 
                      julVar, augVar, sepVar, octVar, novVar, decVar]

        for variable in variables:
            if variable.get() == '':
                messagebox.showerror('Attendence', 'Please fill all the details')
                issue_counter += 1
                break
        studentId = studentIdEntry.get().strip()
        year = yearEntry.get().strip()
        cursor.execute('use school')
        cursor.execute('select * from attendence where studentId = %s and year = %s'%(studentId, year))
        data = cursor.fetchall()
        if len(data) != 0:
            messagebox.showerror('Attendence', "Data already exists")
            issue_counter += 1

        if issue_counter == 0:
            submit()


    def submit():
        studentId = studentIdEntry.get().strip()
        year = yearEntry.get().strip()
        jan = janVar.get()
        feb = febVar.get()
        mar = marVar.get()
        apr = aprVar.get()
        may = mayVar.get()
        jun = junVar.get()
        jul = julVar.get()
        aug = augVar.get()
        sep = sepVar.get()
        octo = octVar.get()
        nov = novVar.get()
        dec = decVar.get()


        cursor.execute('use school')
        cursor.execute('insert into attendence values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'%(studentId, year, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))

        messagebox.showinfo('Attendence', 'Data Successfully Registered')

        studentIdEntry.delete(0, END)
        yearEntry.delete(0, END)
        studentNameEntry.config(state = 'normal')
        studentNameEntry.delete(0, END)
        studentNameEntry.config(state = 'disabled')
        janVar.set('')
        febVar.set('')
        marVar.set('')
        aprVar.set('')
        mayVar.set('')
        junVar.set('')
        julVar.set('')
        augVar.set('')
        sepVar.set('')
        octVar.set('')
        novVar.set('')
        decVar.set('')


        db.commit()



    #----- WIDGETS -----
    studentIdLabel = Label(registerGui, text = 'Enter Student ID')
    studentIdEntry = Entry(registerGui)
    verifyButton = Button(registerGui, text = 'Verify Student', command = verifyStudent)
    studentNameLabel = Label(registerGui, text = 'Student Name')
    studentNameEntry = Entry(registerGui, state = 'disabled')
    yearVar = StringVar(registerGui)
    yearMenu = OptionMenu(registerGui, yearVar, '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024')
    infoLabel = Label(registerGui, text = 'Enter the no. of present days out of 25 working days')
    janLabel = Label(registerGui, text = "January")
    janVar = StringVar()
    janMenu = OptionMenu(registerGui, janVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    febLabel = Label(registerGui, text = "February")
    febVar = StringVar()
    febMenu = OptionMenu(registerGui, febVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    marLabel = Label(registerGui, text = "March")
    marVar = StringVar()
    marMenu = OptionMenu(registerGui, marVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    aprLabel = Label(registerGui, text = "April")
    aprVar = StringVar()
    aprMenu = OptionMenu(registerGui, aprVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    mayLabel = Label(registerGui, text = "May")
    mayVar = StringVar()
    mayMenu = OptionMenu(registerGui, mayVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    junLabel = Label(registerGui, text = "June")
    junVar = StringVar()
    junMenu = OptionMenu(registerGui, junVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    julLabel = Label(registerGui, text = "July")
    julVar = StringVar()
    julMenu = OptionMenu(registerGui, julVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    augLabel = Label(registerGui, text = "August")
    augVar = StringVar()
    augMenu = OptionMenu(registerGui, augVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    sepLabel = Label(registerGui, text = "September")
    sepVar = StringVar()
    sepMenu = OptionMenu(registerGui, sepVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    octLabel = Label(registerGui, text = "October")
    octVar = StringVar()
    octMenu = OptionMenu(registerGui, octVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    novLabel = Label(registerGui, text = "November")
    novVar = StringVar()
    novMenu = OptionMenu(registerGui, novVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    decLabel = Label(registerGui, text = "December")
    decVar = StringVar()
    decMenu = OptionMenu(registerGui, decVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')
    yearLabel = Label(registerGui, text = 'Year')
    yearEntry = Entry(registerGui)
    submitButton = Button(registerGui, text = 'Submit', command = check, height = 2, width = 15)


    #----- PLACING WIDGETS -----
    studentIdLabel.place(relx = 0.1, rely = 0.05)
    studentIdEntry.place(relx = 0.3, rely = 0.05)
    verifyButton.place(relx = 0.7, rely = 0.05)
    studentNameLabel.place(relx = 0.1, rely = 0.1)
    studentNameEntry.place(relx = 0.3, rely = 0.1)
    infoLabel.place(relx = 0.2, rely = 0.6)
    janLabel.place(relx = 0.15, rely = 0.25)
    janMenu.place(relx = 0.3, rely = 0.25, width = 100)
    febLabel.place(relx = 0.15, rely = 0.3)
    febMenu.place(relx = 0.3, rely = 0.3, width = 100)
    marLabel.place(relx = 0.15, rely = 0.35)
    marMenu.place(relx = 0.3, rely = 0.35, width = 100)
    aprLabel.place(relx = 0.15, rely = 0.4)
    aprMenu.place(relx = 0.3, rely = 0.4, width = 100)
    mayLabel.place(relx = 0.15, rely = 0.45)
    mayMenu.place(relx = 0.3, rely = 0.45, width = 100)
    junLabel.place(relx = 0.15, rely = 0.5)
    junMenu.place(relx = 0.3, rely = 0.5, width = 100)
    julLabel.place(relx = 0.55, rely = 0.25)
    julMenu.place(relx = 0.7, rely = 0.25, width = 100)
    augLabel.place(relx = 0.55, rely = 0.3)
    augMenu.place(relx = 0.7, rely = 0.3, width = 100)
    sepLabel.place(relx = 0.55, rely = 0.35)
    sepMenu.place(relx = 0.7, rely = 0.35, width = 100)
    octLabel.place(relx = 0.55, rely = 0.4)
    octMenu.place(relx = 0.7, rely = 0.4, width = 100)
    novLabel.place(relx = 0.55, rely = 0.45)
    novMenu.place(relx = 0.7, rely = 0.45, width = 100)
    decLabel.place(relx = 0.55, rely = 0.5)
    decMenu.place(relx = 0.7, rely = 0.5, width = 100)
    yearLabel.place(relx = 0.2, rely = 0.15)
    yearEntry.place(relx = 0.3, rely = 0.15) 
    submitButton.place(relx = 0.35, rely = 0.8) 



    #----- MAINLOOP -----
    registerGui.mainloop()






