import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkvideo import *
import sqlite3
import os


root = Tk()
root.title('Login Page')
root.geometry("1024x720")
root.resizable(0,0)


# Placing a Background Image for the login page
login_bg = Image.open("D:/Python Final Assignment/login_reg_imgs/back.jpeg")
login_bg = login_bg.resize((1024,720), Image.ANTIALIAS)
log_bg = ImageTk.PhotoImage(login_bg)
log_img_label = Label(image = log_bg)
log_img_label.place(x=0,y=0)


# Creating the login portal
# Creating User Entry
username_label = Label(root, bg="grey", fg="#e0dfdc", text="Username: ", font=("Times New Roman", 21, "bold")).place(x=30, y=250)

username = Entry(root, width=18, borderwidth=0, fg="#e0dfdc", bg="grey", font=("Times New Roman", 23, "bold"), justify=CENTER)
username.place(x=170, y=250)

# Creating Password Entry
password_label = Label(root, bg="grey", fg="#e0dfdc", text="Password : ", font=("Times New Roman", 21, "bold")).place(x=30, y=300)

password = Entry(root, width=18, borderwidth=0, fg="#c4c0b5", bg="grey", font=("Times New Roman", 23, "bold"), justify=CENTER)
# Making the password invisible and showing *
password.config(show="*")

password.place(x=170, y=300)


# For User Login
def login_successful():
    messagebox.showinfo("User Logged In", "You have logged in successfully")
    root.destroy()
    os.system("python user_order_page.py")



def try_login():
    '''Used for user login '''
    conn = sqlite3.connect('D:/Python Final Assignment/Database/registration.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM reg_data")
    records = c.fetchall()

    name = username.get()
    pwd = password.get()
    # Loop through the results
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[3]) + ' ' + '\t' + str(record[4]) + "\n"
        user_log = str(record[0]) + ' ' + str(record[1])
        if user_log != name or record[3] != pwd or record[4] != pwd:
            # login_unsuccessful
            continue
        elif user_log == name and record[3] == pwd and record[4] == pwd:
            login_successful()


def registration_page():
    '''Used for registering new users for the restaurant'''
    root.destroy()
    from tkinter import Tk
    from PIL import ImageTk, Image
    from tkinter import messagebox
    from tkvideo import tkvideo

    import sqlite3

    reg_page = Tk()
    reg_page.title('Registration Page')
    reg_page.geometry("1024x720")
    reg_page.resizable(0, 0)

    # Placing a Background Image for the login page
    item1_img = Image.open("D:/Python Final Assignment/login_reg_imgs/reg_1.jpg")
    item1_img = item1_img.resize((1024, 720), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(item1_img)
    item1_img_label = Label(image=image1)
    item1_img_label.place(x=0, y=0)

    # Creating a database or connect to one
    conn = sqlite3.connect('D:/Python Final Assignment/Database/registration.db')

    # Create Cursor
    c = conn.cursor()

    '''
    # Create Table for storing registration details

    c.execute(""" CREATE TABLE reg_data(
            user_first_name text, 
            user_last_name text,
            user_address text,
            user_pass text,
            user_confirm_pass text   
    )
    """)
    # def popup():
    #     # Showinfo messagebox
    messagebox.showinfo("User Registration Table Created Successfully", "You can now add the data")
    '''

    # Creating text boxes
    new_reg_label = Label(reg_page, width=27, bg="#49f2f5", fg="#003e53", text="New Registration",
                          font=("Times New Roman", 25, "bold")).place(x=450, y=300)

    f_name_label = Label(reg_page, width=13, bg="grey", fg="#e0dfdc", text="First Name",
                         font=("Times New Roman", 21, "bold")).place(x=450, y=400)
    f_name = Entry(reg_page, width=20, borderwidth=0, fg="#e0dfdc", bg="grey", font=("Times New Roman", 23, "bold"),
                   justify=CENTER)
    f_name.place(x=680, y=400)

    l_name_label = Label(reg_page, width=13, bg="grey", fg="#e0dfdc", text="Last Name",
                         font=("Times New Roman", 21, "bold")).place(x=450, y=450)
    l_name = Entry(reg_page, width=20, borderwidth=0, fg="#e0dfdc", bg="grey", font=("Times New Roman", 23, "bold"),
                   justify=CENTER)
    l_name.place(x=680, y=450)

    address_label = Label(reg_page, width=13, bg="grey", fg="#e0dfdc", text="Address",
                          font=("Times New Roman", 21, "bold")).place(x=450, y=500)
    address = Entry(reg_page, width=20, borderwidth=0, fg="#e0dfdc", bg="grey", font=("Times New Roman", 23, "bold"),
                    justify=CENTER)
    address.place(x=680, y=500)

    password_label = Label(reg_page, width=13, bg="grey", fg="#e0dfdc", text="Password",
                           font=("Times New Roman", 21, "bold")).place(x=450, y=550)
    password = Entry(reg_page, width=20, borderwidth=0, fg="#e0dfdc", bg="grey", font=("Times New Roman", 23, "bold"),
                     justify=CENTER)
    password.place(x=680, y=550)

    confirm_password_label = Label(reg_page, width=13, bg="grey", fg="#e0dfdc", text="Confirm Password",
                                   font=("Times New Roman", 21, "bold")).place(x=450, y=600)
    confirm_password = Entry(reg_page, width=20, borderwidth=0, fg="#e0dfdc", bg="grey",
                             font=("Times New Roman", 23, "bold"), justify=CENTER)
    confirm_password.place(x=680, y=600)

    # Adding Video
    reg_vdo = Label(reg_page)
    reg_vdo.place(x=450, y=50)
    player = tkvideo("D:/Python Final Assignment/Video/reg_vdo.mp4", reg_vdo, loop=1, size=(540, 240))
    player.play()

    # Creating a  submit button for the database
    def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('D:/Python Final Assignment/Database/registration.db')
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO reg_data VALUES (:f_name, :l_name, :address, :password, :confirm_password)", {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'password': password.get(),
            'confirm_password': confirm_password.get()
        })

        conn.commit()
        conn.close()

        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        password.delete(0, END)
        confirm_password.delete(0, END)

        messagebox.showinfo("User Data", "YOUR DATA IS REGISTERED")
        reg_page.destroy()
        os.system("python index.py")


    # Creating a function for showing the records to check if the data is being stored

    def view_records():
        # Creating a database or connect to one
        conn = sqlite3.connect('D:/Python Final Assignment/Database/registration.db')
        # Create Cursor
        c = conn.cursor()
        # Query of the databse
        c.execute("SELECT *, oid FROM reg_data")
        records = c.fetchall()
        print(records)
        conn.commit()
        conn.close()

    def quit_reg():
        response = messagebox.askyesno("QUIT???", "Are You Sure You Wan't To Quit ?")
        if response == 1:
            reg_page.destroy()
            os.system("python index.py")
        else:
            pass


    # Creating a submit button
    # Two submit buttons

    # 1st Button : Button with hovering effect on the buttons

    # Making function to create the hovering effect
    def on_submit_enter(e):
        submit_button.config(background='OrangeRed3', foreground="white")

    def on_submit_leave(e):
        submit_button.config(background='grey', foreground='#98eced')

    def on_cancel_enter(f):
        reg_cancel.config(background='OrangeRed3', foreground="white")

    def on_cancel_leave(f):
        reg_cancel.config(background='grey', foreground='#98eced')

    # Create a  Submit Button
    submit_button = Button(text="Register", fg="#98eced", bg="grey", activeforeground="red", activebackground="orange",
                           width=16, borderwidth=0, font=('Century Gothic', 20, 'normal'), command=submit)
    submit_button.place(x=450, y=650)

    reg_cancel = Button(text="Cancel", fg="#98eced", bg="grey", activeforeground="red", activebackground="orange",
                           width=17, borderwidth=0, font=('Century Gothic', 20, 'normal'), command=quit_reg)
    reg_cancel.place(x=725, y=650)

    # Bind the button and Leave Events to the Button
    submit_button.bind('<Enter>', on_submit_enter)
    submit_button.bind('<Leave>', on_submit_leave)

    reg_cancel.bind('<Enter>', on_cancel_enter)
    reg_cancel.bind('<Leave>', on_cancel_leave)

    # 2nd Button : Normal Submit Button

    # submit_btn = Button(fg="orange", bg="grey", activeforeground="red", activebackground="#98eced", width=20, borderwidth=0, text="Register", font=("Times New Roman", 21, "normal"))\
    #     .place(x=680, y=500)

    # View Record Button to test if the data is being stored

    # show_record_btn = Button(text= "Show Records", fg="#98eced", bg="grey", activeforeground="red", activebackground="orange", width=20, borderwidth=0, font= ('Century Gothic', 20, 'normal'), command=view_records)
    # show_record_btn.place(x=350, y=650)

    reg_page.mainloop()


def quit_main():
    response = messagebox.askyesno("QUIT???", "Are You Sure You Wan't To Quit ?")
    if response == 1:
        root.destroy()
    else:
        pass




# Making function to create the hovering effect on the buttons
def on_login_enter(g):
    login_btn.config(background='#949999', foreground="white")

def on_login_leave(g):
    login_btn.config(background='grey', foreground='#98eced')

def on_user_reg_enter(h):
    new_user_reg_label.config(background='#949999', foreground="white")

def on_user_reg_leave(h):
    new_user_reg_label.config(background='grey', foreground='#98eced')

def on_user_quit_enter(h):
    quit_root.config(background='#949999', foreground="white")

def on_user_quit_leave(h):
    quit_root.config(background='grey', foreground='#98eced')


# Creating Login Button
# login_btn = Button(fg="orange", activeforeground="red", activebackground="black", width=10, borderwidth=0, bg="grey", text="Login", font=("Times New Roman", 20, "bold"), command=try_login)\
#     .place(x=160, y=450)

login_btn = Button(fg="#98eced", activeforeground="orange", activebackground="black", width=10, borderwidth=0, bg="grey",
                   text="Login", font=("Times New Roman", 20, "bold"), command=try_login)
login_btn.place(x=160, y=350)


new_user_reg_label = Button(fg="#98eced", activeforeground="orange", activebackground="black", width=20, borderwidth=0, bg="grey",
                            text="For New User Click Here!", font=("Times New Roman", 20, "bold"), command=registration_page)
new_user_reg_label.place(x=80, y=420)


quit_root = Button(fg="#98eced", activeforeground="orange", activebackground="black", width=15, borderwidth=0, bg="grey",
                   text="QUIT", font=("Times New Roman", 20, "normal"), command=quit_main)
quit_root.place(x=780, y=660)


login_btn.bind('<Enter>', on_login_enter)
login_btn.bind('<Leave>', on_login_leave)

new_user_reg_label.bind('<Enter>', on_user_reg_enter)
new_user_reg_label.bind('<Leave>', on_user_reg_leave)

quit_root.bind('<Enter>', on_user_quit_enter)
quit_root.bind('<Leave>', on_user_quit_leave)

mainloop()

