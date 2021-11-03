from tkinter import *
from tkinter import messagebox as mb
import test3
login=Tk()
login.geometry("250x100+630+200")
def show():
    login.mainloop()

def lgsc():
    if e1.get()=="" or e2.get()=="":
        mb.showerror("Error","Please enter both, username and password.")
    else:
        val=test3.verify(e1.get(),e2.get())
        if val==True:
            mb.showinfo("Success","User logged in")
            login.destroy()
            from Home import show
        elif val==False:
            mb.showerror("Error","Incorrect username or password")
            e1.delete(0,END)
            e2.delete(0,END)

frame1=Frame(login,bg='cyan')
frame1.pack(fill='both',expand=1)
l1=Label(frame1,text='Enter username',bg='cyan')
l2=Label(frame1,text='Enter password',bg='cyan')
e1=Entry(frame1)
e2=Entry(frame1)
button=Button(frame1,text='Login',command=lgsc)
l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)
e1.grid(row=0,column=1,padx=5,pady=5)
e2.grid(row=1,column=1,padx=5,pady=5)
button.grid(row=2,column=0,columnspan=2)
