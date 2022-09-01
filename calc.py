
import tkinter as tk

calculation=""

def add_to_calc(expression):#takes the expression as entered through buttons
    global calculation
    calculation+=str(expression)
    text_res.delete(1.0,"end")
    text_res.insert(1.0,calculation)

def evaluate():#evaluates the string
    global calculation
    try:
        calculation=calculation.lstrip("0")
        calculation =str(eval(calculation))
        text_res.delete(1.0,"end")
        text_res.insert(1.0,calculation)
    except ZeroDivisionError:
        clear()
        text_res.insert(1.0,"Zero Division Error")
    except:
        clear()
        text_res.insert(1.0,"Error")

def clear():#Clears the expression
    global calculation
    text_res.delete(1.0,"end")
    calculation=""

# bind title bar motion to the move window function
def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def change_on_hovering(event):
    global close_button
    close_button['bg']='#F16100'

def return_to_normalstate(event):
    global close_button
    close_button['bg']='#131a1a'



root=tk.Tk()
root["bg"]="#202124"
root.overrideredirect(True)
root.geometry("300x350+200+200")

title_bar = tk.Frame(root, bg='#131a1a', bd=2,highlightthickness=0)
close_button = tk.Button(title_bar, text='x', command= root.destroy,bg = "#131a1a",width=3,activebackground='#F16100',bd = 0,font="bold",fg='white',highlightthickness=0)

# a canvas for the main area of the window
window = tk.Canvas(root, bg='#202124',highlightthickness=0)

# pack the widgets
title_bar.pack(expand=1, fill=tk.X)
close_button.pack(side=tk.RIGHT)
window.pack(expand=1, fill=tk.BOTH)
xwin=None
ywin=None
    

title_bar.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>',change_on_hovering)
close_button.bind('<Leave>',return_to_normalstate)

text_res=tk.Text(window,height=2,width=20,font=("Tahoma",20),bg="#202124",fg="#F16100",border=0)
text_res.grid(columnspan=4)

#defining the buttons

button_dot=tk.Button(window,text=".",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("."),bg="#F5C47F",fg="#131a1a",activeforeground="#F5C47F",activebackground="#F6E7D8")
button_b1=tk.Button(window,text="(",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("("),bg="#F5C47F",fg="#131a1a",activeforeground="#F5C47F",activebackground="#F6E7D8")
button_b2=tk.Button(window,text=")",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(")"),bg="#F5C47F",fg="#131a1a",activeforeground="#F5C47F",activebackground="#F6E7D8")

button_add=tk.Button(window,text="+",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("+"),bg="#B7A47C",fg="#131a1a",activebackground="#F6E7D8",activeforeground="#131a1a")
button_sub=tk.Button(window,text="-",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("-"),bg="#B7A47C",fg="#131a1a",activebackground="#F6E7D8",activeforeground="#131a1a")
button_mul=tk.Button(window,text="x",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("*"),bg="#B7A47C",fg="#131a1a",activebackground="#F6E7D8",activeforeground="#131a1a")
button_div=tk.Button(window,text="/",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("/"),bg="#B7A47C",fg="#131a1a",activebackground="#F6E7D8",activeforeground="#131a1a")
button_mod=tk.Button(window,text="mod",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc("%"),bg="#B7A47C",fg="#131a1a",activebackground="#F6E7D8",activeforeground="#131a1a")

button_1=tk.Button(window,text="1",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(1),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_2=tk.Button(window,text="2",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(2),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_3=tk.Button(window,text="3",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(3),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_4=tk.Button(window,text="4",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(4),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_5=tk.Button(window,text="5",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(5),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_6=tk.Button(window,text="6",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(6),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_7=tk.Button(window,text="7",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(7),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_8=tk.Button(window,text="8",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(8),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_9=tk.Button(window,text="9",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(9),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")
button_0=tk.Button(window,text="0",height=2,width=8,font=("Comic Sans MS",10),command=lambda: add_to_calc(0),bg="#131a1a",fg="lightgray", activebackground="lightgray", activeforeground="#131a1a")

button_clear=tk.Button(window,text="AC",height=2,width=8,font=("Comic Sans MS",10),command=clear,bg="#F16100",fg="white")
button_ev=tk.Button(window,text="=",height=2,width=8,font=("Comic Sans MS",10),command=evaluate,bg="#F16100",fg="white")

#positioning the buttons

button_dot.grid(row=1,column=0)
button_b1.grid(row=1,column=1)
button_b2.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_div.grid(row=4,column=3)

button_clear.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_ev.grid(row=5,column=2)
button_mod.grid(row=5,column=3)

root.mainloop()