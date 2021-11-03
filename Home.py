import test3
from io import BytesIO
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
root=Tk()
root.geometry("1500x750+10+10")
    
def t1v():
    root.geometry("500x400+500+200")
    rem()
    l1.config(bg='green')
    l2.config(bg='green')
    l3.config(bg='green')
    l4.config(bg='green')
    l5.config(bg='green')
    l6.config(bg='green')
    l7.config(bg='green')
    l8.config(bg='green')
    stat=test3.t1_status()
    for i in stat:
        for j in range(len(i)):
            if i[j]==l1.cget("text"):
                l1.config(bg='red')
            if i[j]==l2.cget("text"):
                l2.config(bg='red')
            if i[j]==l3.cget("text"):
                l3.config(bg='red')
            if i[j]==l4.cget("text"):
                l4.config(bg='red')
            if i[j]==l5.cget("text"):
                l5.config(bg='red')
            if i[j]==l6.cget("text"):
                l6.config(bg='red')
            if i[j]==l7.cget("text"):
                l7.config(bg='red')
            if i[j]==l8.cget("text"):
                l8.config(bg='red')
    t1.pack(fill='both',expand=1)
    
def t2v():
    root.geometry("500x400+500+200")
    rem()
    l9.config(bg='green')
    l10.config(bg='green')
    l11.config(bg='green')
    l12.config(bg='green')
    l13.config(bg='green')
    l14.config(bg='green')
    l15.config(bg='green')
    stat=test3.t2_status()
    for i in stat:
        for j in range(len(i)): 
            if i[j]==l9.cget("text"):
                l9.config(bg='red')
            if i[j]==l10.cget("text"):
                l10.config(bg='red')
            if i[j]==l11.cget("text"):
                l11.config(bg='red')
            if i[j]==l12.cget("text"):
                l12.config(bg='red')
            if i[j]==l13.cget("text"):
                l13.config(bg='red')
            if i[j]==l14.cget("text"):
                l14.config(bg='red')
            if i[j]==l15.cget("text"):
                l15.config(bg='red')
    t2.pack(fill='both',expand=1)

def hv():
    root.geometry("500x400+500+200")
    rem()
    l16.config(bg='green')
    l17.config(bg='green')
    l18.config(bg='green')
    l19.config(bg='green')
    l20.config(bg='green')
    stat=test3.hg_status()
    for i in stat:
        for j in range(len(i)):
            if i[j]==l16.cget("text"):
                l16.config(bg='red')
            if i[j]==l17.cget("text"):
                l17.config(bg='red')
            if i[j]==l18.cget("text"):
                l18.config(bg='red')
            if i[j]==l19.cget("text"):
                l19.config(bg='red')
            if i[j]==l20.cget("text"):
                l20.config(bg='red')
    hangar.pack(fill='both',expand=1)

def osv():
    root.geometry("500x400+500+200")
    rem()
    l21.config(bg='green')
    l22.config(bg='green')
    l23.config(bg='green')
    l24.config(bg='green')
    l25.config(bg='green')
    stat=test3.op_status()
    for i in stat:
        for j in range(len(i)):
            if i[j]==l21.cget("text"):
                l21.config(bg='red')
            if i[j]==l22.cget("text"):
                l22.config(bg='red')
            if i[j]==l23.cget("text"):
                l23.config(bg='red')
            if i[j]==l24.cget("text"):
                l24.config(bg='red')
            if i[j]==l25.cget("text"):
                l25.config(bg='red')
    openspots.pack(fill='both',expand=1)

def lp():
    root.geometry("1500x750+10+10")
    rem()
    def my_update(id):
        test3.ptl(id)
        mb.showinfo("Status Update","Plane landed")
        lps()
    def lps():
        
        for wid in land.winfo_children():
            wid.destroy()
        
        lpstitle=Label(land,text='Airplanes coming for Landing and Requesting to Land',font=('comic sans ms',19),bg='cyan')
        lpsl1=Label(land, text='Unique Flight id',bg='cyan',font=('comic sans ms',13))
        lpsl2=Label(land, text='Arrival Time',bg='cyan',font=('comic sans ms',13))
        lpsl3=Label(land, text='Departure Time',bg='cyan',font=('comic sans ms',13))
        lpsl4=Label(land, text='Aircraft ID',bg='cyan',font=('comic sans ms',13))
        lpsl5=Label(land, text='Flight Type',bg='cyan',font=('comic sans ms',13))
        lpsl6=Label(land, text='Flight Number',bg='cyan',font=('comic sans ms',13))
        lpsl7=Label(land, text='Airlines',bg='cyan',font=('comic sans ms',13))
        lpsl8=Label(land, text='Arriving From',bg='cyan',font=('comic sans ms',13))
        lpstitle.grid(row=0,column=0,columnspan=8,pady=5)
        lpsl1.grid(row=1,column=0,padx=5)
        lpsl2.grid(row=1,column=1,padx=5)
        lpsl3.grid(row=1,column=2,padx=5)
        lpsl4.grid(row=1,column=3,padx=5)
        lpsl5.grid(row=1,column=4,padx=5)
        lpsl6.grid(row=1,column=5,padx=5)
        lpsl7.grid(row=1,column=6,padx=5)
        lpsl8.grid(row=1,column=7,padx=5)
        i=2
        count=0
        data=test3.rtl()
        for a in data: 
            for j in range(len(a)):
                e = Entry(land, width=20, fg='blue',font=('comic sans ms',9)) 
                e.grid(row=i, column=j,padx=5,pady=25)
                e.insert(END,str(a[j]))
            e = Button(land, text='Land',font=('comic sans ms',9),command=lambda d=int(a[0]) : my_update(d)) 
            e.grid(row=i, column=j+1,padx=5,pady=2)
            i=i+1
            count=count+1
        land.pack(fill='both',expand=1)
        
    lps()

def landawaitpark():
    rem()
    root.geometry("1500x750+10+10")
    def laps():
        for wid in parka.winfo_children():
            wid.destroy()
        lapstitle=Label(parka,text='Airplanes who landed and are now waiting for Parking Allocation',font=('comic sans ms',19),bg='cyan')
        lapsl1=Label(parka, text='Unique Flight id',bg='cyan',font=('comic sans ms',13))
        lapsl2=Label(parka, text='Arrival Time',bg='cyan',font=('comic sans ms',13))
        lapsl3=Label(parka, text='Departure Time',bg='cyan',font=('comic sans ms',13))
        lapsl4=Label(parka, text='Aircraft ID',bg='cyan',font=('comic sans ms',13))
        lapsl5=Label(parka, text='Flight Type',bg='cyan',font=('comic sans ms',13))
        lapsl6=Label(parka, text='Flight Number',bg='cyan',font=('comic sans ms',13))
        lapsl7=Label(parka, text='Airlines',bg='cyan',font=('comic sans ms',13))
        lapsl8=Label(parka, text='Arriving From',bg='cyan',font=('comic sans ms',13))
        lapstitle.grid(row=0,column=0,columnspan=8,pady=5)
        lapsl1.grid(row=1,column=0,padx=5)
        lapsl2.grid(row=1,column=1,padx=5)
        lapsl3.grid(row=1,column=2,padx=5)
        lapsl4.grid(row=1,column=3,padx=5)
        lapsl5.grid(row=1,column=4,padx=5)
        lapsl6.grid(row=1,column=5,padx=5)
        lapsl7.grid(row=1,column=6,padx=5)
        lapsl8.grid(row=1,column=7,padx=5)
        i=2
        data=test3.law()
        for a in data: 
            for j in range(len(a)):
                e = Entry(parka, width=20, fg='blue',font=('comic sans ms',9)) 
                e.grid(row=i, column=j,padx=5,pady=25) 
                e.insert(END,str(a[j]))
            e = Button(parka, text='Request Parking',font=('comic sans ms',9),command=lambda d=int(a[0]) : my_update(d)) 
            e.grid(row=i, column=j+1,padx=5,pady=2)
            i=i+1
        parka.pack(fill='both',expand=1)
    def my_update(id):
        a=test3.pallot(id)
        if a==False:
            mb.showerror("Error","No parking available at the moment. Please wait.")
        else:
            test3.usttp(id)
            mb.showinfo("Status Update","Airplane Now Taxing Towards Parking")
        laps()
    laps()
        
def ttpp():
    root.geometry("1500x750+10+10")
    rem()
    def ttps():
        for wid in hard.winfo_children():
            wid.destroy()
        ttpstitle=Label(hard, text='Planes going towards Parking and after some time request for permission to move towards runway',font=('comic sans ms',19),bg='cyan')
        ttpsl1=Label(hard, text='Unique Flight id',bg='cyan',font=('comic sans ms',13))
        ttpsl2=Label(hard, text='Arrival Time',bg='cyan',font=('comic sans ms',13))
        ttpsl3=Label(hard, text='Departure Time',bg='cyan',font=('comic sans ms',13))
        ttpsl4=Label(hard, text='Arriving From',bg='cyan',font=('comic sans ms',13))
        ttpsl5=Label(hard, text='Departing to',bg='cyan',font=('comic sans ms',13))
        ttpsl6=Label(hard, text='Flight type',bg='cyan',font=('comic sans ms',13))
        ttpsl7=Label(hard, text='Flight Number',bg='cyan',font=('comic sans ms',13))
        ttpsl8=Label(hard,text='Parking',bg='cyan',font=('comic sans ms',13))
        ttpstitle.grid(row=0,column=0,columnspan=8,pady=5)
        ttpsl1.grid(row=1,column=0,padx=5)
        ttpsl2.grid(row=1,column=1,padx=5)
        ttpsl3.grid(row=1,column=2,padx=5)
        ttpsl4.grid(row=1,column=3,padx=5)
        ttpsl5.grid(row=1,column=4,padx=5)
        ttpsl6.grid(row=1,column=5,padx=5)
        ttpsl7.grid(row=1,column=6,padx=5)
        ttpsl8.grid(row=1,column=7,padx=5)
        data=test3.rttp()
        i=2
        for a in data:
            for j in range(len(a)):
                e = Entry(hard, width=20, fg='blue',font=('comic sans ms',9)) 
                e.grid(row=i, column=j,padx=5,pady=3) 
                e.insert(END, str(a[j]))
            e=Button(hard, text='Show route',font=('comic sans ms',9),command=lambda d=int(a[0]) : my_show(d)) 
            e.grid(row=i, column=j+1)
            e=Button(hard,text='Reached parking and now,\nrequests for permission to\ntaxitowards runway',font=('comic sans ms',9),command=lambda d=int(a[0]) : my_update(d))
            e.grid(row=i,column=j+2,padx=5,pady=2)
            i=i+1
        hard.pack(fill='both',expand=1)
    def my_update(id):
        test3.ptttr(id)
        mb.showinfo("Status Update","Airplane Now taxing towards runway")
        ttps()
    def my_show(id):
        a1=test3.showroute1(id)
        image1=Image.open(BytesIO(a1))
        image1.show()
    ttps()

def ttrp():
    root.geometry("1500x750+10+10")
    rem()
    def my_update(id):
        test3.ptt(id)
        mb.showinfo("Status Update","Airplane Ready to Take Off")
        ttrs()
    def ttrs():
        i=2
        for wid in run.winfo_children():
            wid.destroy()
        ttrstitle=Label(run,text='Plane going towards runway and after some time request for permission to Take off',font=('comic sans ms',19),bg='cyan')
        ttrsl1=Label(run, text='Unique Flight id',bg='cyan',font=('comic sans ms',13))
        ttrsl2=Label(run, text='Arrival Time',bg='cyan',font=('comic sans ms',13))
        ttrsl3=Label(run, text='Departure Time',bg='cyan',font=('comic sans ms',13))
        ttrsl4=Label(run, text='Aircraft ID',bg='cyan',font=('comic sans ms',13))
        ttrsl5=Label(run, text='Flight Type',bg='cyan',font=('comic sans ms',13))
        ttrsl6=Label(run, text='Flight Number',bg='cyan',font=('comic sans ms',13))
        ttrsl7=Label(run, text='Airlines',bg='cyan',font=('comic sans ms',13))
        ttrsl8=Label(run, text='Departing to',bg='cyan',font=('comic sans ms',13))
        ttrstitle.grid(row=0,column=0,columnspan=8,pady=5)
        ttrsl1.grid(row=1,column=0,padx=5)
        ttrsl2.grid(row=1,column=1,padx=5)
        ttrsl3.grid(row=1,column=2,padx=5)
        ttrsl4.grid(row=1,column=3,padx=5)
        ttrsl5.grid(row=1,column=4,padx=5)
        ttrsl6.grid(row=1,column=5,padx=5)
        ttrsl7.grid(row=1,column=6,padx=5)
        ttrsl8.grid(row=1,column=7,padx=5)
        data=test3.gtr()
        for a in data: 
            for j in range(len(a)):
                e = Entry(run, width=20, fg='blue',font=('comic sans ms',9)) 
                e.grid(row=i, column=j,padx=5,pady=25) 
                e.insert(END, str(a[j]))
            e = Button(run, text='Show Route',font=('comic sans ms',9),command=lambda d=int(a[0]):my_show(d)) 
            e.grid(row=i, column=j+1)
            e=Button(run,text='Reached for Takeoff',font=('comic sans ms',9),command=lambda d=int(a[0]) : my_update(d))
            e.grid(row=i,column=j+2,padx=5,pady=2)
            i=i+1
        run.pack(fill='both',expand=1)
    def my_show(id):
        a1=test3.showroute2(id)
        image1=Image.open(BytesIO(a1))
        image1.show()
    ttrs()

def tp():
    root.geometry("1500x750+10+10")
    rem()
    def my_update(id):
        test3.usto(id)
        mb.showinfo("Status Update","Airplane Taken Off")
        tps()
    def tps():
        i=2
        for wid in take.winfo_children():
            wid.destroy()
        tpsl1=Label(take, text='Unique Flight id',bg='cyan',font=('comic sans ms',13))
        tpsl2=Label(take, text='Arrival Time',bg='cyan',font=('comic sans ms',13))
        tpsl3=Label(take, text='Departure Time',bg='cyan',font=('comic sans ms',13))
        tpsl4=Label(take, text='Aircraft ID',bg='cyan',font=('comic sans ms',13))
        tpsl5=Label(take, text='Flight Type',bg='cyan',font=('comic sans ms',13))
        tpsl6=Label(take, text='Flight Number',bg='cyan',font=('comic sans ms',13))
        tpsl7=Label(take, text='Airlines',bg='cyan',font=('comic sans ms',13))
        tpsl8=Label(take, text='Departing to',bg='cyan',font=('comic sans ms',13))
        tpstitle=Label(take,text='Planes requesting for Takeoff',font=('comic sans ms',19),bg='cyan')
        tpsl1.grid(row=1,column=0,padx=5)
        tpsl2.grid(row=1,column=1,padx=5)
        tpsl3.grid(row=1,column=2,padx=5)
        tpsl4.grid(row=1,column=3,padx=5)
        tpsl5.grid(row=1,column=4,padx=5)
        tpsl6.grid(row=1,column=5,padx=5)
        tpsl7.grid(row=1,column=6,padx=5)
        tpsl8.grid(row=1,column=7,padx=5)
        tpstitle.grid(row=0,column=0,columnspan=8,pady=5)
        data=test3.rtt()
        for a in data: 
            for j in range(len(a)):
                e = Entry(take, width=20, fg='blue',font=('comic sans ms',9)) 
                e.grid(row=i, column=j,padx=5,pady=25) 
                e.insert(END, str(a[j]))
            e = Button(take, text='Takeoff',font=('comic sans ms',9),command=lambda d=int(a[0]) : my_update(d)) 
            e.grid(row=i, column=j+1,padx=5,pady=2)
            i=i+1
        take.pack(fill='both',expand=1)
    tps()

def af():
    root.geometry("400x400+600+200")
    rem()
    add.pack(fill='both',expand=1)

def afo():
    root.geometry("400x400+600+200")
    if cb1.get()==True:
        if e26.get()=="" or e28.get()=="" or e31.get()=="" or e32.get()=="" or e33.get()=="":
            mb.showerror("Error","Please enter required values")
        else:
            test3.addEntry(e31.get(),e26.get(),e26.get(),e28.get(),e30.get(),e29.get(),'Y',e32.get(),e33.get(),e34.get())
            test3.ptl(e31.get())
            mb.showinfo("Success","Emergency Flight Landed")
            e26.delete(0,END)
            e27.delete(0,END)
            e28.delete(0,END)
            e29.delete(0,END)
            e30.delete(0,END)
            e31.delete(0,END)
            e32.delete(0,END)
            e33.delete(0,END)
            e34.delete(0,END)
            
        
    elif e26.get()=="" or e28.get()==""  or e31.get()=="" or e32.get()=="" or e33.get()=="":
        mb.showerror("Error","Please enter required values")
    else:
        test3.addEntry(e31.get(),e26.get(),e27.get(),e28.get(),e30.get(),e29.get(),'N',e32.get(),e33.get(),e34.get())
        mb.showinfo("Success","Flight Added Successfully")
        e26.delete(0,END)
        e27.delete(0,END)
        e28.delete(0,END)
        e29.delete(0,END)
        e30.delete(0,END)
        e31.delete(0,END)
        e32.delete(0,END)
        e33.delete(0,END)
        e34.delete(0,END)
        

def vh():
    root.geometry("1500x750+10+10")
    rem()
    def showhis():
        showhisstitle=Label(his,text='Flight history',font=('comic sans ms',19),bg='cyan')
        showhisl1=Label(his, text='Unique Flight id',bg='cyan',font=('comic sans ms',13))
        showhisl2=Label(his, text='Arrival Time',bg='cyan',font=('comic sans ms',13))
        showhisl3=Label(his, text='Departure Time',bg='cyan',font=('comic sans ms',13))
        showhisl4=Label(his, text='Aircraft ID',bg='cyan',font=('comic sans ms',13))
        showhisl5=Label(his, text='Flight Type',bg='cyan',font=('comic sans ms',13))
        showhisl6=Label(his, text='Flight Number',bg='cyan',font=('comic sans ms',13))
        showhisl7=Label(his, text='Airlines',bg='cyan',font=('comic sans ms',13))
        showhisl8=Label(his,text='Parking',bg='cyan',font=('comic sans ms',13))
        showhisl9=Label(his, text='Arrived from',bg='cyan',font=('comic sans ms',13))
        showhisl10=Label(his,text='Departed To',bg='cyan',font=('comic sans ms',13))
        showhisstitle.grid(row=0,column=0,columnspan=10,pady=5)
        showhisl1.grid(row=1,column=0,padx=5)
        showhisl2.grid(row=1,column=1,padx=5)
        showhisl3.grid(row=1,column=2,padx=5)
        showhisl4.grid(row=1,column=3,padx=5)
        showhisl5.grid(row=1,column=4,padx=5)
        showhisl6.grid(row=1,column=5,padx=5)
        showhisl7.grid(row=1,column=6,padx=5)
        showhisl8.grid(row=1,column=7,padx=5)
        showhisl9.grid(row=1,column=8,padx=5)
        showhisl10.grid(row=1,column=9,padx=5)
        i=2
        data=test3.his()
        for a in data: 
            for j in range(len(a)):
                e = Entry(his, width=20, fg='blue',font=('comic sans ms',8)) 
                e.grid(row=i, column=j,padx=3,pady=25) 
                e.insert(END, str(a[j]))
            i=i+1
        his.pack(fill='both',expand=1)
    showhis()
def rem():
    airport.pack_forget()
    t1.pack_forget()
    t2.pack_forget()
    openspots.pack_forget()
    land.pack_forget()
    take.pack_forget()
    hangar.pack_forget()
    hard.pack_forget()
    run.pack_forget()
    add.pack_forget()
    his.pack_forget()
    parka.pack_forget()

def abo():
    root.geometry("1500x750+10+10")
    rem()
    airport.pack(fill='both',expand=1)

def show():
    abo()
    root.mainloop()

my_menu=Menu(root)
root.config(menu=my_menu)

my_menu.add_command(label='About',command=abo)

home_menu=Menu(my_menu)
my_menu.add_cascade(label='Airport Views',menu=home_menu)
home_menu.add_command(label='Terminal 1',command=t1v)
home_menu.add_command(label='Terminal 2',command=t2v)
home_menu.add_command(label='Hangars',command=hv)
home_menu.add_command(label='Open Spots',command=osv)

modify_menu=Menu(my_menu)
my_menu.add_cascade(label='Modify',menu=modify_menu)
modify_menu.add_command(label='Landing Permission',command=lp)
modify_menu.add_command(label='Request Hardstand allocation',command=landawaitpark)
modify_menu.add_command(label='Taxing towards Hardstand',command=ttpp)
modify_menu.add_command(label='Taxing towards Runway',command=ttrp)
modify_menu.add_command(label='Takeoff Permission',command=tp)

other_menu=Menu(my_menu)
my_menu.add_cascade(label='View and Add flights',menu=other_menu)
other_menu.add_command(label='View History',command=vh)
other_menu.add_command(label='Add flights',command=af)

def qui():
    mb.showwarning("Close screen","Logging you out and closing the screen")
    root.destroy()

my_menu.add_command(label='Exit',command=qui)

airport=Canvas(root,height=1500,width=750,bg='cyan')
land=Frame(root,height=400,width=400,bg='cyan')
hard=Frame(root,height=400,width=400,bg='cyan')
run=Frame(root,height=400,width=400,bg='cyan')
take=Frame(root,height=400,width=400,bg='cyan')
add=Frame(root,height=400,width=400,bg='cyan')
his=Frame(root,height=400,width=400,bg='cyan')
parka=Frame(root,height=400,width=400,bg='cyan')
hl=Label(airport,text='Overall view of Airport',bg='cyan',font=('comic sans ms',19))
hl.place(x=650,y=5)
hl1=Label(airport,text='This is the design of our airport which is inspired by Mumbai Airport which is better known as Chattrapati Shivagi International Airport.\
We have considered partition of airport into 4 parts for 4 differet flight categories: T1 for domestic commercial flights,\n T2 for International commercial flights\
Hangars for Private Airplanes and Open Parking for Cargo airplanes. Staff can give permissions to airplanes for takeoff and landing as well as guide airplanes\
towards their respective hardstands or parking spots.',bg='cyan',font=('comic sans ms',9))
hl1.place(x=25,y=50)
i12=Image.open('DEFAULT.png')
i12=i12.resize((1500,750),Image.ANTIALIAS)
i112=ImageTk.PhotoImage(i12)
airport.create_image(0,90,image=i112,anchor=NW)
airport.pack(fill='both',expand=1)


t1=Canvas(root,width=500,height=400,bg='white')
img1=Image.open('123.jpeg')
im1=ImageTk.PhotoImage(img1)
t1.create_image(0,0,image=im1,anchor=NW)

l1=Label(t1,text='P1',font=(20),bg='green',fg='white')
l1.place(x=50,y=180)
l2=Label(t1,text='P2',font=(20),bg='green',fg='white')
l2.place(x=100,y=180)
l3=Label(t1,text='P3',font=(20),bg='green',fg='white')
l3.place(x=150,y=180)
l4=Label(t1,text='P4',font=(20),bg='green',fg='white')
l4.place(x=200,y=180)
l5=Label(t1,text='P5',font=(20),bg='green',fg='white')
l5.place(x=250,y=180)
l6=Label(t1,text='P6',font=(20),bg='green',fg='white')
l6.place(x=300,y=180)
l7=Label(t1,text='P7',font=(20),bg='green',fg='white')
l7.place(x=350,y=180)
l8=Label(t1,text='P8',font=(20),bg='green',fg='white')
l8.place(x=400,y=180)
l2222=Label(t1,text='Terminal 1',font=(25),bg='white')
l2222.place(x=190,y=95)

t2=Canvas(root,width=320,height=300,bg='white')
img2=Image.open('101.jpeg')
img2=img2.resize((500,300),Image.ANTIALIAS)
im2=ImageTk.PhotoImage(img2)
t2.create_image(0,0,image=im2,anchor=NW)

l9=Label(t2,text='P9',font=(20),bg='green',fg='white')
l9.place(x=50,y=52)
l10=Label(t2,text='P10',font=(20),bg='green',fg='white')
l10.place(x=50,y=82)
l11=Label(t2,text='P11',font=(20),bg='green',fg='white')
l11.place(x=50,y=197)
l12=Label(t2,text='P12',font=(20),bg='green',fg='white')
l12.place(x=75,y=225)
l13=Label(t2,text='P13',font=(20),bg='green',fg='white')
l13.place(x=100,y=252)
l14=Label(t2,text='P14',font=(20),bg='green',fg='white')
l14.place(x=400,y=225)
l15=Label(t2,text='P15',font=(20),bg='green',fg='white')
l15.place(x=450,y=225)
l1111=Label(t2,text='Terminal 2',font=(25),bg='white')
l1111.place(x=200,y=100)

hangar=Canvas(root,width=500,height=400,bg='white')
img3=Image.open('456.jpeg')
img3=img3.resize((505,79),Image.ANTIALIAS)
im3=ImageTk.PhotoImage(img3)
hangar.create_image(0,180,image=im3,anchor=NW)

l16=Label(hangar,text='P16',font=(20),bg='green',fg='white')
l16.place(x=22,y=160)
l17=Label(hangar,text='P17',font=(20),bg='green',fg='white')
l17.place(x=130,y=160)
l18=Label(hangar,text='P18',font=(20),bg='green',fg='white')
l18.place(x=235,y=160)
l19=Label(hangar,text='P19',font=(20),bg='green',fg='white')
l19.place(x=340,y=160)
l20=Label(hangar,text='P20',font=(20),bg='green',fg='white')
l20.place(x=445,y=160)
l3333=Label(hangar,text='Hangers',font=(25),bg='white')
l3333.place(x=215,y=265)

openspots=Canvas(root,width=500,height=400,bg='white')
img4=Image.open('789.jpeg')
im4=ImageTk.PhotoImage(img4)
openspots.create_image(150,0,image=im4,anchor=NW)

l21=Label(openspots,text='P21',font=(20),bg='green',fg='white')
l21.place(x=220,y=50)
l22=Label(openspots,text='P22',font=(20),bg='green',fg='white')
l22.place(x=220,y=110)
l23=Label(openspots,text='P23',font=(20),bg='green',fg='white')
l23.place(x=220,y=170)
l24=Label(openspots,text='P24',font=(20),bg='green',fg='white')
l24.place(x=220,y=230)
l25=Label(openspots,text='P25',font=(20),bg='green',fg='white')
l25.place(x=220,y=290)
l4444=Label(openspots,text='Open Spots',font=(25),bg='white')
l4444.place(x=190,y=350)

def cbshow():
    if cb1.get():
        b2.grid(row=1,column=2)
    else:
        b2.grid_forget()

l31=Label(add,text='Unique Flight ID *',bg='cyan')
l32=Label(add,text='Enter aircraft no. *',bg='cyan')
l33=Label(add,text='Arriving from *',bg='cyan')
l34=Label(add,text='Departing to',bg='cyan')
l26=Label(add,text='Arrival timestamp *',bg='cyan')
l27=Label(add,text='Departure timestamp',bg='cyan')
l28=Label(add,text='Flight type *',bg='cyan')
l29=Label(add,text='Airlines',bg='cyan')
l30=Label(add,text='Flight Number',bg='cyan')

e31=Entry(add)
e32=Entry(add)
e33=Entry(add)
e34=Entry(add)
e26=Entry(add)
e27=Entry(add)
n=StringVar()
e28=ttk.Combobox(add,width=20,textvariable=n)
e28['values']=('Domestic Commercial','International Commercial','Cargo','Private')
e29=Entry(add)
e30=Entry(add)
cb1=BooleanVar()
c=Checkbutton(add,text='Emergency',variable=cb1,onvalue=True,offvalue=False,command=cbshow,bg='cyan')

b1=Button(add,text='Add flight',command=afo)
b1.grid(row=9,column=1)
b2=Button(add,text='Emergency Land',command=afo)

l31.grid(row=0,column=0,padx=2,pady=2)
l32.grid(row=1,column=0,padx=2,pady=2)
l33.grid(row=2,column=0,padx=2,pady=2)
l34.grid(row=3,column=0,padx=2,pady=2)
l29.grid(row=4,column=0,padx=2,pady=2)
l26.grid(row=5,column=0,padx=2,pady=2)
l27.grid(row=6,column=0,padx=2,pady=2)
l28.grid(row=7,column=0,padx=2,pady=2)
l30.grid(row=8,column=0,padx=2,pady=2)
e31.grid(row=0,column=1,padx=2,pady=2)
e32.grid(row=1,column=1,padx=2,pady=2)
e33.grid(row=2,column=1,padx=2,pady=2)
e34.grid(row=3,column=1,padx=2,pady=2)
e29.grid(row=4,column=1,padx=2,pady=2)
e26.grid(row=5,column=1,padx=2,pady=2)
e27.grid(row=6,column=1,padx=2,pady=2)
e28.grid(row=7,column=1,padx=2,pady=2)
e30.grid(row=8,column=1,padx=2,pady=2)
c.grid(row=0,column=2,padx=2,pady=2)