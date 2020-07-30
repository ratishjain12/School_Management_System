from tkinter import *
from database import db,cursor
from tkinter import messagebox


def viewGuiRun():

	#----- GUI -----
    viewGui = Toplevel()
    viewGui.title('Register')
    viewGui.geometry('600x600')
    viewGui.resizable(0,0)


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
    		studentNameEntry.config()


    	else:
    		messagebox.showerror('Attendence', 'No data found')


    def get():
    	if studentIdEntry.get().strip() == '':
    		messagebox.showerror('Attendence', 'Please enter a Student ID')

    	elif yearEntry.get().strip() == '':
    		messagebox.showerror('Attendence', 'Please enter a year')

    	else:	
    		verifyStudent()
    		studentId = studentIdEntry.get().strip()
    		year = yearEntry.get().strip()

    		try:
    			cursor.execute('select * from attendence where studentId = %s and year = %s'%(studentId, year))
    		except:
    			messagebox.showerror('Attendence', 'No data found')


    		data = cursor.fetchall()
    		if len(data) != 0:
	    		field = data[0]
	    		jan = field[2]
	    		feb = field[3]
	    		mar = field[4]
	    		apr = field[5]
	    		may = field[6]
	    		jun = field[7]
	    		jul = field[8]
	    		aug = field[9]
	    		sep = field[10]
	    		octo = field[11]
	    		nov = field[12]
	    		dec = field[13]
	    		total = jan + feb + mar + apr + may + jun + jul + aug + sep + nov + octo + nov + dec
	    		percent = str(total/3) + '%'


	    		if len(janEntry.get().strip()) != 0:

	    			janEntry.config(state = 'normal')
	    			febEntry.config(state = 'normal')
	    			marEntry.config(state = 'normal')
	    			aprEntry.config(state = 'normal')
	    			mayEntry.config(state = 'normal')
	    			junEntry.config(state = 'normal')
	    			julEntry.config(state = 'normal')
	    			augEntry.config(state = 'normal')
	    			sepEntry.config(state = 'normal')
	    			octEntry.config(state = 'normal')
	    			novEntry.config(state = 'normal')
	    			decEntry.config(state = 'normal')
	    			totalEntry.config(state = 'normal')
	    			percentEntry.config(state = 'normal')

		    		janEntry.delete(0, END)
		    		febEntry.delete(0, END)
		    		marEntry.delete(0, END)
		    		aprEntry.delete(0, END)
		    		mayEntry.delete(0, END)
		    		junEntry.delete(0, END)
		    		julEntry.delete(0, END)
		    		augEntry.delete(0, END)
		    		sepEntry.delete(0, END)
		    		octEntry.delete(0, END)
		    		novEntry.delete(0, END)
		    		decEntry.delete(0, END)
		    		totalEntry.delete(0, END)
		    		percentEntry.delete(0, END)


	    		janEntry.insert(0, jan)
	    		janEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		febEntry.insert(0, feb)
	    		febEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		marEntry.insert(0, mar)
	    		marEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		aprEntry.insert(0, apr)
	    		aprEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		mayEntry.insert(0, may)
	    		mayEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		junEntry.insert(0, jun)
	    		junEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		julEntry.insert(0, jul)
	    		julEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		augEntry.insert(0, aug)
	    		augEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		sepEntry.insert(0, sep)
	    		sepEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		octEntry.insert(0, octo)
	    		octEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		novEntry.insert(0, nov)
	    		novEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		decEntry.insert(0, dec)
	    		decEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		totalEntry.insert(0 , total)
	    		totalEntry.config(state = 'disabled', disabledforeground  = 'black')
	    		percentEntry.insert(0 , percent)
	    		percentEntry.config(state = 'disabled', disabledforeground  = 'black')





	    	else:
	    		messagebox.showerror('Attendence', 'No data found')



    def graph():
    	import matplotlib.pyplot as plt
    	import numpy

    	if len(janEntry.get().strip()) == 0:
    		messagebox.showerror('Attendence', 'Please get the values first')
    	
    	else:
    		jan = janEntry.get().strip()
    		feb = febEntry.get().strip()
    		mar = marEntry.get().strip()
    		apr = aprEntry.get().strip()
    		may = mayEntry.get().strip()
    		jun = junEntry.get().strip()
    		jul = julEntry.get().strip()
    		aug = augEntry.get().strip()
    		sep = sepEntry.get().strip()
    		octo = octEntry.get().strip()
    		nov = novEntry.get().strip()
    		dec = decEntry.get().strip()
    		studentId = studentIdEntry.get().strip()
    		year = yearEntry.get().strip()
    		name = studentNameEntry.get().strip()
    		months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    		values = [float(jan), float(feb), float(mar), float(apr), float(may), float(jun), float(jul), float(aug), float(sep), float(octo), float(nov), float(dec)]
    		#xlim = numpy.array(list(range(1,26)))
    		#ylim = numpy.array(list(range(1,13)))
    		#print(xlim, ylim)
    		#
    		print(name)
    		plt.suptitle('Attendence - ' + name + ' - ' + year)
    		#plt.xticks(list(range(0, 12)))
    		#plt.yticks(list(range(0, 25)))
    		plt.bar(months, values)
    		plt.xlabel('Months')
    		plt.ylabel('Present Days')
    		plt.show()





    #----- WIDGETS -----
    studentIdLabel = Label(viewGui, text = 'Enter Student ID')
    studentIdEntry = Entry(viewGui)
    verifyButton = Button(viewGui, text = 'Verify Student', command = verifyStudent)
    studentNameLabel = Label(viewGui, text = 'Student Name')
    studentNameEntry = Entry(viewGui, state = 'disabled')
    yearLabel = Label(viewGui, text = 'Year')
    yearEntry = Entry(viewGui)
    janLabel = Label(viewGui, text = "January")
    janEntry = Entry(viewGui)
    febLabel = Label(viewGui, text = "February")
    febEntry = Entry(viewGui)
    marLabel = Label(viewGui, text = "March")
    marEntry = Entry(viewGui)
    aprLabel = Label(viewGui, text = "April")
    aprEntry = Entry(viewGui)
    mayLabel = Label(viewGui, text = "May")
    mayEntry = Entry(viewGui)
    junLabel = Label(viewGui, text = "June")
    junEntry = Entry(viewGui)
    julLabel = Label(viewGui, text = "July")
    julEntry = Entry(viewGui)
    augLabel = Label(viewGui, text = "August")
    augEntry = Entry(viewGui)
    sepLabel = Label(viewGui, text = "September")
    sepEntry = Entry(viewGui)
    octLabel = Label(viewGui, text = "October")
    octEntry = Entry(viewGui)
    novLabel = Label(viewGui, text = "November")
    novEntry = Entry(viewGui)
    decLabel = Label(viewGui, text = "December")
    decEntry = Entry(viewGui)
    totalLabel = Label(viewGui, text = "Total")
    totalEntry = Entry(viewGui, width = 10)
    percentLabel = Label(viewGui, text = "Percent")
    percentEntry = Entry(viewGui, width = 10)
    getButton = Button(viewGui, text = 'Get', command = get, width = 15, height = 2)
    graphButton = Button(viewGui, text = 'See Graphs', command = graph, width = 15, height = 2)



    #----- PLACING WIDGETS -----
    studentIdLabel.place(relx = 0.1, rely = 0.05)
    studentIdEntry.place(relx = 0.3, rely = 0.05)
    verifyButton.place(relx = 0.7, rely = 0.05)
    studentNameLabel.place(relx = 0.1, rely = 0.1)
    studentNameEntry.place(relx = 0.3, rely = 0.1)
    janLabel.place(relx = 0.15, rely = 0.25)
    janEntry.place(relx = 0.3, rely = 0.25, width = 100)
    febLabel.place(relx = 0.15, rely = 0.325)
    febEntry.place(relx = 0.3, rely = 0.325, width = 100)
    marLabel.place(relx = 0.15, rely = 0.4)
    marEntry.place(relx = 0.3, rely = 0.4, width = 100)
    aprLabel.place(relx = 0.15, rely = 0.475)
    aprEntry.place(relx = 0.3, rely = 0.475, width = 100)
    mayLabel.place(relx = 0.15, rely = 0.55)
    mayEntry.place(relx = 0.3, rely = 0.55, width = 100)
    junLabel.place(relx = 0.15, rely = 0.625)
    junEntry.place(relx = 0.3, rely = 0.625, width = 100)
    julLabel.place(relx = 0.55, rely = 0.25)
    julEntry.place(relx = 0.7, rely = 0.25, width = 100)
    augLabel.place(relx = 0.55, rely = 0.325)
    augEntry.place(relx = 0.7, rely = 0.325, width = 100)
    sepLabel.place(relx = 0.55, rely = 0.4)
    sepEntry.place(relx = 0.7, rely = 0.4, width = 100)
    octLabel.place(relx = 0.55, rely = 0.475)
    octEntry.place(relx = 0.7, rely = 0.475, width = 100)
    novLabel.place(relx = 0.55, rely = 0.55)
    novEntry.place(relx = 0.7, rely = 0.55, width = 100)
    decLabel.place(relx = 0.55, rely = 0.625)
    decEntry.place(relx = 0.7, rely = 0.625, width = 100)
    totalLabel.place(relx = 0.15, rely = 0.7)
    totalEntry.place(relx = 0.3, rely = 0.7)
    percentLabel.place(relx = 0.55, rely = 0.7)
    percentEntry.place(relx = 0.7, rely = 0.7)
    yearLabel.place(relx = 0.2, rely = 0.15)
    yearEntry.place(relx = 0.3, rely = 0.15) 
    getButton.place(relx = 0.2, rely = 0.85)
    graphButton.place(relx = 0.55, rely = 0.85)



    #----- MAINLOOP -----
    viewGui.mainloop()