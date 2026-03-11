from tkinter import *

root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


#defining functions
def clickbut(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(number))
#defining clear button
def button_clear():
    e.delete(0,END)

#defining addition button
def but_add():
    first_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    e.delete(0,END)

#defining subtraction button
def sub():
    first_num=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_num)
    e.delete(0,END)

#defining multiplication button
def mul():
    first_num=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_num)
    e.delete(0,END)

#defining division button
def div():
    first_num=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    e.delete(0,END)

#defining equal to button
def but_equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_num))
    elif math=="subtraction":
        e.insert(0,f_num-int(second_num))
    elif math=="multiplication":
        e.insert(0,f_num*int(second_num))
    elif math=="division":
        e.insert(0,f_num/int(second_num))
    


#creating the buttons


button_1=Button(root,text="1",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(1))
button_2=Button(root,text="2",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(2))
button_3=Button(root,text="3",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(3))
button_4=Button(root,text="4",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(4))
button_5=Button(root,text="5",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(5))
button_6=Button(root,text="6",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(6))
button_7=Button(root,text="7",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(7))
button_8=Button(root,text="8",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(8))
button_9=Button(root,text="9",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(9))
button_0=Button(root,text="0",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=lambda:clickbut(0))

button_add=Button(root,text="+", font=10,bg="orange",fg="white",borderwidth=0,padx=40,pady=13,command=but_add)
button_sub=Button(root,text="-", font=10,bg="orange",fg="white",borderwidth=0,padx=40,pady=13,command=sub)
button_mul=Button(root,text="x", font=10,bg="orange",fg="white",borderwidth=0,padx=40,pady=13,command=mul)
button_div=Button(root,text="/", font=10,bg="orange",fg="white",borderwidth=0,padx=40,pady=13,command=div)
button_equals=Button(root,text="=",bg="#e8e8e8",fg="black",borderwidth=0,padx=40,pady=20,command=but_equal)
button_AC=Button(root,text="AC",padx=40,pady=13,bg="#a7a8a7",fg="white",borderwidth=0,command=lambda:button_clear())
#putting the button on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)

button_equals.grid(row=4,column=1)
button_AC.grid(row=4,column=2)
root.mainloop()
