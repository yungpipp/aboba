from tkinter import *
from tkinter import ttk
window=Tk()
window.title('аче')
window.geometry('800x600')

def clicked():
    windor=Tk()
    windor.title('ниче')
    windor.geometry('400x300')
    lble=Label(windor,text="0",font=('Arial',50))
    if combox.get()=='+':
        a=int(entry.get())
        b=int(entryg.get())
        c=a+b
        lble.configure(text=str(c))
    if combox.get()=='-':
        a=int(entry.get())
        b=int(entryg.get())
        c=a-b
        lble.configure(text=str(c))
    if combox.get()=='*':
        a=int(entry.get())
        b=int(entryg.get())
        c=a*b
        lble.configure(text=str(c))
    if combox.get()=='/':
        a=int(entry.get())
        b=int(entryg.get())
        c=a/b
        lble.configure(text=str(c))
    if combox.get()=='^':
        a=int(entry.get())
        b=int(entryg.get())
        c=a**b
        lble.configure(text=str(c))
    lble.place(anchor='c',relx=0.5,rely=0.5)
    windor.mainloop()
entry=Entry(window,width=15)
entry.place(anchor='c',relx=0.25,rely=0.2)
combox=ttk.Combobox(window, values=['+','-','*','/','^'])
combox.place(anchor='c',relx=0.5,rely=0.2)
entryg=Entry(window,width=15)
entryg.place(anchor='c',relx=0.75,rely=0.2)
btn=Button(window,text='=',command=clicked)
btn.place(anchor='c',relx=0.5,rely=0.5)

window.mainloop()
