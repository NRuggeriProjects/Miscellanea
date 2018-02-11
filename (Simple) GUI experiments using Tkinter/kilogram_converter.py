''' kilograms converter  '''

from tkinter import *

window=Tk()
window.title('Kilograms converter')

def kg_convert():
    kg=float(e1_in.get())
    t1.insert(END,kg*1000)
    t2.insert(END,kg*2.20462)
    t3.insert(END,kg*35.274)
    

b1=Button(window,text='Convert',command=kg_convert)
b1.grid(row=0,column=3,columnspan=2)

e1_in=StringVar()
e1=Entry(window,textvariable=e1_in)
e1.grid(row=0,column=2)

l=Label(window,text='Insert kg to convert:')
l.grid(row=0,column=1)

t1=Text(window,height=1,width=10)
t1.grid(row=2,column=1)
l1=Label(window,text='Grams')
l1.grid(row=1,column=1)

t2=Text(window,height=1,width=10)
t2.grid(row=2,column=2)
l2=Label(window,text='Pounds')
l2.grid(row=1,column=2)

t3=Text(window,height=1,width=10)
t3.grid(row=2,column=3)
l3=Label(window,text='Ounces')
l3.grid(row=1,column=3)




window.mainloop()