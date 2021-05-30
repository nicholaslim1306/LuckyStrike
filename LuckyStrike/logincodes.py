from Orbit import *
import mysql.connector
from tkinter import messagebox
from tkinter import *

#SQL add account and validate login
def add_account(user, passw):
    test_query = "SELECT * FROM accounts WHERE username = '%s' "%(user.get())
    results = readQuery(connection,test_query)
    if len(results) == 0 :
            sql_query = "INSERT INTO accounts VALUES ('%s', '%s','%d','%d','%d')"%(user.get(),passw.get(),0,0,0)
            executeQuery(connection, sql_query)
            return messagebox.showinfo(title="Success",message="registration Successful")
            
    else:
            return messagebox.showerror(title="Error",message="Username in use!")



def validate_login(user, passw,window):
        validate_query = "SELECT * FROM accounts WHERE username = '%s' AND password = '%s' "%(user.get(),passw.get())
        results = readQuery(connection,validate_query)
        if len(results) == 0 or  user.get()== "" :
                return messagebox.showerror(title="Error",message="Wrong username/password !")
        else:
            clear_frame(window)

def clear_frame(window):
   for i in Frame(window).winfo_children():
      i.destroy()
