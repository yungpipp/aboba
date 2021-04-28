import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window=Tk()
window.title('аче')
window.geometry('800x600')
r=random.randint(0,10)
p=0
f=0
def clicked():
    global p
    global f
    p+=1
    lbl.configure(text=str(p))
    if int(entry.get())<r:
        lble.configure(text="Число больше")
    elif int(entry.get())>r:
        lble.configure(text="Число меньше")
    else:
        entry.configure(state="disabled")
        messagebox.showinfo('123','Вы угадали')
        f+=1
        if f>=5:
            messagebox.showinfo('хватит','хватит')
        p=0
def clickedс():
    entry.configure(state="normal")
    entry.delete(0, END)
    lble.configure(text="")
    global r
    r=random.randint(0,10)

entry=Entry(window,width=15)
entry.place(anchor='c',relx=0.5,rely=0.35)
lble=Label(window,text="",font=('Arial',25))
lble.place(anchor='c',relx=0.5,rely=0.25)
lbl=Label(window,text=p,font=('Arial',25))
lbl.place(anchor='c',relx=0.5,rely=0.75)
btn=Button(window,text='OK',font=('Arial',19),command=clicked)
btn.place(anchor='c',relx=0.5,rely=0.5)
btn=Button(window,text='Заново',font=('Arial',19),command=clickedс)
btn.place(anchor='c',relx=0.5,rely=0.65)
window.mainloop()