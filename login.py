import books_page
from tkinter import *
import sqlite3
from functools import partial



class Login:
    def __init__(self,main) -> None:
        main.title("Login")
        main.geometry('300x500')
        main.resizable(0, 0)
        self.i=0
        # Image (lock)
        self.canvas=Canvas(main, width=300, height=300)
        self.image=PhotoImage(file='images/user.png')
        self.canvas.create_image(100,50,anchor=NW, image=self.image)        
        self.canvas.pack()
        self.t=[]
         # Entries
        self.username =StringVar()
        label_user =Label(main, text="Username", font=("Arial", 12)).place(x=35, y=210)
        self.entry_user =Entry(main, width=40, textvariable=self.username)
        self.entry_user.place(x=35,y=240)
        self.password = StringVar()
        label_pass = Label(main, text="Password", font=("Arial", 12)).place(x=35, y=270)
        self.entry_passwd = Entry(main, width=40, textvariable=self.password, show="*")
        self.entry_passwd.place(x=35,y=300)
        self.validateLogin = partial(self.validateLogin, self.username, self.password)
        button_login = Button(main, text="Login", font=("Arial", 12),command=self.validateLogin).place(x=35, y=350)
        button_register = Button(main, text="Register", font=("Arial", 12),command=self.register).place(x=210,y=350)
        
    # Database
    def connect(self):
        self.db= sqlite3.connect("project.db")
        self.c=self.db.cursor()
      
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS  admin (
            id  integer PRIMARY KEY AUTOINCREMENT,
            identifiant text,
            mdp text,
            email text
        )""")
        self.db.commit()
        self.newaccount()
    def newaccount(self):
        self.c.execute(f"INSERT INTO admin(identifiant,mdp,email) VALUES ('{self.eentry_user.get()}','{self.eentry_passwd.get()}','{self.email_entry.get()}')")
        self.c.execute("SELECT * FROM admin")
        self.db.commit()
        self.t=self.c.fetchall()
        print(self.t)
        return self.t 
           # creer un account
    def list2check(self):
        self.db= sqlite3.connect("project.db")
        self.c=self.db.cursor()
        self.c.execute("SELECT * FROM admin")
        self.t=self.c.fetchall()
     
       
       
    def register(self):
        self.registry_win = Toplevel()
        self.registry_win.title('Registry')
        self.registry_win.iconbitmap('images/register.ico')
        self.registry_win.geometry("300x350")
        self.registry_win.resizable(0, 0)

        title_label = Label(self.registry_win, text="Registry", font=("Arial", 20), fg="black").place(x=90,
                                                                                                         y=0)
        self.email = StringVar()
        email_label = Label(self.registry_win, text="Email:", font=("Arial", 12)).place(x=20, y=50)
        self.email_entry = Entry(self.registry_win, width=30, textvariable=self.email)
        self.email_entry.place(x=100, y=51)
        self.username = StringVar()
        label_user = Label(self.registry_win, text="Username:", font=("Arial", 12)).place(x=20, y=90)
        self.eentry_user = Entry(self.registry_win, width=30, textvariable=self.username)
        self.eentry_user.place(x=100,y=91)
        self.password = StringVar()
        label_pass = Label(self.registry_win, text="Password:", font=("Arial", 12)).place(x=20, y=130)
        self.eentry_passwd = Entry(self.registry_win, width=30, textvariable=self.password, show="*")
        self.eentry_passwd.place(x=100,y=131)
        button_new = Button(self.registry_win, text="New", font=("Arial", 12), ).place(x=20, y=200)

        button_registry_sql = Button(self.registry_win, text="Register", font=("Arial", 12),command=self.connect
                                        ).place(x=210,
                                                                         y=200)
    def droptable(self):
        self.list2check()
        self.c.execute("DROP TABLE admin")
    def checkk(self,username, password):
       self.list2check()
   
       for i in self.t:
            A=username.get()
            B=password.get()
            if A==i[1]:
                if B==i[2]:
                    return True
       return False


    def validateLogin(self,username, password ) :
    
        d=self.checkk(username, password)

        if d:
           
           window.destroy() 
           books_page.main()
           
        else : 
            print("sad")
            
    def trythis(self,i):
        self.i=i
        self.list2check()
       
        try:
            name1=Entry(self.root,width=30)
            name1.insert(0,self.t[1-1][1])
            name1.place(x=20,y=20+35*1)
            delete=Button(self.root,text="delete",command=self.deletuser1)

            delete.place(x=220,y=18+35*1)
            name2=Entry(self.root,width=30)
    
            name2.insert(0,self.t[2-1][1])
            name2.place(x=20,y=20+35*2)
            delete=Button(self.root,text="delete",command=self.deletuser2)

            delete.place(x=220,y=18+35*2)
            name3=Entry(self.root,width=30)
    
            name3.insert(0,self.t[3-1][1])
            name3.place(x=20,y=20+35*3)
            delete=Button(self.root,text="delete",command=self.deletuser3)

            delete.place(x=220,y=18+35*3)
            name4=Entry(self.root,width=30)
    
            name4.insert(0,self.t[4-1][1])
            name4.place(x=20,y=20+35*4)
            delete=Button(self.root,text="delete",command=self.deletuser4)

            delete.place(x=220,y=18+35*4)
            name5=Entry(self.root,width=30)
    
            name5.insert(0,self.t[5-1][1])
            name5.place(x=20,y=20+35*5)
            delete=Button(self.root,text="delete",command=self.deletuser5)

            delete.place(x=220,y=18+35*5)

            name6=Entry(self.root,width=30)
    
            name6.insert(0,self.t[6-1][1])
            name6.place(x=20,y=20+35*6)
            delete=Button(self.root,text="delete",command=self.deletuser6)

            delete.place(x=220,y=18+35*6)
            name7=Entry(self.root,width=30)
    
            name7.insert(0,self.t[7-1][1])
            name7.place(x=20,y=20+35*7)
            delete=Button(self.root,text="delete",command=self.deletuser7)

            delete.place(x=220,y=18+35*7)
            name8=Entry(self.root,width=30)
    
            name8.insert(0,self.t[8-1][1])
            name8.place(x=20,y=20+35*8)
            delete=Button(self.root,text="delete",command=self.deletuser8)

            delete.place(x=220,y=18+35*8)
            name9=Entry(self.root,width=30)
    
            name9.insert(0,self.t[9-1][1])
            name9.place(x=20,y=20+35*9)
            delete=Button(self.root,text="delete",command=self.deletuser9)

            delete.place(x=220,y=18+35*9)
        except :
            pass
     
    def modifyusers(self):
        self.list2check()
        self.root=Tk()
        self.root.title('Registry')
        self.root.iconbitmap('images/register.ico')
        self.root.geometry("400x450")
        self.root.resizable(0, 0)
        buttonta7t=Button(self.root,text="drop everything",command=self.droptable)
        buttonta7t.place(x=280,y=380)
   

        print(len(self.t))
        for i in range(1,len(self.t)+1):
            self.trythis(i)
        

    def deletuser1(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=1")
        print("xd")
        self.db.commit()
    def deletuser2(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=2")
        print("xd")
        self.db.commit()
    def deletuser3(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=3")
        print("xd")
        self.db.commit()
    def deletuser4(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=4")
        print("xd")
        self.db.commit()
    def deletuser5(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=5")
        print("xd")
        self.db.commit()
    def deletuser6(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=6")
        print("xd")
        self.db.commit()
    def deletuser7(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=7")
        print("xd")
        self.db.commit()
    def deletuser8(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=8")
        print("xd")
        self.db.commit()
    def deletuser9(self):
        self.list2check()
        self.c.execute("DELETE FROM admin WHERE id=9")
        print("xd")
        self.db.commit()


window=Tk()
t=Login(window)
t.modifyusers()



window.mainloop()