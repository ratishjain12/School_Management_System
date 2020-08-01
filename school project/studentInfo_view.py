from tkinter import *
from database import db, cursor
from tkinter import ttk
from tkinter import messagebox
import datetime, pdb

def viewGuiRun():
    #----- GUI -----
    viewGui = Toplevel()
    viewGui.title('View')
    viewGui.geometry('700x700')
    viewGui.resizable(0, 0)


    #----- FUNCTIONS -----
    def search():
        if searchEntry.get().strip() == '':
            messagebox.showerror('Student Info', 'Please enter a search parameter!')

        else:
            query = searchEntry.get().strip()
            display.delete(*display.get_children())
            if searchParameter.get().strip() == 'Student ID':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where studentId = %s'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid Student ID')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')

            elif searchParameter.get().strip() == 'Roll No':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where rollno = %s'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid Roll No')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')

            elif searchParameter.get().strip() == 'Firstname':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where firstname = "%s"'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid name')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')


            elif searchParameter.get().strip() == 'Lastname':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where lastname = "%s"'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid name')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')


            elif searchParameter.get().strip() == 'Class':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where std = "%s"'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a class')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')





    def expand():

        data = display.focus()
        if len(data) == 0:
            messagebox.showerror("Student Info", "No field selected")

        else:
            data = display.item(data)

            studentId = data['values'][0]

            openGui = Toplevel()
            openGui.title('Student Details')
            openGui.geometry('800x500')
            openGui.resizable(0,0)


            #----- FUCNTIONS -----
            def back():
                openGui.withdraw()




            #----- WIDGETS -----
            infoLabel = Label(openGui, text = "Student Details")
            studentIdLabel = Label(openGui, text = 'Student ID')
            studentIdEntry = Entry(openGui)
            nameLabel = Label(openGui, text = 'Name')
            nameEntry = Entry(openGui)
            addressLabel = Label(openGui, text = 'Address')
            addressEntry = Entry(openGui)
            dobLabel = Label(openGui, text = 'DOB')
            dobEntry = Entry(openGui)
            genderLabel = Label(openGui, text = 'Gender')
            genderEntry = Entry(openGui)
            fatherNameLabel = Label(openGui, text = "Father's Name")
            fatherNameEntry = Entry(openGui)
            fatherNoLabel = Label(openGui, text = "Father's No.")
            fatherNoEntry = Entry(openGui)
            fatherProfessionLabel = Label(openGui, text = "Father's Profession")
            fatherProfessionEntry = Entry(openGui)
            motherNameLabel = Label(openGui, text = "Mother's Name")
            motherNameEntry = Entry(openGui)
            motherNoLabel = Label(openGui, text = "Mother's No.")
            motherNoEntry = Entry(openGui)
            motherProfessionLabel = Label(openGui, text = "Mother's Profession")
            motherProfessionEntry = Entry(openGui)
            stdLabel = Label(openGui, text = 'Class')
            stdEntry = Entry(openGui)
            sectionLabel = Label(openGui, text = 'Section')
            sectionEntry = Entry(openGui)
            rollnoLabel = Label(openGui, text = 'Roll No.')
            rollnoEntry = Entry(openGui)
            backButton = Button(openGui, text = "Go Back", command = back, height = 2, width = 20)



            #----- PLACING WIDGETS -----
            infoLabel.place(relx = 0.45, rely = 0.0175)

            studentIdLabel.place(relx = 0.05, rely = 0.1)
            studentIdEntry.place(relx = 0.25, rely = 0.1)
            nameLabel.place(relx = 0.05, rely = 0.2)
            nameEntry.place(relx = 0.25, rely = 0.2)
            stdLabel.place(relx = 0.05, rely = 0.3)
            stdEntry.place(relx = 0.25, rely = 0.3)
            rollnoLabel.place(relx = 0.05, rely = 0.4)
            rollnoEntry.place(relx = 0.25, rely = 0.4)


            fatherNameLabel.place(relx = 0.05, rely = 0.55)
            fatherNameEntry.place(relx = 0.25, rely = 0.55)
            fatherNoLabel.place(relx = 0.05, rely = 0.65)
            fatherNoEntry.place(relx = 0.25, rely = 0.65)
            fatherProfessionLabel.place(relx = 0.05, rely = 0.75)
            fatherProfessionEntry.place(relx = 0.25, rely = 0.75)

            motherNameLabel.place(relx = 0.525, rely = 0.55)
            motherNameEntry.place(relx = 0.725, rely = 0.55)
            motherNoLabel.place(relx = 0.525, rely = 0.65)
            motherNoEntry.place(relx = 0.725, rely = 0.65)
            motherProfessionLabel.place(relx = 0.525, rely = 0.75)
            motherProfessionEntry.place(relx = 0.725, rely = 0.75)
            

            addressLabel.place(relx = 0.525, rely = 0.1)
            addressEntry.place(relx = 0.725, rely = 0.1)
            dobLabel.place(relx = 0.525, rely = 0.2)
            dobEntry.place(relx = 0.725, rely = 0.2)
            genderLabel.place(relx = 0.525, rely = 0.3)
            genderEntry.place(relx = 0.725, rely = 0.3)
            sectionLabel.place(relx = 0.525, rely = 0.4)
            sectionEntry.place(relx = 0.725, rely = 0.4)


            backButton.place(relx = 0.4, rely = 0.9)

            #----- ADDING DATA -----
            cursor.execute('use school')
            cursor.execute('select * from studentdata, parentinfo where studentdata.studentId = %s'%(studentId))
            data = cursor.fetchall()
            field = data[0]
            # [(1, 'Gautam', 'Zanzmera', 18, '12', 'A', 'M', '123, ABC', datetime.date(2002, 6, 4),
                # 1,'Mahendra', 4363577, 'Business', 'Urvi', 56745876, 'Housewife')]

            name = field[1] + ' ' + field[2]
            rollno = field[3]
            std = field[4]
            section = field[5]
            gender = field[6]
            address = field[7]
            dob = field[8]
            fatherName = field[10]
            fatherNo = field[11]
            fatherProfession = field[12]
            motherName = field[13]
            motherNo = field[14]
            motherProfession = field[15]


            studentIdEntry.insert(0, studentId)
            studentIdEntry.config(state = 'disabled', disabledforeground  = 'black')
            genderEntry.insert(0, gender)
            genderEntry.config(state = 'disabled', disabledforeground  = 'black')
            nameEntry.insert(0, name)
            nameEntry.config(state = 'disabled', disabledforeground  = 'black')
            rollnoEntry.insert(0, rollno)
            rollnoEntry.config(state = 'disabled', disabledforeground  = 'black')
            stdEntry.insert(0, std)
            stdEntry.config(state = 'disabled', disabledforeground  = 'black')
            sectionEntry.insert(0, section)
            sectionEntry.config(state = 'disabled', disabledforeground  = 'black')
            addressEntry.insert(0, address)
            addressEntry.config(state = 'disabled', disabledforeground  = 'black')
            dobEntry.insert(0, dob)
            dobEntry.config(state = 'disabled', disabledforeground  = 'black')
            fatherNameEntry.insert(0, fatherName)
            fatherNameEntry.config(state = 'disabled', disabledforeground  = 'black')
            fatherNoEntry.insert(0, fatherNo)
            fatherNoEntry.config(state = 'disabled', disabledforeground  = 'black')
            fatherProfessionEntry.insert(0, fatherProfession)
            fatherProfessionEntry.config(state = 'disabled', disabledforeground  = 'black')
            motherNameEntry.insert(0, motherName)
            motherNameEntry.config(state = 'disabled', disabledforeground  = 'black')
            motherNoEntry.insert(0, motherNo)
            motherNoEntry.config(state = 'disabled', disabledforeground  = 'black')
            motherProfessionEntry.insert(0, motherProfession)
            motherProfessionEntry.config(state = 'disabled', disabledforeground  = 'black')




            #----- MAINLOOP -----
            openGui.mainloop()


    def update():
        data = display.focus()
        if len(data) == 0:
            messagebox.showerror("Student Info", "No field selected")

        else:
            data = display.item(data)

            studentId = data['values'][0]

            updateGui = Toplevel()
            updateGui.title('Student Details')
            updateGui.geometry('800x500')
            updateGui.resizable(0,0)



            infoLabel = Label(updateGui, text = "Student Details")
            studentIdLabel = Label(updateGui, text = 'Student ID')
            studentIdEntry = Entry(updateGui)
            nameLabel = Label(updateGui, text = 'Name')
            nameEntry = Entry(updateGui)
            addressLabel = Label(updateGui, text = 'Address')
            addressEntry = Entry(updateGui)
            dobLabel = Label(updateGui, text = 'DOB')
            dobEntry = Entry(updateGui)
            genderLabel = Label(updateGui, text = 'Gender')
            genderEntry = Entry(updateGui)
            fatherNameLabel = Label(updateGui, text = "Father's Name")
            fatherNameEntry = Entry(updateGui)
            fatherNoLabel = Label(updateGui, text = "Father's No.")
            fatherNoEntry = Entry(updateGui)
            fatherProfessionLabel = Label(updateGui, text = "Father's Profession")
            fatherProfessionEntry = Entry(updateGui)
            motherNameLabel = Label(updateGui, text = "Mother's Name")
            motherNameEntry = Entry(updateGui)
            motherNoLabel = Label(updateGui, text = "Mother's No.")
            motherNoEntry = Entry(updateGui)
            motherProfessionLabel = Label(updateGui, text = "Mother's Profession")
            motherProfessionEntry = Entry(updateGui)
            stdLabel = Label(updateGui, text = 'Class')
            stdEntry = Entry(updateGui)
            sectionLabel = Label(updateGui, text = 'Section')
            sectionEntry = Entry(updateGui)
            rollnoLabel = Label(updateGui, text = 'Roll No.')
            rollnoEntry = Entry(updateGui)

            #----- ADDING DATA -----
            cursor.execute('use school')
            cursor.execute('select * from studentdata, parentinfo where studentdata.studentId = %s'%(studentId))
            data = cursor.fetchall()
            field = data[0]
            # [(1, 'Gautam', 'Zanzmera', 18, '12', 'A', 'M', '123, ABC', datetime.date(2002, 6, 4),
                # 1,'Mahendra', 4363577, 'Business', 'Urvi', 56745876, 'Housewife')]

            name = field[1] + ' ' + field[2]
            rollno = str(field[3])
            std = field[4]
            section = field[5]
            gender = field[6]
            address = field[7]
            dob = field[8]
            dob = datetime.datetime.strftime(dob, "%Y-%m-%d")
            fatherName = field[10]
            fatherNo = str(field[11])
            fatherProfession = field[12]
            motherName = field[13]
            motherNo = str(field[14])
            motherProfession = field[15]


            studentIdEntry.insert(0, studentId)
            genderEntry.insert(0, gender)
            nameEntry.insert(0, name)
            rollnoEntry.insert(0, rollno)
            stdEntry.insert(0, std)
            sectionEntry.insert(0, section)
            addressEntry.insert(0, address)
            dobEntry.insert(0, dob)
            fatherNameEntry.insert(0, fatherName)
            fatherNoEntry.insert(0, fatherNo)
            fatherProfessionEntry.insert(0, fatherProfession)
            motherNameEntry.insert(0, motherName)
            motherNoEntry.insert(0, motherNo)
            motherProfessionEntry.insert(0, motherProfession)

            studentdataEntries = [nameEntry, rollnoEntry, stdEntry,
                                 sectionEntry, genderEntry, addressEntry, dobEntry]
            studentdataValues = [name, rollno, std, section, gender, address, dob]
            studentdata = ['name', 'rollno', 'std', 'section', 'gender', 'address', 'dob']

            parentinfoValues = [fatherName, fatherNo, fatherProfession,
                          motherName, motherNo, motherProfession]

            parentinfo = ['fatherName', 'fatherNo', 'fatherProfession',
                          'motherName', 'motherNo', 'motherProfession']

            parentinfoEntries = [fatherNameEntry, fatherNoEntry, fatherProfessionEntry,
                          motherNameEntry, motherNoEntry, motherProfessionEntry]

            
            #----- FUCNTIONS -----
            def submit():
                errors = 0
                for i in range(len(studentdata)):
                    
                    if studentdataEntries[i].get() != studentdataValues[i]:
                        try:
                            cursor.execute('update studentdata set %s = %s where studentId = %s'%(studentdata[i], studentdataEntries[i].get(), studentId))

                        except:
                            messagebox.showerror('Student Info', 'Invalid input')
                            errors += 1

                for i in range(len(parentinfo)):
                    
                    if parentinfoEntries[i].get() != parentinfoValues[i]:
                        try:
                            cursor.execute('update parentinfo set %s = %s where studentId = %s'%(parentinfo[i], parentinfoEntries[i].get(), studentId))
                        except:
                            messagebox.showerror('Student Info', 'Invalid input')
                            errors += 1

                db.commit()
                if errors == 0:
                    messagebox.showinfo('Student Info', 'Data successfully updated!')
                    

                

            


            #----- WIDGETS -----
            
            submitButton = Button(updateGui, text = "Submit", command = submit, height = 2, width = 20)








            #----- PLACING WIDGETS -----
            infoLabel.place(relx = 0.45, rely = 0.0175)

            studentIdLabel.place(relx = 0.05, rely = 0.1)
            studentIdEntry.place(relx = 0.25, rely = 0.1)
            nameLabel.place(relx = 0.05, rely = 0.2)
            nameEntry.place(relx = 0.25, rely = 0.2)
            stdLabel.place(relx = 0.05, rely = 0.3)
            stdEntry.place(relx = 0.25, rely = 0.3)
            rollnoLabel.place(relx = 0.05, rely = 0.4)
            rollnoEntry.place(relx = 0.25, rely = 0.4)


            fatherNameLabel.place(relx = 0.05, rely = 0.55)
            fatherNameEntry.place(relx = 0.25, rely = 0.55)
            fatherNoLabel.place(relx = 0.05, rely = 0.65)
            fatherNoEntry.place(relx = 0.25, rely = 0.65)
            fatherProfessionLabel.place(relx = 0.05, rely = 0.75)
            fatherProfessionEntry.place(relx = 0.25, rely = 0.75)

            motherNameLabel.place(relx = 0.525, rely = 0.55)
            motherNameEntry.place(relx = 0.725, rely = 0.55)
            motherNoLabel.place(relx = 0.525, rely = 0.65)
            motherNoEntry.place(relx = 0.725, rely = 0.65)
            motherProfessionLabel.place(relx = 0.525, rely = 0.75)
            motherProfessionEntry.place(relx = 0.725, rely = 0.75)
            

            addressLabel.place(relx = 0.525, rely = 0.1)
            addressEntry.place(relx = 0.725, rely = 0.1)
            dobLabel.place(relx = 0.525, rely = 0.2)
            dobEntry.place(relx = 0.725, rely = 0.2)
            genderLabel.place(relx = 0.525, rely = 0.3)
            genderEntry.place(relx = 0.725, rely = 0.3)
            sectionLabel.place(relx = 0.525, rely = 0.4)
            sectionEntry.place(relx = 0.725, rely = 0.4)


            submitButton.place(relx = 0.4, rely = 0.9)

            




            #----- MAINLOOP -----
            updateGui.mainloop()




    #----- WIDGETS -----
    viewByLabel = Label(viewGui, text = "View By", font = 'Helvetica 16 bold')
    searchParameter = StringVar()
    searchParameter.set("Student ID")
    searchBy = OptionMenu(viewGui, searchParameter, "Student ID", "Roll No", "Firstname", "Lastname", "Class")
    searchBy.config(width = 10)
    searchLabel = Label(viewGui, text = "Search Here:")
    searchEntry = Entry(viewGui, width = 30)
    searchButton = Button(viewGui, text = "Search", width = 10, command  = search)
    deleteButton = Button(viewGui, text = "Delete", height = 2, width = 15)
    updateButton = Button(viewGui, text = 'Update', height = 2, width = 15, command = update)
    openButton = Button(viewGui, text  = 'Open', height = 2, width = 15, command = expand)

    display = ttk.Treeview(viewGui, selectmode = "browse", height = 25)
    scrlbar = ttk.Scrollbar(viewGui, orient = 'vertical', command = display.yview)
    display.configure(xscrollcommand = scrlbar.set)

    display['columns'] = ('studentId', 'name', 'class', 'rollno', 'gender')
    display['show'] = 'headings'
    display.heading('studentId', text = 'Student ID')
    display.heading('name', text = 'Name')
    display.heading('class', text = 'Class')
    display.heading('rollno', text = 'Roll no.')
    display.heading('gender', text = 'Gender')

    display.column('studentId', anchor = 'c', width = 100 )
    display.column('name', anchor = 'c', width = 200 )
    display.column('class', anchor = 'c', width = 100)
    display.column('rollno', anchor = 'c', width = 100)
    display.column('gender', anchor = 'c', width = 100)


    #----- PLACING WIDGETS -----

    viewByLabel.place(relx = 0.13, rely = 0.095)
    searchBy.place(relx  = 0.26, rely = 0.095)
    searchEntry.place(relx = 0.44, rely = 0.1)
    searchButton.place(relx = 0.73, rely = 0.1)
    display.place(relx = 0.0715, rely = 0.2)
    scrlbar.pack(side = 'right', fill = 'x')
    openButton.place(relx = 0.1, rely = 0.9)
    updateButton.place(relx = 0.425, rely = 0.9)
    deleteButton.place(relx = 0.745, rely = 0.9)





    #----- MAINLOOP -----
    viewGui.mainloop()
