from tkinter import *
from tkinter import messagebox
import mysql.connector
import Projectcode 

class login:
    def __init__(self, w) :
        self.w = w
        self.w.geometry('450x600')
        self.w.title("L O G I N")
        self.w.resizable(0, 0)

        #=============variables=================
        self.username = StringVar()
        self.password = StringVar()

        j=0
        r=0
        for i in range(100):
            c = str(222222+r)
            Frame(w,width=10,height=600,bg='#'+c).place(x=j,y=0)
            j=j+10
            r=r+1

        Frame(self.w, width = 350, height = 500, bg = 'white').place(x = 50, y = 50)
        self.l = ('consolas', 13)
        #==============Username Label=============
        self.l1 = Label(self.w, text = 'Username', bg = 'white')
        
        self.l1.config(font = self.l)
        self.l1.place(x = 80, y = 200)

        self.e1 = Entry(self.w, width = 20, border = 0, textvariable=self.username)
        self.e1.config(font = self.l)
        self.e1.place(x = 80, y = 230)

        #=============Password Label===========
        self.l2 = Label(self.w, text = 'Password', bg = 'white')
        self.l2.config(font = self.l)
        self.l2.place(x = 80, y = 280)

        self.e2 = Entry(self.w, width = 20, border = 0, show = "*", textvariable = self.password)
        self.e2.config(font = self.l)
        self.e2.place(x = 80, y = 310)

        Frame(self.w, width = 180, height = 2, bg = '#141414').place(x = 80, y = 250)
        Frame(self.w, width = 180, height = 2, bg = '#141414').place(x = 80, y = 330)

        Button(self.w, width = 20, height = 2, fg = 'white', bg = '#994422', border = 0, command = self.cmd, text = "L 0 G I N").place(x = 100, y = 375)
    
    def cmd(self):
        conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
        cur = conn.cursor()
        cur.execute("select uid,pass from login")
        data = cur.fetchall()
        uname = self.username.get()
        passwd = self.password.get()
        if uname.lower() == "admin" :
            cur.execute("select pass from login where uid = 'admin'")
            log = cur.fetchone()
            if log[0] == passwd :
                messagebox.showinfo('LOGIN SUCCESSFULL',"      WELCOME ADMIN     ")
                Projectcode.PharmacyManagementSystem(w)
        else :
            for i in data:
                if uname == i[0] and passwd == i[1] :
                        pass
                else:
                    self.username.set("")
                    self.password.set("")
                    messagebox.showinfo("LOGIN FAILED","        PLEASE TRY AGAIN        ")

        conn.close()

if __name__ == "__main__":
    w = Tk()
    obj = login(w)
    w.mainloop()