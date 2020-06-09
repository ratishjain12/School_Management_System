from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Menu")
root.geometry("800x600")
root.config(bg = "yellow")
root.resizable(0,0)


#####Functions########
def quit_function():
    repsonse = messagebox.askquestion("Confirmation","Are you sure you want to quit?",icon = "warning")
    if repsonse == "yes":
        root.destroy()


frame = Frame(root,bg = "yellow")
frame.place(relx = 0.35,rely = 0.32)

Student_info = Button(frame,text = "Student-Info",font = "Helvetica 20 bold",width=20)
Student_info.grid(pady = 5)

Fee_status = Button(frame,text = "Fee - Status",font = "Helvetica 20 bold",width =20)
Fee_status.grid(pady = 5)

Gradebook = Button(frame,text = "Grade-book",font = "Helvetica 20 bold",width = 20)
Gradebook.grid(pady = 5)

Attendance = Button(frame,text = "Attendance",font = "Helvetica 20 bold",width = 20)
Attendance.grid(pady = 5)


quit = Button(frame,text = "Quit",font = "Helvetica 20 bold",width = 20 ,command = quit_function)
quit.grid(pady = 5)




root.mainloop()
