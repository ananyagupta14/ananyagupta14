from tkinter import *

root=Tk()
root.title("Tic Tac Toe")
root["bg"]="#A9F1DF"

def disable():
    btn1["state"] = "disabled"
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"
    btn4["state"] = "disabled"
    btn5["state"] = "disabled"
    btn6["state"] = "disabled"
    btn7["state"] = "disabled"
    btn8["state"] = "disabled"
    btn9["state"] = "disabled"

def enable():
    btn1["state"] = "normal"
    btn2["state"] = "normal"
    btn3["state"] = "normal"
    btn4["state"] = "normal"
    btn5["state"] = "normal"
    btn6["state"] = "normal"
    btn7["state"] = "normal"
    btn8["state"] = "normal"
    btn9["state"] = "normal"

def NewGame():
    global x_turn,gameover,count
    count=0
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""

    btn1["bg"]="#1EAE98"
    btn2["bg"]="#1EAE98"
    btn3["bg"]="#1EAE98"
    btn4["bg"]="#1EAE98"
    btn5["bg"]="#1EAE98"
    btn6["bg"]="#1EAE98"
    btn7["bg"]="#1EAE98"
    btn8["bg"]="#1EAE98"
    btn9["bg"]="#1EAE98"

    x_turn=True
    status["text"]="X's Turn"
    gameover=False
    enable()

x_wins=0
o_wins=0
x_turn=True
gameover=False
count=0

btn_new=Button(text="New Game",relief="flat",font=("Arial Rounded MT Bold",12), command=NewGame,bg="#A9F1DF",fg="#007965",activebackground="#007965",activeforeground="#A9F1DF")
status=Label(text="X's Turn",font=("Arial Rounded MT Bold",12),bg="#A9F1DF",fg="#007965")
score=Label(text="X:{}  O:{}".format(x_wins,o_wins),bg="#A9F1DF",font=("Arial Rounded MT Bold",12),fg="#007965")

btn_new.grid(row=0,column=0)
status.grid(row=0,column=1)
score.grid(row=0,column=2)

def check_status(x_turn):

    if x_turn:
        check="X"
    else:
        check="O"

    #3 rows
    if btn1["text"] == btn2["text"] == btn3["text"] == check:
        return btn1,btn2,btn3
    if btn4["text"] == btn5["text"] == btn6["text"] == check:
        return btn4,btn5,btn6
    if btn7["text"] == btn8["text"] == btn9["text"] == check:
        return btn7,btn8,btn9
    #3 columns
    if btn1["text"] == btn4["text"] == btn7["text"] == check:
        return btn1,btn4,btn7
    if btn2["text"] == btn5["text"] == btn8["text"] == check:
        return btn2,btn5,btn8
    if btn3["text"] == btn6["text"] == btn9["text"] == check:
        return btn3,btn6,btn9
    #2 diagonals
    if btn1["text"] == btn5["text"] == btn9["text"] == check:
        return btn1,btn5,btn9
    if btn3["text"] == btn5["text"] == btn7["text"] == check:
        return btn3,btn5,btn7
    return None
    
def Click(btn):
    global x_turn,x_wins,o_wins,gameover,count
    if (btn["text"]!="" or gameover):
        return
    if x_turn:
        btn["text"]="X"
        btn["fg"]="#A9F1DF"
    else:
        btn["text"]="O"
        btn["fg"]="#FFFFC7"
    
    b=check_status(x_turn)

    if b!=None:
        b[0]["bg"]="#007965"
        b[1]["bg"]="#007965"
        b[2]["bg"]="#007965"
    
        if x_turn:
            status["text"]="X wins!"
            x_wins+=1
            disable()
        else:
            status["text"]="O wins!"
            o_wins+=1
            disable()

        score["text"]="X:{}  O:{}".format(x_wins,o_wins)
        gameover=True
        return
    count+=1
    if count==9:
        status["text"]="Tie"
    x_turn=not x_turn
    status["text"]="X's Turn" if x_turn else "O's Turn"
    if count==9:
        status["text"]="Tie"
        disable()


btn1=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn1),activebackground="#A9F1DF")
btn2=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn2),activebackground="#A9F1DF")
btn3=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn3),activebackground="#A9F1DF")

btn4=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn4),activebackground="#A9F1DF")
btn5=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn5),activebackground="#A9F1DF")
btn6=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn6),activebackground="#A9F1DF")

btn7=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn7),activebackground="#A9F1DF")
btn8=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn8),activebackground="#A9F1DF")
btn9=Button(width=6,height=2,bg="#1EAE98",font=("Bauhaus 93",30),command=lambda: Click(btn9),activebackground="#A9F1DF")

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)

root.mainloop()