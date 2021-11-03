from tkinter import *
from PIL import ImageTk,Image
def ssc():
    sp.destroy()
    from Login import show
    
sp=Tk()
canvasss=Canvas(sp,height=400,width=400)
canvasss.pack(fill='both',expand=1)
i=Image.open('abcd.png')
i=i.resize((400,400),Image.ANTIALIAS)
i1=ImageTk.PhotoImage(i)
canvasss.create_image(0,0,image=i1,anchor=NW)
sp.geometry("400x400+600+200")
sp.after(7000,ssc)
sp.mainloop()