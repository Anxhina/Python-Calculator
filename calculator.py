#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import*
import math
from math import *
from math import sin
import os


me=Tk()
me.geometry("800x500")
me.title("CALCULATOR")
melabel = Label(me,text="CALCULATOR",bg='light blue',font=("Times",30,'bold'))
melabel.pack(side=TOP)
me.config(background='light blue')

textin=StringVar()
operator=""

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator) 

def e_constant(number):   #lambda:clickbut(1)
     global operator
     e=2.7182818285
     operator=operator+str(number)
     textin.set(operator) 
     return number

def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''         

def clrbut():
     textin.set('')

def factorial(n):   
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);   
def calculate():
    result=factorial(int(textin.get()))
    textin.set(result)

def clear():
	global operator
	operator=""
	textin.set("")


     
metext=Entry(me,font=("Courier New",12,'bold'),textvar=textin,width=50,bd=5,bg='powder blue')
metext.pack()

#buttons
but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but9.place(x=10,y=240)

but10=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but10.place(x=75,y=100)

but11=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but11.place(x=75,y=170)

but12=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but12.place(x=75,y=240)

but13=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but13.place(x=140,y=100)

but14=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but14.place(x=140,y=170)

but15=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but15.place(x=140,y=240)

but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

#trigonometri
butS=Button(me,padx=16,pady=16,bd=4,bg='white',text="sin",command=lambda:clickbut("sin"),font=("Courier New",16,'bold'))
butS.place(x=275,y=100)

butC=Button(me,padx=16,pady=16,bd=4,bg='white',text="cos",command=lambda:clickbut("cos"),font=("Courier New",16,'bold'))
butC.place(x=380,y=100)

butF=Button(me,padx=27,pady=16,bd=4,bg='white',text="!",command=calculate,font=("Courier New",16,'bold'))
butF.place(x=480,y=100)


but3=Button(me,padx=20,pady=14,bd=4,bg='white',command=lambda:clickbut("ln"),text="ln",font=("Courier New",16,'bold'))
but3.place(x=275,y=170)

but4=Button(me,padx=16,pady=14,bd=4,bg='white',command=lambda:clickbut("log"),text="log",font=("Courier New",16,'bold'))
but4.place(x=380,y=170)


but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:e_("e**"),text="e^x",font=("Courier New",16,'bold'))
but6.place(x=480,y=240)

but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("*"),text="SQR",font=("Courier New",16,'bold'))
but7.place(x=275,y=240)

but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("**"),text="x^y",font=("Courier New",16,'bold'))
but8.place(x=380,y=240)

#constant
butSq=Button(me,padx=20,pady=14,bd=4,bg='white',command=lambda:clickbut("**0.5"),text="√x",font=("Courier New",16,'bold'))
butSq.place(x=380,y=310)

butPi=Button(me,padx=28,pady=14,bd=4,bg='white',command=lambda:e_(e),text="π",font=("Courier New",16,'bold'))
butPi.place(x=275,y=310)

but5=Button(me,padx=28,pady=14,bd=4,bg='white',command=lambda:clickbut("("),text="(",font=("Courier New",16,'bold'))
but5.place(x=480,y=170)

but18=Button(me,padx=28,pady=14,bd=4,bg='white',command=lambda:clickbut(2.71),text="e",font=("Courier New",16,'bold'))
but18.place(x=480,y=310)

but19=Button(me,padx=28,pady=14,bd=4,bg='white',text=")",command=lambda:clickbut(")"),font=("Courier New",16,'bold'))
but19.place(x=580,y=170)

#operators
butPl=Button(me,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butPl.place(x=205,y=100)

butM=Button(me,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butM.place(x=205,y=170)

but=Button(me,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
but.place(x=205,y=240)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

but20=Button(me,padx=28,pady=14,bd=4,bg='white',text="%",command=lambda:clickbut("%"),font=("Courier New",16,'bold'))
but20.place(x=580,y=240)

but21=Button(me,padx=190,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
but21.place(x=10,y=400)

#clear
butclear=Button(me,padx=20,pady=14,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=580,y=100)

butclear1=Button(me,padx=28,pady=14,bd=4,bg='white',text="C",command=clear,font=("Courier New",16,'bold'))
butclear1.place(x=580,y=310)


me.mainloop()