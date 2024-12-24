from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


root = Tk()

root.geometry('400x300+400+300')
root.title("Employee System")
connection = mysql.connect(host='localhost',database='db1',user='root',password='Pavankumar143')

def add_employee():
    add_gui=Tk()
    add_gui.geometry('300x200+300+200')
    add_gui.title('Add Employee')

    label1=Label(add_gui,text="EmpId",font=('Arial',14))
    label1.grid(row=1,column=1,pady=5)
    entry1=Entry(add_gui,font=('Arial',14),justify='center')
    entry1.grid(row=1,column=2,pady=5,padx=5)

    label2=Label(add_gui,text="Name",font=('Arial',14))
    label2.grid(row=2,column=1,pady=5)
    entry2=Entry(add_gui,font=('Arial',14),justify='center')
    entry2.grid(row=2,column=2,pady=5)

    label3=Label(add_gui,text='Job',font=('Arial',14))
    label3.grid(row=3,column=1,pady=5)
    entry3=Entry(add_gui,font=('Arial',14),justify='center')
    entry3.grid(row=3,column=2,pady=5)

    label4=Label(add_gui,text="Salary",font=('Arial',14))
    label4.grid(row=4,column=1,pady=5)
    entry4=Entry(add_gui,font=('Arial',14),justify='center')
    entry4.grid(row=4,column=2,pady=5)
    
    def add():
        eid=int(entry1.get())
        ename=entry2.get()
        j=entry3.get()
        sal=float(entry4.get())
        c=connection.cursor()
        try:
            c.execute("INSERT into Emp values (%s,%s,%s,%s)",params=(eid,ename,j,sal))
            messagebox.showinfo(title="Info",message="Employee Added")
            entry1.delete(0,END)
            entry2.delete(0,END)
            entry3.delete(0,END)
            entry4.delete(0,END)
            connection.commit()
        
        except:
            messagebox.showerror(title="Error",message="EmpId alrealy exits.")

    btn_add=Button(add_gui,text="Add",font=("Arial",14),command=add)
    btn_add.grid(row=5,column=1,pady=5)
    btn_exit=Button(add_gui,text="Exit",font=("Arial",14),command=lambda :add_gui.destroy())
    btn_exit.grid(row=5,column=2,pady=5)
  

    add_gui.config(bg='cyan')
    add_gui.mainloop()

def update_employee():
    update_gui=Tk()
    update_gui.geometry('350x150+200+100')
    update_gui.title("Update Employee")

    label1=Label(update_gui,text="EmpId",font=('Arial',14))
    label1.grid(row=1,column=1,pady=10)
    entry1=Entry(update_gui,font=('Arial',14),justify='center')
    entry1.grid(row=1,column=2,pady=10,padx=5)

    label2=Label(update_gui,text="Salary",font=('Arial',14))
    label2.grid(row=2,column=1,pady=5)
    entry2=Entry(update_gui,font=('Arial',14),justify='center')
    entry2.grid(row=2,column=2,pady=10)

    def update():
        eid=int(entry1.get())
        sal=float(entry2.get())
        c=connection.cursor()
        c.execute('UPDATE Emp set salary=%s where empId=%s',params=(sal,eid))
        k=c.rowcount
        if k>0:
            messagebox.showinfo(title="Info",message="Salary Updated")
            entry1.delete(0,END)
            entry2.delete(0,END)
            connection.commit()
        else:  
            messagebox.showerror(title="Error",message="Invalid EmpId")
        
        

    btn_update=Button(update_gui,text='Update',font=('Arial',14),command=update)
    btn_update.grid(row=3,column=1,pady=10,padx=10)
    btn_exit=Button(update_gui,text='Exit',font=('Arial',14),command=lambda :update_gui.destroy())
    btn_exit.grid(row=3,column=2,pady=10,padx=10)

    update_gui.config(bg='cyan')
    update_gui.mainloop()

def delete_employee():
    delete_gui=Tk()
    delete_gui.geometry('300x100+200+100')
    delete_gui.title('Delete Employee')

    label1=Label(delete_gui,text='EmpId',font=('Arial',14))
    label1.grid(row=1,column=1,pady=10)
    entry1=Entry(delete_gui,font=('Arial',14),justify='center')
    entry1.grid(row=1,column=2,pady=10)

    def emp_delete():
        eid=int(entry1.get())
        c=connection.cursor()
        try:
            c.execute('delete from Emp where empId=%s',params=(eid,))
            messagebox.showinfo(title="Info",message="Employee Deleted")
            connection.commit()
            entry1.delete(0,END)
        except:
            messagebox.showerror(title="Error",message="Invalid EmpId")

    btn_delete=Button(delete_gui,text="Delete",font=("Arial",14),command=emp_delete)
    btn_delete.grid(row=2,column=1,pady=10)
    btn_exit=Button(delete_gui,text='Exit',font=("Arial",14),command=lambda : delete_gui.destroy())
    btn_exit.grid(row=2,column=2,pady=10)

    delete_gui.config(bg='cyan')
    delete_gui.mainloop()

def view_employee():
    view_gui=Tk()
    view_gui.geometry('400x400')
    view_gui.title("Employee details")
    c=connection.cursor()
    c.execute("select * from Emp")
    rows=c.fetchall()
    if len(rows)==0:
        l1=Label(view_gui,text="No Employees Added.",font=('Arial',14))
        l1.pack(padx=30,pady=50)
    else:
        c=1
        for row in rows:
            empid,ename,j,sal=str(row[0]),str(row[1]),str(row[2]),str(row[3]) 
            l1=Label(view_gui,text=empid,font=('Arial',14))
            l2=Label(view_gui,text=ename,font=('Arial',14))
            l3=Label(view_gui,text=j,font=('Arial',14))
            l4=Label(view_gui,text=sal,font=('Arial',14))
            l1.grid(row=c,column=1,pady=5,padx=10)
            l2.grid(row=c,column=2,pady=5,padx=10)
            l3.grid(row=c,column=3,pady=5,padx=10)
            l4.grid(row=c,column=4,pady=5,padx=10)
            c+=1
    view_gui.config()
    view_gui.mainloop()

btn1=Button(root,text="Add Employee",width='20',font=('Arial',14),command=add_employee)
btn2=Button(root,text='Update Employee',width='20',font=('Arial',14),command=update_employee)
btn3=Button(root,text='Delete Employee',width='20',font=('Arial',14),command=delete_employee)
btn4=Button(root,text='View Employee',width='20',font=('Arial',14),command=view_employee)
btn5=Button(root,text="Exit",width=20,font=('Arial',14),command=lambda :root.destroy())

btn1.pack(pady='10')
btn2.pack(pady='10')
btn3.pack(pady='10')
btn4.pack(pady='10')
btn5.pack(pady='10')

root.config(bg='cyan')
root.mainloop()