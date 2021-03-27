from tkinter import *


#----- GUI -----
attendenceGui = Tk()
attendenceGui.geometry('500x500')
attendenceGui.resizable(0,0)
attendenceGui.title('Student Information')


#----- FUNCTIONS -----
def register():
    from attendence_register import registerGuiRun
    registerGuiRun()


def view():
    from attendence_view import viewGuiRun
    viewGuiRun()



    

#---- WIDGETS -----
registerButton = Button(attendenceGui, text = 'Register', width = 10, height = 2, command = register)
viewButton = Button(attendenceGui, text = 'View', width = 10, height = 2, command = view)
registerPhoto = PhotoImage(file = 'images/registerIcon.png')
registerLabel = Label(attendenceGui,image = registerPhoto)
viewPhoto = PhotoImage(file = 'images/viewIcon.png')
viewLabel = Label(attendenceGui,image = viewPhoto)



#----- PLACING WIDGETS -----
registerButton.place(relx = 0.25, rely = 0.5)
viewButton.place(relx = 0.6, rely = 0.5)
registerLabel.place(relx = 0.25, rely = 0.3)
viewLabel.place(relx = 0.6, rely = 0.3)


#----- MAINLOOP -----
attendenceGui.mainloop()
