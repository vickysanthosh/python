import mysql.connector
from tkinter import*
from tkinter import messagebox

window=Tk()

window.configure(bg="blue")

w=window.winfo_screenwidth();
h=window.winfo_screenheight();
window.geometry("%dx%d+0+0"%(w,h))

def insertdata():
    mycon=mysql.connector.connect(host="localhost",user="root",password="root",database="emp")
    mycur=mycon.cursor()
    r=int(t1.get() )
    n=(t2.get() )
    m=int(t3.get () )
    mycur.execute("insert into login values(%d,'%s',%d)"%(r,n,m) )
    mycon.commit()
    messagebox.showinfo("Insert","Data successfully inserted:%d%s%d"%(r,n,m))




l1=Label(window,text="Enter Roll no:")
l1.place(x="100",y="100")
l2=Label(window,text="Student Registration Form",fg="red",bg="orange")
l2.place(x="150",y="50")
t1=Entry(window)
t1.place(x="200",y="100")

l2=Label(window,text="Enter Your Name:")
l2.place(x="100",y="200")

t2=Entry(window)
t2.place(x="200",y="200")

l3=Label(window,text="Enter Mark:")
l3.place(x="100",y="300")

t3=Entry(window)
t3.place(x="200",y="300")

b=Button(window,text="Insert",command=insertdata)
b.place(x="200",y="400")

