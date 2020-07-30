from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database import *


fee_window = Toplevel()
fee_window.geometry('500x400')
fee_window.title('Fee-Status')
fee_window.resizable(0,0)
def check():
    student_id = stid_ent.get()
    student_name = name_ent.get()
    

    if student_id == '' or student_name == '':
        messagebox.showwarning('ERROR','Please fill the details')
    else:
        cursor.execute('select status from feeStatus where studentId = "%s"'%(student_id))
        status_data = cursor.fetchall()
        cursor.execute('select firstname from studentdata where firstname="%s" and studentId="%s"'%(student_name,student_id))
        name_data= cursor.fetchall()
        if status_data != [] and name_data != []:
            print(status_data)
            for i in status_data[0]:
                status = i
                print(i)
            if i == 'paid':
                result = Label(check_individual_window,text = "Fee has been sumbitted by  -"+" "+name_ent.get(),height=2,foreground="black",font='Helvetica 20 bold')
                result.place(relx = 0.21,rely = 0.9)
                result.after(3000,result.destroy)
            else:
                result = Label(check_individual_window,text = "Fee has not been sumbitted by  -"+" "+name_ent.get(),height=2,foreground="black",font='Helvetica 20 bold')
                result.place(relx = 0.21,rely = 0.9)
                result.after(3000,result.destroy)
        else:
            result = Label(check_individual_window,text = "Make sure you are giving correct id and Name!",height=2,foreground="black",font='Helvetica 20 bold')
            result.place(relx = 0.16,rely = 0.9)
            result.after(3000,result.destroy)
            
def back():
    check_individual_window.withdraw()
    fee_window.deiconify()
def back0():
    fee_window.withdraw()
    from menu import root
def back1():
    pending_window.withdraw()
    fee_window.deiconify()

def back2():
    payment_window.withdraw()
    fee_window.deiconify()
            
  

def check_individual():
    global check_individual_window
    global name_ent
    global stid_ent
    fee_window.withdraw()
    check_individual_window = Toplevel(fee_window)
    check_individual_window.geometry('600x700')
    check_individual_window.title('Fee - Status')
    check_individual_window.resizable(0,0)
    
    frame= Frame(check_individual_window,height = 700)
    frame.place(relx=0.14,rely = 0.3)

    stid_lbl = Label(frame,text = "Enter Student Id:",font = "Helvetica 20 bold")
    stid_lbl.grid(pady = 5)

    stid_ent = Entry(frame)
    stid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

    name_lbl = Label(frame,text = "Enter Student FirstName:",font = "Helvetica 20 bold")
    name_lbl.grid(pady = 30)

    name_ent = Entry(frame)
    name_ent.grid(row = 1,column = 1,padx = 3,pady = 30)

    check_button = Button(check_individual_window,text = 'CHECK',width=40,height=2,command=check,font='Sans-serif 15 bold')
    check_button.place(relx = 0.14, rely=0.5)

    back_button = Button(check_individual_window,text = 'BACK',width=10,height=2,command=back,font='Sans-serif 15 bold')
    back_button.place(relx = 0.03)

def pending():
    fee_window.withdraw()
    global pending_window
    pending_window = Toplevel(fee_window)
    pending_window.title('pending-list')
    pending_window.geometry('700x700')
    pending_window.resizable(0,0)

    table = ttk.Treeview(pending_window,selectmode='browse',height = 25)
    table.place(relx = 0.0715, rely = 0.2)
    
    
    scrlbar = ttk.Scrollbar(pending_window, orient = 'vertical', command = table.yview)
    scrlbar.pack(side = 'right', fill = 'x')
    table.configure(xscrollcommand = scrlbar.set)
    
    table['columns']=('studentId','name','class','section','status')
    table['show']='headings'
    table.heading('studentId',text = 'Student ID')
    table.heading('name',text = 'Name')
    table.heading('class',text = 'Class')
    table.heading('section',text = 'Section')
    table.heading('status',text = 'Status')

    table.column('studentId', anchor = 'c', width = 100)
    table.column('name', anchor = 'c', width = 200)
    table.column('class', anchor = 'c', width = 100)
    table.column('section', anchor = 'c', width = 100)
    table.column('status', anchor = 'c', width = 100)
    
    cursor.execute("select studentdata.studentId ,firstname,lastname,std,section,feeStatus.status from studentdata,feeStatus where feeStatus.status='pending'")
    data = cursor.fetchall()
    print(data)
    for x in data:
        Id = x[0]
        name = x[1]+''+x[2]
        std = x[3]
        section = x[4]
        status = x[5]
        table.insert('',END,values = (Id,name,std,section,status))

    back_button = Button(pending_window,text = 'BACK',width=10,height=2,command=back1,font='Sans-serif 15 bold')
    back_button.place(relx = 0.03)

def payment():
    student_id = stid_ent.get()
    student_name = name_ent.get()
    if student_id == '' or student_name == '':
        messagebox.showwarning('Error','please fill all details')
    else:
        cursor.execute('select firstname from studentdata where firstname="%s" and studentId="%s"'%(student_name,student_id))
        data = cursor.fetchall()
        print(data)
        if data !=[]:
            cursor.execute("update feeStatus set status = 'paid' where studentId = %s"%(student_id))
            result = Label(payment_window,text = "Payment successfull!!",height=2,foreground="green",font='Helvetica 20 bold')
            result.place(relx = 0.1,rely = 0.9)
            result.after(3000,result.destroy)
        else:
            messagebox.showwarning('Error','Please enter correct id and name of student')
        
        
    

def make_payment():
    fee_window.withdraw()
    global payment_window
    global stid_ent
    global name_ent
    
    payment_window = Toplevel(fee_window)
    payment_window.title('Payment')
    payment_window.geometry('500x600')
    payment_window.resizable(0,0)

    frame = Frame(payment_window)
    frame.place(relx=0.08,rely = 0.3)

    stid_lbl = Label(frame,text = "Enter Student Id:",font = "Helvetica 20 bold")
    stid_lbl.grid(pady = 5)

    stid_ent = Entry(frame)
    stid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

    name_lbl = Label(frame,text = "Enter Student FirstName:",font = "Helvetica 20 bold")
    name_lbl.grid(pady = 30)

    name_ent = Entry(frame)
    name_ent.grid(row = 1,column = 1,padx = 3,pady = 30)

    payment_button = Button(payment_window,text = 'Make Payment',width=40,height=2,command=payment,font='Sans-serif 15 bold')
    payment_button.place(relx = 0.09, rely=0.5)

    back_button = Button(payment_window,text = 'BACK',width=10,height=2,command=back2,font='Sans-serif 15 bold')
    back_button.place(relx = 0.02)
    

frame = Frame(fee_window)
frame.place(relx = 0.25, rely = 0.3)


#--------Buttons---------#
check_individual = Button(frame,text = 'Check for a student',width=20, font = 'Helvetica 20 bold',command = check_individual)
check_individual.grid(pady=4)

Pending = Button(frame,text = 'pending list',width=20, font = 'Helvetica 20 bold',command= pending)
Pending.grid(pady=4)

make_payment = Button(frame,text = 'Make Payment',width=20, font = 'Helvetica 20 bold',command= make_payment)
make_payment.grid(pady=4)

back_button = Button(fee_window,text = 'BACK',width=10,height=2,command=back0,font='Sans-serif 15 bold')
back_button.place(relx = 0.03)


fee_window.mainloop()

