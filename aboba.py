from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext
def click():
    file=filedialog.askopenfile()
    txt.delete(1.0,END)
    txt.insert(txt.insert(INSERT,file.read()))
def ckicl():
    file=filedialog.asksaveasfile()
    file.write(txt.get(1.0,END))
window=Tk()
window.title('аче')
window.geometry('800x600')
menu=Menu(window)
menu.add_command(label="лйаФ",command=click)
menu.add_command(label='save',command=ckicl)
window.config(menu=menu)
txt=scrolledtext.ScrolledText(window,width=400,height=600)
txt.grid(row=0,column=0)
txt.insert(INSERT,"Здарова, ну шо ты")
window.mainloop()