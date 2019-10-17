import tkinter
import mysql.connector
from tkinter import messagebox

window=tkinter.Tk()
window.title("vicky")
window.configure(bg="yellow")
wi=window.winfo_screenwidth()
hi=window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(wi,hi))

def insertdata():
    mycon=mysql.connector.connect(host="localhost",user="root",password="root",database="vicky1")
    mycur=mycon.cursor()
    un=e1.get()
    ps=e2.get()
    mycur.execute("insert into login1 values('%s','%s')"%(un,ps))
    mycon.commit()
    messagebox.showinfo("Insert","Data Successfully inserted:%s"%(un))

l1=tkinter.Label(window,text="Enter user Name:")
l1.place(x="100",y="100")

e1=tkinter.Entry(window)
e1.place(x="200",y="100")

l2=tkinter.Label(window,text="Enter Password:")
l2.place(x="100",y="200")

e2=tkinter.Entry(window,show="*")
e2.place(x="200",y="200")

b1=tkinter.Button(window,text="clickme",command=insertdata)
b1.place(x=200,y=250)

window.mainloop()
