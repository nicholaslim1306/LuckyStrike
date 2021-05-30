from tkinter import *
from Orbit import *
from tkinter import messagebox
from functools import partial
from logincodes import add_account,validate_login


def login():
    global username
    global password

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
               window.destroy()
               import homepage

    
    #window
    login_window = Tk()  
    login_window.geometry('400x400')  
    login_window.title('LuckyStrike')

    #background
    img = PhotoImage(file="Untitled.png")
    label = Label(
        login_window,
        image=img
    )
    label.place(x=0, y=0)

    #username label and text entry box
    usernameLabel = Label(login_window, text="Username",fg="white",bg="purple")
    usernameLabel.place(x=100,y=200)
    username = StringVar()
    usernameEntry = Entry(login_window, textvariable=username)
    usernameEntry.place(x=170,y=200)

    #password label and password entry box
    passwordLabel = Label(login_window,text="Password",fg="white",bg="purple")
    passwordLabel.place(x=100,y=225)
    password = StringVar()
    passwordEntry = Entry(login_window, textvariable=password, show='*')
    passwordEntry.place(x=170,y=225)

    #validate login and account creation
    validatelogin = partial(validate_login, username, password,login_window)
    addaccount = partial(add_account,username,password)

    #login button
    loginButton = Button(login_window, text="Login", command=validatelogin, fg ="white",bg="green")
    loginButton.place(x =150,y=250)

    #register button
    registerButton = Button(login_window, text="Register", command=addaccount, fg ="white",bg="green")
    registerButton.place(x=250,y=250)
    
    login_window.mainloop()

login()
