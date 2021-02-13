from tkinter import *

expression=''

master = Tk()
master.configure(background="dodgerblue")
master.title("My header")
master.resizable(width=False, height=False)

def press(num):
 global expression
 expression =expression+str(num)
 equation.set(expression)

def equl():
 try:

  global expression
 
  total=str(eval(expression))
  equation.set(total)
  expression=""
 
 except:
  equation.set("Error")
  expression=""


f= Frame(master, width=240,height=320)
f.pack()
equation=StringVar()
dp=Entry(f,width=12,textvariable=equation)
dp.config(font=("Arial", 30))
dp.grid(columnspan='4',column=0,row=0,ipadx=10,ipady=10)

equation.set("Type some text")

width="2"
height="1"
bcolor="royalblue"
fcolor="#fff"



b7=Button(f,text=7,bg=bcolor,fg=fcolor,width=width,height=height ,command=lambda: press(7),bd=0)
b7.grid(column=0,row=1)
b7.config(font=("Arial", 30))

b8=Button(f,text=8,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(8),bd=0)
b8.grid(column=1,row=1)
b8.config(font=("Arial", 30))

b9=Button(f,text=9,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(9),bd=0)
b9.grid(column=2,row=1)
b9.config(font=("Arial", 30))

bmu=Button(f,text="*",bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press("*"),bd=0)
bmu.grid(column=3,row=1)
bmu.config(font=("Arial", 30))



b4=Button(f,text=4,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(4),bd=0)
b4.grid(column=0,row=2)
b4.config(font=("Arial", 30))

b5=Button(f,text=5,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(5),bd=0)
b5.grid(column=1,row=2)
b5.config(font=("Arial", 30))

b6=Button(f,text=6,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(6),bd=0)
b6.grid(column=2,row=2)
b6.config(font=("Arial", 30))

bdiv=Button(f,text="/",bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press("/"),bd=0)
bdiv.grid(column=3,row=2)
bdiv.config(font=("Arial", 30))



b1=Button(f,text=1,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(1),bd=0)
b1.grid(column=0,row=3)
b1.config(font=("Arial", 30))

b2=Button(f,text=2,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(2),bd=0)
b2.grid(column=1,row=3)
b2.config(font=("Arial", 30))

b3=Button(f,text=3,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(3),bd=0)
b3.grid(column=2,row=3)
b3.config(font=("Arial", 30))

bm=Button(f,text="-",bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press("-"),bd=0)
bm.grid(column=3,row=3)
bm.config(font=("Arial", 30))



bd=Button(f,text=".",bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press("."),bd=0)
bd.grid(column=0,row=4)
bd.config(font=("Arial", 30))

b0=Button(f,text=0,bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press(0),bd=0)
b0.grid(column=1,row=4)
b0.config(font=("Arial", 30))

be=Button(f,text="=",bg=bcolor,fg=fcolor,width=width,height=height,command=equl,bd=0)
be.grid(column=2,row=4)
be.config(font=("Arial", 30))

bp=Button(f,text="+",bg=bcolor,fg=fcolor,width=width,height=height,command=lambda: press("+"),bd=0)
bp.grid(column=3,row=4)
bp.config(font=("Arial", 30))

master.mainloop()