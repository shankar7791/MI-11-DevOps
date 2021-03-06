import tkinter.messagebox
from tkinter import*
from typing import Sized

root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Toc Toe")
root.configure(background='cadet Blue')

Tops = Frame(root, bg = 'cadet Blue',pady=2,width=1350,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)

lblTitle= Label(Tops,font=('arial',85,'bold'),text="***Advanced Tic Tac Toe Game***",bd=21,bg='orange',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root, bd=10, bg = 'Powder Blue',pady=2,width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame, bd=10,bg = 'Cadet Blue',padx=10,pady=2,width=750,height=500,relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10,bg='Cadet Blue',padx=10,pady=2,width=560,height=500,relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bg = 'Cadet Blue',bd=10,width=560,height=200,relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame,bg = 'Cadet Blue',bd=10,width=560,height=200,relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX = IntVar()
Player0 = IntVar()

PlayerX.set(0)
Player0.set(0)

button = StringVar()
click = True

def checker(buttons) :
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    if buttons["text"] == " " and click == False:
        buttons["text"] = "0"
        click = True
        scorekeeper()


def scorekeeper() :
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background= "powder blue")
        button2.configure(background= "powder blue")
        button3.configure(background= "powder blue")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background= "Red")
        button5.configure(background= "Red")
        button6.configure(background= "Red")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background= "Cadet Blue")
        button8.configure(background= "Cadet Blue")
        button9.configure(background= "Cadet Blue")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background= "Cadet Blue")
        button5.configure(background= "Cadet Blue")
        button7.configure(background= "Cadet Blue")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background= "Red")
        button5.configure(background= "Red")
        button9.configure(background= "Red")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background= "yellow")
        button4.configure(background= "yellow")
        button7.configure(background= "yellow")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background= "pink")
        button5.configure(background= "pink")
        button8.configure(background= "pink")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background= "cadet blue")
        button6.configure(background= "cadet blue")
        button9.configure(background= "cadet blue")

        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    
    if (button1["text"]=="0" and button2["text"]=="0" and button3["text"]=="0"):
        button1.configure(background= "powder blue")
        button2.configure(background= "powder blue")
        button3.configure(background= "powder blue")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button4["text"]=="0" and button5["text"]=="0" and button6["text"]=="0"):
        button4.configure(background= "Red")
        button5.configure(background= "Red")
        button6.configure(background= "Red")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button7["text"]=="0" and button8["text"]=="0" and button9["text"]=="0"):
        button7.configure(background= "Cadet Blue")
        button8.configure(background= "Cadet Blue")
        button9.configure(background= "Cadet Blue")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button3["text"]=="0" and button5["text"]=="0" and button7["text"]=="0"):
        button3.configure(background= "Cadet Blue")
        button5.configure(background= "Cadet Blue")
        button7.configure(background= "Cadet Blue")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button1["text"]=="0" and button5["text"]=="0" and button9["text"]=="0"):
        button1.configure(background= "Red")
        button5.configure(background= "Red")
        button9.configure(background= "Red")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button1["text"]=="0" and button4["text"]=="0" and button7["text"]=="0"):
        button1.configure(background= "yellow")
        button4.configure(background= "yellow")
        button7.configure(background= "yellow")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button2["text"]=="0" and button5["text"]=="0" and button8["text"]=="0"):
        button2.configure(background= "pink")
        button5.configure(background= "pink")
        button8.configure(background= "pink")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")

    if (button3["text"]=="0" and button6["text"]=="0" and button9["text"]=="0"):
        button3.configure(background= "cadet blue")
        button6.configure(background= "cadet blue")
        button9.configure(background= "cadet blue")

        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0", "You have just won a game")


def reset() :
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(background= "gainsboro")
    button2.configure(background= "gainsboro")
    button3.configure(background= "gainsboro")
    button4.configure(background= "gainsboro")
    button5.configure(background= "gainsboro")
    button6.configure(background= "gainsboro")
    button7.configure(background= "gainsboro")
    button8.configure(background= "gainsboro")
    button9.configure(background= "gainsboro")

def NewGame () :
    reset ()
    PlayerX.set(0)
    Player0.set(0)


lblPlayerX = Label(RightFrame1, font=('arial',40,'bold'),text="Player X:",padx=2,pady=2, bg="Cadet Blue")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font=('arial',40,'bold'), bd=2, fg="black",textvariable=PlayerX, width=14,
                justify=LEFT).grid(row=0,column=1)

lblPlayer0= Label(RightFrame1, font=('arial',40,'bold'),text="Player 0:",padx=2,pady=2, bg="Cadet Blue")
lblPlayer0.grid(row=1, column=0, sticky=W)
txtPlayer0 = Entry(RightFrame1, font=('arial',40,'bold'), bd=2, fg="black",textvariable=Player0, width=14,
                justify=LEFT).grid(row=1,column=1)

btnReset = Button(RightFrame2, text="Reset",font=('arial',40,'bold'),height=2, width=20, command= reset)
btnReset.grid(row=2, column=0, padx=6, pady=11)

btnNewGame = Button(RightFrame2, text="New Game",font=('arial',40,'bold'),height=2, width=20,command= NewGame)
btnNewGame.grid(row=3, column=0,  padx=6, pady=10)



button1 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button1) )
button1.grid(row=1, column=0, sticky= S+N+E+W)

button2 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button2))
button2.grid(row=1, column=1, sticky= S+N+E+W)

button3 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button3))
button3.grid(row=1, column=2, sticky= S+N+E+W)

button4 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button4))
button4.grid(row=2, column=0, sticky= S+N+E+W)

button5 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button5))
button5.grid(row=2, column=1, sticky= S+N+E+W)

button6 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button6))
button6.grid(row=2, column=2, sticky= S+N+E+W)

button7 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button7))
button7.grid(row=3, column=0, sticky= S+N+E+W)

button8 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button8))
button8.grid(row=3, column=1, sticky= S+N+E+W)

button9 = Button(LeftFrame, text=" ",font=('Times 26 bold'),height=3, width=8, bg='gainsboro', command = lambda:checker(button9))
button9.grid(row=3, column=2, sticky= S+N+E+W)

root.mainloop()