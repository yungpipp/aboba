from tkinter import *
from tkinter import ttk
window=Tk()
window.title('аче')
window.geometry('1366x786')

def clicked():
    windor=Tk()
    windor.title('ниче')
    windor.geometry('800x600')
    lble=Label(windor,text=entry.get(),font=('Arial',50))
    lble.place(anchor='c',relx=0.5,rely=0.5)
    windor.mainloop()
lbl=Label(window,text='who reading that nigger',font=('Arial',25))
lbl.place(anchor='c',relx=0.91,rely=0.5)
photo = PhotoImage(file = "bruh.png",width=128,height=128)
btn=Button(window,text='bruh',font=('Arial',19),image=photo,compound=TOP,command=clicked)
btn.place(anchor='c',relx=0.5,rely=0.5)
entry=Entry(window,width=50)
entry.place(anchor='c',relx=0.5,rely=0.1)
combox=ttk.Combobox(window, values=['one','two','three'])
combox.place(anchor='c',relx=0.5,rely=0.9)
window.mainloop()
