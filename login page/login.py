from tkinter import * 
from tkinter import messagebox 
def login():
    UserName=e1.get()
    Password=e2.get()
    if UserName=="" and Password=="":
        messagebox.showerror('Login','Blank is not allowed')
    elif UserName=='bernet' and Password=='1234':
        messagebox.showinfo('Login','Login Successful')
        root.destroy()
        top=Tk()
        top.configure(bg="blue")
        top.geometry("700x400+50+50")
        l3=Label(top, text='Welcome',font=('Arial',20))
        l3.place(x=300,y=200)
    else:
        messagebox.showerror('Login','Invalid UserName and Password')
root = Tk()
root.geometry("700x400+50+50")
l1 = Label(root, text = "Username:")
l2 = Label(root, text = "Password:")
l1.grid(row = 0, column = 0, pady = 2)
l2.grid(row = 1, column = 0, pady = 2)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
b1=Button(root,text='Login',command=login)
b1.grid(row=2,column=1)
root.mainloop()

