# Python-Practise
##Basic calculator

from  tkinter import *

root=Tk()

root.geometry("270x150")
root.title("Basic calculator")

equation=StringVar()

l1=Entry(root,textvariable=equation,justify="right")
l1.grid(columnspan=4,ipadx=70)


str1=""
def add_list(n):
    global str1
    str1=str1+str(n)
    equation.set(str1)
    

def final_result():
    try:
        global str1
        total=str(eval(str1))
        equation.set(total)
        str1=total
    except:
        equation.set("Error")
        str1=""

def clear_operation():
    global str1
    str1=""
    equation.set(str1)
    

def back_space():
    global str1
    str1=str1[:-1]
    equation.set(str1)
   

btn1=Button(root,text="1",width=8,height=1,command=lambda :add_list(1))
btn1.grid(row=1,column=0)

btn2=Button(root,text="2",width=8,height=1,command=lambda :add_list(2))
btn2.grid(row=1,column=1)

btn3=Button(root,text="3",width=8,height=1,command=lambda :add_list(3))
btn3.grid(row=1,column=2)

plus=Button(root,text="+",width=8,height=1,command=lambda :add_list("+"))
plus.grid(row=1,column=3)

btn4=Button(root,text="4",width=8,height=1,command=lambda :add_list(4))
btn4.grid(row=2,column=0)

btn5=Button(root,text="5",width=8,height=1,command=lambda :add_list(5))
btn5.grid(row=2,column=1)

btn6=Button(root,text="6",width=8,height=1,command=lambda :add_list(6))
btn6.grid(row=2,column=2)

minus=Button(root,text="-",width=8,height=1,command=lambda :add_list("-"))
minus.grid(row=2,column=3)

btn7=Button(root,text="7",width=8,height=1,command=lambda :add_list(7))
btn7.grid(row=3,column=0)

btn8=Button(root,text="8",width=8,height=1,command=lambda :add_list(8))
btn8.grid(row=3,column=1)

btn9=Button(root,text="9",width=8,height=1,command=lambda :add_list(9))
btn9.grid(row=3,column=2)

mul=Button(root,text="*",width=8,height=1,command=lambda :add_list("*"))
mul.grid(row=3,column=3)

div=Button(root,text="/",width=8,height=1,command=lambda :add_list("/"))
div.grid(row=4,column=3)

decimal=Button(root,text=".",width=8,height=1,command=lambda :add_list("."))
decimal.grid(row=4,column=0)

clear=Button(root,text="Clear",width=8,height=1,command=lambda :clear_operation())
clear.grid(row=5,column=0,columnspan=2)

equal=Button(root,text="=",width=8,height=1,command=lambda :final_result())
equal.grid(row=5,column=2,columnspan=2)

btn0=Button(root,text="0",width=8,height=1,command=lambda :add_list(0))
btn0.grid(row=4,column=1)

back=Button(root,text="<back",width=8,height=1,command=lambda :back_space())
back.grid(row=4,column=2)

root.config(bg="cyan")

root.mainloop()

