import time
from tkinter import *
from tkinter.font import names
import pyautogui

def ss():
    '''name = 'pooja.png'
    time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()
'''
    name = int(round(time.time() * 1000))
    name = 'Image' + '{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()

def delay():
    root.withdraw()
    root.after(1000,ss)


root = Tk()
root.title('Screenshot')
root['bg'] = 'pink'
root.geometry('700x500')
root.resizable(0,0)
btn1 = Button(root,text='Take Screenshot',font=('Arial',15,'bold'),height=2, width=18, fg= 'blue',bg='orange',command=delay).place(x=250, y = 50)
btn2 = Button(root,text='Quit',font=('Arial',15,'bold'),height=2, width=18,  fg= 'blue',bg='orange',command=quit).place(x=250, y = 140)



root.mainloop()
