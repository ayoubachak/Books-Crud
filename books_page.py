import sqlite3
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk,ImageOps
from tkcalendar import DateEntry
import tkinter.font as font
# from add_book import add
# from update_book import update

def window():
    global fenetre
    fenetre = Tk()
    fenetre.configure(background="white")
    global tableau
    tableau_frame=Frame(fenetre)
    tableau_frame.pack(side="bottom")
    scroll_frame = Scrollbar(tableau_frame)
    scroll_frame.pack(side="right",fill=Y)
    tableau = ttk.Treeview(tableau_frame, columns=('Title','Number_of_Pages','Borrowed at','To return at'),yscrollcommand=scroll_frame.set)
    scroll_frame.config(command=tableau.yview)
    style = ttk.Style()

    style.theme_use('clam')
    def fixed_map(option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in style.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]

    style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

    # Configure the style of Heading in Treeview widget
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
    
   
    fenetre.title('Books management')



    tableau.tag_configure('a',background="white")
    tableau.tag_configure('b',background="lightblue")
    tableau.heading('Title', text='Title',anchor=CENTER)

    tableau.heading('Number_of_Pages', text='Number_of_Pages',anchor=CENTER)

    tableau.heading('Borrowed at', text='Borrowed at',anchor=CENTER)
    tableau.heading('To return at',text='To return at',anchor=CENTER)

    tableau.column('Title',anchor=CENTER)
    tableau.column('Number_of_Pages',anchor=CENTER)
    tableau.column('Borrowed at',anchor=CENTER)
    tableau.column('To return at',anchor=CENTER)
    tableau.tag_configure('odd',background="green")

    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

    tableau.pack(padx = 10, pady = (0, 10))
    global label_search
    label_search=LabelFrame(fenetre,text="Title",background="lightblue")
    global autre_libelle
    autre_libelle=Entry(label_search,font=("Helvetica",11))
    global libelle
    libelle = Label(fenetre, text = 'Books',font=("Arial",20),background="white")
    

# fenêtre principale
def exit():
    fenetre.destroy()
def create_table():

   conn = sqlite3.connect('project.db')
# cursor object
   cursor = conn.cursor()
# drop query

   
# create query
   query = """CREATE TABLE BOOKS(
        ID INTEGER PRIMARY KEY  NOT NULL,
        TITLE TEXT NOT NULL, 
        PAGES INT, 
        Borrowed_at DATE NULL, 
        Toreturn_at DATE NULL
         )"""
   conn.execute(query)      
   conn.commit()
   conn.close() 
def insert_lines():
    
# cursor object
    
   try: 
        conn = sqlite3.connect('project.db')
        create_table()       
        books = [( 'Game of thrones', 250, '2006-04-05', '2006-04-07'),
                ( 'System d\'exploitation', 114, '2006-04-05', '2006-04-07'),
                ( 'OOP', 115, '2006-04-10', '2006-04-21'),
                ( 'Java', 116, '2006-04-12', '2006-04-15'),
                ( 'C#', 117, '2006-04-05', '2006-04-30'),
                ( 'Lunix', 118, '2006-04-05', '2006-04-30'),
                ( 'C++', 119, '2006-04-10', '2006-04-12'),
                ( 'Javascript', 120, '2006-04-05', '2006-05-07'),
                ( 'HTML', 121, '2006-04-05', '2006-09-05'),
                ( 'CSS', 126, '2006-04-05', '2006-11-1'),
                ( 'C in one day', 127, '2006-04-05', '2006-04-05'),
                ( 'How to be a man', 128, '2006-04-05', '2006-04-25'),
                ( 'Why always me', 129, '2006-04-05', '2006-04-15')
                ]
        conn.executemany('INSERT INTO BOOKS(TITLE,PAGES,Borrowed_at,Toreturn_at) VALUES (?,?,?,?)', books)
        conn.commit()
        conn.close()
   except: return    
def remove_one():

    if(tableau.selection()):   
        books=tableau.selection()
        for i in books:
         curItem = tableau.focus()
         title=tableau.item(curItem)["values"][0]
         pages=tableau.item(curItem)["values"][1]
         
         conn = sqlite3.connect('project.db')
     # cursor object
         cursor = conn.cursor()
         cursor.execute('DELETE FROM books WHERE title=? and pages=?',(title,pages))
         conn.commit()
         
         tableau.delete(i)
    else:
         tkinter.messagebox.showinfo("No selected line","Please select the book you want to delete")
def update_b():
    if(tableau.selection()):  
        curItem = tableau.focus()
        title=tableau.item(curItem)["values"][0]
        pages=tableau.item(curItem)["values"][1]
        borrow_date=tableau.item(curItem)["values"][2]
        return_date=tableau.item(curItem)["values"][2]
        fenetre.destroy()
        
        update(title,pages,borrow_date,return_date)
    else:
         tkinter.messagebox.showinfo("No selected line","Please select the book you want to update")

# The add and the update function were moved just to avoid circular imports 
def add():
    
   

    # font selection
    #hal = font.Font(family='Helvetica', size=20, weight='bold')
    #Creating object 'root' of Tk()
    root = Tk()
    hal = font.Font(family='Helvetica', size=20, weight='bold')
    mhal = font.Font(family='Helvetica', size=10, weight='bold')
    #Providing Geometry to the form
    root.geometry("500x500")

    #image insertion 
    canvas = Canvas(width=600, height=800, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file="images/lib1.jpg")
    canvas.create_image(0, 0, image=image, anchor=NW)


    #Providing title to the form
    root.title('Element Insertion')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Add book", width=20,font=('italic',20))
    label_0.place(x=90,y=60)
    label_0.configure(background="brown")
    label_0['font'] = hal
    # root.wm_attributes("-transparentcolor", '#34A2FE')
    # the first label
    label_1 =Label(root,text="Title:", width=20,font=("bold",10))
    label_1.place(x=80,y=130)
    label_1.configure(background = "#b5651d") # this is light brown
    label_1['font'] = mhal
    #this will accept the input string text from the user.
    global entry_1
    entry_1=Entry(root)
    entry_1.place(x=240,y=130)

    label_2 =Label(root,text="Number of pages:", width=20,font=("bold",10))
    label_2.place(x=80,y=170)
    label_2.configure(background = "#b5651d") # this is light brown
    label_2['font'] =mhal
    #this will accept the input string text from the user.
    global entry_2
    entry_2=Entry(root)
    entry_2.place(x=240,y=170)

    #this is the due date
    label_3 =Label(root,text="Borrow date:", width=20,font=("bold",10))
    label_3.place(x=80,y=210)
    label_3.configure(background = "#b5651d") # this is light brown
    label_3['font'] = mhal
    # this is just a test calender
    global cal1
    cal1 = DateEntry(root, width=12, year=2019, month=6, day=22, 
    background='darkblue', foreground='white', borderwidth=2)
    cal1.place(x=240,y=210)
    # this is the due date
    label_4 =Label(root,text="Due date:", width=20,font=("bold",10))
    label_4.place(x=80,y=250)
    label_4.configure(background = "#b5651d") # this is light brown
    label_4['font'] = mhal
    # this is just a test calender
    global cal2
    cal2 = DateEntry(root, width=12, year=2019, month=6, day=22,
    background='darkblue', foreground='white', borderwidth=2)
    cal2.place(x=240,y=250)


    #this creates button for submitting the details provides by the user
    def insert():
        title=entry_1.get()
        
        nbpages=int(entry_2.get())
    
        borrow=cal1.get_date()
        return_date=cal2.get_date()
        conn = sqlite3.connect('project.db')
        books = [ title, nbpages , borrow , return_date ]
        conn.execute('INSERT INTO BOOKS(TITLE,PAGES,Borrowed_at,Toreturn_at) VALUES (?,?,?,?)', books)
        conn.commit()
        conn.close()
        root.destroy()
        main()
        
        

    Button(root, text='Create' , width=20,bg="black",fg='white',command=insert).place(x=180,y=380)

    #this will run the mainloop.
    root.mainloop()

def update(title,pages,borrow_at,return_at):
    
   

    # font selection
    #hal = font.Font(family='Helvetica', size=20, weight='bold')
    #Creating object 'root' of Tk()
    root = Tk()
    hal = font.Font(family='Helvetica', size=20, weight='bold')
    mhal = font.Font(family='Helvetica', size=10, weight='bold')
    #Providing Geometry to the form
    root.geometry("500x500")

    #image insertion 
    canvas = Canvas(width=600, height=800, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file="images/lib1.jpg")
    canvas.create_image(0, 0, image=image, anchor=NW)


    #Providing title to the form
    root.title('Book update')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Update book", width=20,font=('italic',20))
    label_0.place(x=90,y=60)
    label_0.configure(background="orange")
    label_0['font'] = hal
    # root.wm_attributes("-transparentcolor", '#34A2FE')
    # the first label
    label_1 =Label(root,text="Title:", width=20,font=("bold",10))
    label_1.place(x=80,y=130)
    label_1.configure(background = "#b5651d") # this is light brown
    label_1['font'] = mhal
    #this will accept the input string text from the user.
    global entry_1
    entry_1=Entry(root)
    entry_1.place(x=240,y=130)
    entry_1.insert(0,title)

    label_2 =Label(root,text="Number of pages:", width=20,font=("bold",10))
    label_2.place(x=80,y=170)
    label_2.configure(background = "#b5651d") # this is light brown
    label_2['font'] =mhal
    #this will accept the input string text from the user.
    global entry_2
    entry_2=Entry(root)
    entry_2.place(x=240,y=170)
    entry_2.insert(0,pages)

    #this is the due date
    label_3 =Label(root,text="Borrow date:", width=20,font=("bold",10))
    label_3.place(x=80,y=210)
    label_3.configure(background = "#b5651d") # this is light brown
    label_3['font'] = mhal
    # this is just a test calender
    global cal1
    data = borrow_at.split("-")
    
    cal1 = DateEntry(root, width=12, year=int(data[0]), month=int(data[1]), day=int(data[2]), 
    background='darkblue', foreground='white', borderwidth=2)
    cal1.place(x=240,y=210)
    cal1
    # this is the due date
    label_4 =Label(root,text="Due date:", width=20,font=("bold",10))
    label_4.place(x=80,y=250)
    label_4.configure(background = "#b5651d") # this is light brown
    label_4['font'] = mhal
    # this is just a test calender
    global cal2
    data = return_at.split("-")
    cal2 = DateEntry(root, width=12, year=int(data[0]), month=int(data[1]), day=int(data[2]),
    background='darkblue', foreground='white', borderwidth=2)
    cal2.place(x=240,y=250)


    #this creates button for submitting the details provides by the user
    def insert():
        title_new=entry_1.get()
        
        try:
            nbpages=int(entry_2.get())
        
        except :      
            tkinter.messagebox.showerror("Number is integer","Please enter  a number in number of pages ")
            return  
        borrow=cal1.get_date()
        return_date=cal2.get_date()
        conn = sqlite3.connect('project.db')
        query="UPDATE   BOOKS SET title='"+title_new+"',pages="+str(nbpages)+",Borrowed_at='"+str(borrow)+"',Toreturn_at='"+str(return_date)+"' where title='"+title+"' and pages="+str(pages)+" and Borrowed_at='"+str(borrow_at)+"' and Toreturn_at='"+str(return_at)+"'"
        
        conn.execute(query)
        conn.commit()
        conn.close()
        root.destroy()
        main()
        

    Button(root, text='Update' , width=20,bg="black",fg='white',command=insert).place(x=180,y=380)

    #this will run the mainloop.
    root.mainloop()



def remove_all():
    for i in tableau.get_children():
        tableau.delete(i)
    conn = sqlite3.connect('project.db')
     # cursor object
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books ')
    conn.commit()
    conn.close()
    #search 


def search_book():
    conn = sqlite3.connect('project.db')
# cursor object
    cursor = conn.cursor()
    for i in tableau.get_children():
        tableau.delete(i)
    search_value=autre_libelle.get()
    if(search_value == ""):
      tkinter.messagebox.showinfo("Empty Search","Please make sure you enter a word in search zone")
      
    conn.row_factory=sqlite3.Row
    search_value+='%'
    cursor=conn.execute('select title,pages,borrowed_at,toreturn_at from BOOKS where title LIKE  ?', (search_value,) )
    count=0
    if(cursor):
        for row in cursor:
            if count % 2 == 0:
                tableau.insert('', 'end',iid=count, values=(row["title"],row["PAGES"],row["Borrowed_at"],row["Toreturn_at"]),tags=("a",))
            else:
                 tableau.insert('', 'end',iid=count, values=(row["title"],row["PAGES"],row["Borrowed_at"],row["Toreturn_at"]),tags=("b",))
            count+=1    
    else:


        libelle.configure(text = 'Il n\'y a présentement aucun livre.')

        tableau.pack_forget()
    
    conn.commit()
    conn.close()

def read():
#Affichage des livres
   conn = sqlite3.connect('project.db')
# cursor object
    
   for i in tableau.get_children():
        tableau.delete(i)
   conn.row_factory=sqlite3.Row
   cursor=conn.execute("select title,pages,borrowed_at,toreturn_at from BOOKS ORDER BY title,pages")
   count=0
   if(cursor):
      for row in cursor:
        if count % 2 == 0:
                tableau.insert('', 'end', values=(row["title"],row["PAGES"],row["Borrowed_at"],row["Toreturn_at"]),tags=('book','a'))
        else:
                 tableau.insert('', 'end', values=(row["title"],row["PAGES"],row["Borrowed_at"],row["Toreturn_at"]),tags=('book','b'))
        count+=1    
   else:
        libelle.configure(text = 'Il n\'y a présentement aucun livre.')

        tableau.pack_forget()
   conn.commit()  
   conn.close()  
    
def add_book():
    fenetre.destroy()
    j=1
    add()

    
    
        








# libellé

def lib():
    libelle.pack(padx = 10, pady = 10)



    label_search.pack(padx=10,pady=10)

    autre_libelle.pack(padx = 10 , pady= 5)
    button_search=Button(fenetre,text="Search",padx=3,pady=3,bg="lightblue",command=search_book).pack(padx = 10,pady=5)





'''
tableau.tag_configure("image1",image=img)
'''


# Connect to sqlite database


def Menus():
    #Menu
    menu_bar = Menu(fenetre)
    menu_action = Menu(menu_bar, tearoff=0)
    menu_action.add_command(label="Add")
    menu_action.add_command(label="Update")
    menu_action.add_command(label="Delete",command=remove_one)
    menu_action.add_command(label="Delete All",command=remove_all)
    menu_action.add_separator()
    menu_action.add_command(label="Exit",command=exit)
    menu_bar.add_cascade(label="Action", menu=menu_action)

    menu_refresh = Menu(menu_bar, tearoff=0)
    menu_refresh.add_command(label="Refresh",command=read)
    menu_bar.add_cascade(label="Refresh", menu=menu_refresh)

    menu_exit = Menu(menu_bar, tearoff=0)
    fenetre.config(menu=menu_bar)
    

#Boutons
def buttons():
    frame=Frame(fenetre).pack(padx=10)
    Button(frame,text="ADD",padx=5,fg="brown",command=add_book).pack(side="left",padx=10,pady=5)
    Button(frame,text="UPDATE",padx=5,fg="orange",command=update_b).pack(side="left",padx=5,pady=5)
    Button(frame,text="DELETE",padx=5,fg="red",command=remove_one).pack(side="left",padx=5,pady=5)
    Button(frame,text="DELETE ALL",padx=5,fg="black",command=remove_all).pack(side="right",padx=30,pady=5)


def afficher():
   fenetre.mainloop()
#functions CRUD
def main():
    window()
    image=Image.open("images/Library.jpg")
    image = ImageOps.expand(image,border=5,fill='lightblue')
    
    image = image.resize((800, 150), Image.ANTIALIAS)
    backg=ImageTk.PhotoImage(image)
    background_label = Label(fenetre, image=backg)
            #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.pack()
    insert_lines()
    read()
    lib()
    Menus()
    buttons()
    afficher()
if __name__ == '__main__':
    main()



