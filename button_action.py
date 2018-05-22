#!/usr/bin/python
from Tkinter import *
from Tkinter import messagebox
	
def click():
	res=txt.get()
	lbl.configure(text=res)
	txt.configure(text=" ")
	messagebox.showinfo('Report','Completed!')

window=Tk()
window.title("Button Action")
window.geometry('400x400')

lbl = Label(window, text="It is a clicky Button!")
lbl.grid(column=0, row=0)

txt=Entry(window, width=10)
txt.grid(column=0, row=1)
txt.focus()

btn=Button(window, text="Click Here!", font=("Arial Bold", 10), bg="blue", fg="red", command=click)
btn.grid(column=0, row=3)
window.mainloop()
