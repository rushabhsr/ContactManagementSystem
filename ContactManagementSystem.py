from tkinter import *
from tkinter import messagebox
import sqlite3


def AddContact():
 
    s1=entry1_addwindow.get()
    s2=entry2_addwindow.get()

#checks if Name is empty
    if s1 == "":
        messagebox.showerror("Contact Management", "Enter proper name")
        return    
    
#Verifing if input number is correctly entered
    try:
        val = int(s2)
    except ValueError:
        messagebox.showerror("Contact Management", "Enter proper number")
        return
    
    conn = sqlite3.connect('Contacts.db')
    print ("Opened database successfully")
    
    conn.execute("INSERT INTO Contacts1 (NAME, NUMBER)  VALUES (?, ?)",(s1,s2));
    conn.commit()
    print ("Records created successfully")
    conn.close()
    entry1_addwindow.delete(0, 'end')
    entry2_addwindow.delete(0, 'end')
    messagebox.showinfo("Contact Management", "Name added successfully")

'''Display'''

def DisplayContact():
    
    DisplayGui=Tk()
    DisplayGui.title("Display Window")
    DisplayGui.geometry("300x300")
    DisplayGui.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
    
    s = Scrollbar(DisplayGui)
    t = Text(DisplayGui , height=4, width=50)
    s.pack(side='right',fill='both')
    t.pack(side='left',fill='both')
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)
    
    conn = sqlite3.connect('Contacts.db')
    print ("Opened database successfully")
    
    
    cursor = conn.execute("SELECT * from Contacts order by name")
    for row in cursor:
        name = row[1]
        number = row[2]
        t.insert('insert', "%s:%s\n"%(name,number))
        
    
    conn.close()
    
    DisplayGui.mainloop()



def SearchContact():
    
    t_swin.delete(1.0, END) 

    flag = 0
    s1 = entry1_swin.get()
    conn = sqlite3.connect('Contacts.db')
    print ("Opened database successfully")
    
    
    cursor = conn.execute("SELECT * from Contacts order by name")
    for row in cursor:
        name = row[1]
        number = row[2]
        if s1 == name:
            t_swin.insert('insert', "%s\n"%(number))
            flag = 1
        
    if flag == 0:
        t_swin.insert('insert', "NO SUCH CONTACT")
    
    conn.close()


def DeleteContact():
    
    s1 = entry1_delwin.get()
    
    
    if s1 == "":
        messagebox.showerror("Contact Management", "Enter proper name")
        return
    
    
    conn = sqlite3.connect('Contacts.db')
    print ("Opened database successfully")
    
    
    conn.execute("DELETE from Contacts where NAME=(?)",(s1,))
    conn.commit()
        
        
    conn.close()
    
    messagebox.showinfo("Contact Management", "Name deleted successfully")

def EditContact():
    
    global x
    flag = 0
   
    conn = sqlite3.connect('Contacts.db')
    print ("Opened database successfully")
    
    if x == 1: 
        s1 = entry1_edwin.get()     #New name
        
    
    else:   
        s1 = entry2_edwin.get()     #New number
        s3 = entry2_ewin.get()      #Old number
        cursor = conn.execute("SELECT * from Contacts order by name")
        for row in cursor:
            abc = str(s3)
            xyz = str(row[2])
            if abc == xyz:
                flag = 1
        if flag == 0:
            messagebox.showinfo("Contact Management", "No such number")
            return
                
        
    ''' OLD NAME '''
    s2 = entry1_ewin.get()          
    
    
    
    
    if x == 1:
        conn.execute("UPDATE Contacts set NAME = (?) where NAME = (?)",(s1,s2))
        conn.commit()
    
    if x == 2:
        conn.execute("UPDATE Contacts set NUMBER = (?) where NAME = (?) AND NUMBER = (?)",(s1,s2,s3))
        conn.commit()
    conn.close()
    messagebox.showinfo("Contact Management", "Edited successfully")


'''Edit if Found window'''
def Editiffoundwindow():
    
    global x
    flag = 0

    conn = sqlite3.connect('Contacts.db')
    print ("Opened database successfully")
    
    if x == 1:
        
        s1 = entry1_ewin.get()
        cursor = conn.execute("SELECT * from Contacts order by name")
        for row in cursor:
            name = row[1]
            if s1 == name:
                flag = 1
    
    if x == 2:
        
        s1 = entry1_ewin.get()
        s2 = entry2_ewin.get()
        cursor = conn.execute("SELECT * from Contacts order by name")
        for row in cursor:
            name = row[1]
            abc = int(s2)
            xyz = int(row[2])
            if (abc == xyz) & (name == s1):
                flag = 1
        
        if flag == 0:
            messagebox.showinfo("Contact Management", "No such name or number")
            return
   
    if flag == 1:
        edwin=Tk()
        edwin.title('Edit Contact')
        edwin.geometry("250x220")
        edwin.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
        edwin.configure(background="gray24")
        
        global label1_edwin
        global label2_edwin
        
        label1_edwin = Label(edwin,text="Enter New Name:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
        label1_edwin.grid(row=0,sticky='E',column=0)
        label2_edwin = Label(edwin,text="Enter New Number:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
        label2_edwin.grid(row=1,sticky='E',column=0)
        
        
        global entry1_edwin
        global entry2_edwin
        
        entry1_edwin= Entry(edwin) 
        entry1_edwin.grid(row=0 , column=1)
        entry2_edwin= Entry(edwin) 
        entry2_edwin.grid(row=1 , column=1)
        button1_swin = Button(edwin, text="Edit",command=EditContact,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
        button1_swin.grid(row=2, column= 1)
        button2_edwin = Button(edwin, text="Cancel",command=edwin.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
        button2_edwin.grid(row=2, column= 0)
        
        edwin.mainloop()
        
    else:
        messagebox.showinfo("Contact Management", "No such name")

def sel(y):
    if y == 1:    #Name
        label1_ewin.configure(text="Enter Name")
        label2_ewin.configure(text=" ")
        label2_edwin.configure(text=" ")
        label1_edwin.configure(text="Enter New Name ") 

       
        entry1_edwin.configure(state = 'normal' )
        entry2_ewin.configure(state = 'disable' )
        entry2_edwin.configure(state = 'disable' )

        
    if y == 2: #Number
        label1_ewin.configure(text="Enter Name")
        label2_ewin.configure(text="Enter Number")
        label2_edwin.configure(text="Enter New Number")
        label1_edwin.configure(text=" ")
        
        
        entry2_ewin.configure(state = 'normal' )
        entry1_edwin.configure(state = 'disable' )
        entry2_edwin.configure(state = 'normal' )
        
def sel1():
    global x
    x = 1
    sel(1)
    
def sel2():
    global x
    x = 2
    sel(2)


'''Edit Window'''
def Editwindow():
    ewin=Tk()
    ewin.title('Edit Contact')
    ewin.geometry("250x220")
    ewin.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
    ewin.configure(background="gray24")
    
    global label1_ewin
    global label2_ewin
    
    label1_ewin = Label(ewin,text="Enter Name:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label1_ewin.grid(row=0,sticky='E',column=0)
    label2_ewin = Label(ewin,text="Enter Number:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label2_ewin.grid(row=1,sticky='E',column=0)
    
    global entry1_ewin
    global entry2_ewin
    
    entry1_ewin= Entry(ewin) 
    entry1_ewin.grid(row=0 , column=1)
    entry2_ewin= Entry(ewin) 
    entry2_ewin.grid(row=1 , column=1)
    
    button1_swin = Button(ewin,command=Editiffoundwindow, text="Edit",bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button1_swin.grid(row=2, column= 1)
    button2_ewin = Button(ewin, text="Cancel",command=ewin.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button2_ewin.grid(row=2, column= 0)
    
    
    global var
    
    var = IntVar()
    
        
    
    R1 = Radiobutton(ewin, text="Name", variable=var, value=1,command=sel1)
    R2 = Radiobutton(ewin, text="Number", variable=var, value=2,command=sel2)
    R1.grid(row=3, column=0)
    R2.grid(row=3, column=1)
    
    R1.select()
    sel(1)
    
    ewin.mainloop()

'''Search Window'''
def Searchwindow():
    swin=Tk()
    swin.title('Search Contacts')
    swin.geometry("500x220")
    swin.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
    swin.configure(background="gray24")
    label1_swin = Label(swin,text="Enter Name:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label1_swin.grid(row=0,sticky='E',column=0)
    global entry1_swin
    entry1_swin= Entry(swin) 
    entry1_swin.grid(row=0 , column=1)
    button1_swin = Button(swin, text="Search",command=SearchContact,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button1_swin.grid(row=2, column= 1)
    button2_swin = Button(swin, text="Cancel",command=swin.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button2_swin.grid(row=2, column= 0)
    
    global s_swin
    global t_swin
    s_swin = Scrollbar(swin)
    t_swin = Text(swin , height=4, width=25)
    s_swin.grid(row=0,column=4,rowspan=11,sticky='ns')
    t_swin.grid(row=0,column=3,rowspan=12)
    s_swin.config(command=t_swin.yview)
    t_swin.config(yscrollcommand=s_swin.set)
    
    
    
    
    swin.mainloop()

'''Delete Window'''
def Deletewindow():
    delwin=Tk()
    delwin.title('Delete Contact')
    delwin.geometry("250x220")
    delwin.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
    delwin.configure(background="gray24")
    label1_delwin = Label(delwin,text="Enter Name:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label1_delwin.grid(row=0,sticky='E',column=0)
    
    global entry1_delwin
    entry1_delwin= Entry(delwin) 
    entry1_delwin.grid(row=0 , column=1)
    button1_delwin = Button(delwin, text="Delete",command=DeleteContact,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button1_delwin.grid(row=2, column= 1)
    button2_delwin = Button(delwin, text="Cancel",command=delwin.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button2_delwin.grid(row=2, column= 0)
    delwin.mainloop()

'''Add Window'''
def Addwindow():
    addwindow=Tk()
    addwindow.geometry("290x250")
    addwindow.title("Adding Contact")
    addwindow.configure(background="gray24")
    addwindow.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
    label1_addwindow = Label(addwindow,text="Enter Name:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label1_addwindow.grid(row=0,sticky='E',column=0)
    global entry1_addwindow
    global entry2_addwindow
    entry1_addwindow= Entry(addwindow) 
    entry1_addwindow.grid(row=0 , column=1)
    label2_addwindow = Label(addwindow,text="Enter Number 1:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label2_addwindow.grid(row=2,sticky='E',column=0)
    entry2_addwindow= Entry(addwindow) 
    entry2_addwindow.grid(row=2 , column=1)
    label3_addwindow = Label(addwindow,text="Enter Numbere 2:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label3_addwindow.grid(row=4,sticky='E',column=0)
    entry3_addwindow= Entry(addwindow) 
    entry3_addwindow.grid(row=4 , column=1)
    label4_addwindow = Label(addwindow,text="Enter Email:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
    label4_addwindow.grid(row=6,sticky='E',column=0)
    entry4_addwindow= Entry(addwindow) 
    entry4_addwindow.grid(row=6 , column=1)
    
    button1_addwindow = Button(addwindow, text="ADD",command=AddContact,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button1_addwindow.grid(row=8, column= 1)
    button2_addwindow = Button(addwindow, text="Cancel",command=addwindow.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=1)
    button2_addwindow.grid(row=8, column= 0)
    
    addwindow.mainloop()
    



root=Tk()
root.title("Contacts Management")
root.geometry("290x250")
root.configure(background="gray24")
root.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
label1_Root= Label(root,text="Contacts Management",font = "Calibri 14 bold underline ",bg='gray24',fg='thistle1' )
 
label1_Root.grid(row=0,sticky="S",columnspan=2)


'''Button creation and addition'''
button1_Root = Button(root , text="Add" ,command=Addwindow,font = "Calibri 10 bold ",bg='gray40',fg='white' ,width=16,height=2)
button2_Root = Button(root , text="Delete",command=Deletewindow,font = "Calibri 10 bold ",bg='gray40',fg='white'  ,width=16,height=2)
button3_Root = Button(root , text="Search" ,command=Searchwindow,font = "Calibri 10 bold ",bg='gray40',fg='white', width=16,height=2)
button4_Root = Button(root , text="Edit" ,command=Editwindow,font = "Calibri 10 bold ",bg='gray40',fg='white',width=16,height=2)
button5_Root = Button(root, text="Quit",command=root.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=2)
button6_Root = Button(root , text="Display" ,command=DisplayContact,font = "Calibri 10 bold ",bg='gray40',fg='white', width=16,height=2)

button1_Root.grid(row=5, column=0)
button2_Root.grid(row=5, column=1)
button3_Root.grid(row=7, column=0)
button4_Root.grid(row=7, column=1)
button5_Root.grid(row=9, column=0)
button6_Root.grid(row=9, column=1)

root.grid_rowconfigure(4, minsize=20)
root.grid_rowconfigure(6, minsize=20)
root.grid_rowconfigure(8, minsize=20)
root.grid_rowconfigure(10, minsize=20)


root.mainloop()

