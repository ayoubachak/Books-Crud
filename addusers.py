from tkinter import *
import sqlite3
db= sqlite3.connect("booksks.db")
c=db.cursor()
c.execute("""DROP TABLE IF EXISTS books;
""")
c.execute("""
CREATE TABLE  books (
	identifiant text,
	mdp text
 
  




	)""")
def newaccount():
    c.execute(f"INSERT INTO books(identifiant,mdp) VALUES ('{usernameEntry.get()}','{passwordEntry.get()}')")
    c.execute("SELECT * FROM books")
    global t
    t=c.fetchall()
    
    print()
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel1 = Label(tkWindow, text="ADD USERS").grid(row=0, column=1)
usernameLabel = Label(tkWindow, text="email").grid(row=1, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.grid(row=1, column=1)  
usernameEntry.focus_set()
#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.grid(row=2, column=1)  
passwordEntry.focus_set()
adduser = Button(tkWindow, text="join!", command=newaccount).grid(row=4, column=0) 
tkWindow.mainloop()

