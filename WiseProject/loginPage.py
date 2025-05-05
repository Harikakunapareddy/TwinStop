from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'sony@1303', database = 'twinstop')
mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE TwinStop")
# mycursor.execute("CREATE TABLE user_details(user_name VARCHAR(50), password VARCHAR(50))")

fonts=('verdana',15,'bold')
root = Tk()
root.geometry("1399x758+100+58")
background_color = "lightblue"
root.configure(bg=background_color)
root.title("TWIN STOP")


def set_background(root, frame, image_path):
    # Load the image
    image = PhotoImage(file=image_path)

    # Create a label with the image
    label = Label(frame, image=image)
    label.image = image  # Keep a reference to avoid garbage collection

    # Place the label in the frame
    label.place(relwidth=1, relheight=1)

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width=1399, height=758, bg='#aaa')
        self.login_frame.place(x=0, y=0)

        # set_background(root, self.login_frame, "bg.png")

        self.label = Label(self.login_frame, text ="TWIN STOP", font =("Times", 35, 'bold'), fg = "black", bg = "white")
        self.label.place(x = 875, y = 108)

        self.user_name = Label(self.login_frame, text='NAME', font=fonts, bg='white', fg='steel blue', width=10)
        self.user_name.place(x=700, y=300)
        self.user_name_entry = Entry(self.login_frame, width=13, font=fonts, bg='white')
        self.user_name_entry.place(x=700, y=350)

        self.user_pass = Label(self.login_frame, text='PASSWORD', font=fonts, bg='white', fg='steel blue', width=10)
        self.user_pass.place(x=1150, y=300)
        self.user_pass_entry = Entry(self.login_frame, width=13, font=fonts, bg='white', show="*")
        self.user_pass_entry.place(x=1150, y=350)


        self.submit_btn = Button(self.login_frame, text='LOGIN', bg='white', fg='steel blue', font=fonts,command=self.check_function, cursor='hand2', activebackground='blue')
        self.submit_btn.place(x=850, y=500)

        self.signup_btn = Button(self.login_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts,command= lambda:SignUp(self.root), cursor='hand2', activebackground='blue')
        self.signup_btn.place(x=1000, y=500)

        self.create = Label(self.login_frame, text='Dont have an account?', font='blue 10', bg='#aaa',fg='black', width=20)
        self.create.place(x=1000, y=470)


    def check_function(self):
        if self.user_name_entry.get() == "" or self.user_pass_entry.get() == "":
            messagebox.showerror("Error", "ALL fields are required", parent=self.root)
        elif self.user_name_entry.get() != "wiseproject" or self.user_pass_entry.get() != "twinstop":
            messagebox.showerror("Error","Invalid user name or password",parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.user_name_entry.get()}")
            dashboard = Dashboard(self.root)

class SignUp:
    def __init__(self, root):
        self.root = root

        self.signup_frame = Frame(self.root, width=600, height=500, bg='#bbb')
        self.signup_frame.place(x=270, y=100)

        self.label = Label(self.signup_frame, text="SIGN UP", font=("Times", 35, 'bold'), fg="black", bg="white")
        self.label.place(x=200, y=38)

        self.user_name = Label(self.signup_frame, text='USER NAME', font=fonts, bg='white', fg='steel blue', width=10)
        self.user_name.place(x=20, y=150)
        self.user_name_entry = Entry(self.signup_frame, width=13, font=fonts, bg='white')
        self.user_name_entry.place(x=20, y=200)

        self.user_pass = Label(self.signup_frame, text='PASSWORD', font=fonts, bg='white', fg='steel blue', width=10)
        self.user_pass.place(x=20, y=250)
        self.user_pass_entry = Entry(self.signup_frame, width=13, font=fonts, bg='white', show="*")
        self.user_pass_entry.place(x=20, y=300)

        self.con_user_pass = Label(self.signup_frame, text='CONFIRM PASSWORD', font=fonts, bg='white', fg='steel blue', width=20)
        self.con_user_pass.place(x=20, y=350)
        self.con_user_pass_entry = Entry(self.signup_frame, width=13, font=fonts, bg='white', show="*")
        self.con_user_pass_entry.place(x=20, y=400)

        self.signup_btn = Button(self.signup_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts,command=self.check_function, cursor='hand2', activebackground='blue')
        self.signup_btn.place(x=400, y=400)


    def check_function(self):
        if self.user_name_entry.get() == "" or self.user_pass_entry.get() == "":
            messagebox.showerror("Error", "ALL fields are required", parent=self.root)
        elif self.user_pass_entry.get() == self.con_user_pass_entry.get():
            # sql = "INSERT INTO user_details(user_name, password)VALUES(%s, %s)"
            # val = (self.user_name_entry.get(), self.user_pass_entry.get())
            # mycursor.execute(sql, val)
            messagebox.showinfo("Welcome", f"Welcome {self.user_name_entry.get()}")
            self.signup_btn = Button(self.signup_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts,command=Dashboard(self.root), cursor='hand2', activebackground='blue')
           # messagebox.showerror("Error","Re-enter password",parent=self.root)
        else:
            messagebox.showerror("Error", "Re-enter password", parent=self.root)

            #messagebox.showinfo("Welcome", f"Welcome {self.user_name_entry.get()}")
           # self.signup_btn = Button(self.signup_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts,command=Login(self.root), cursor='hand2', activebackground='blue')




class Dashboard:
    def __init__bv (self, root):
        self.root = root
        self.root.title('WELCOME TO THE DASHBOARD')
        self.login_frame = Frame(self.root, width=600, height=500, bg='#ccc')
        self.login_frame.place(x=270, y=100)

        self.label = Label(self.login_frame, text="ENTER DETAILS", font=("Times", 35, 'bold'), fg="black",bg="#ccc")
        self.label.place(x=150, y=38)

        self.user_city = Label(self.login_frame, text='SEARCH FOR CITY', font=fonts, bg='white', fg='steel blue', width=20)
        self.user_city.place(x=20, y=150)
        self.user_city_entry = Entry(self.login_frame, width=13, font=fonts, bg='white')
        self.user_city_entry.place(x=20, y=200)

        self.user_date = Label(self.login_frame, text='DATE', font=fonts, bg='white', fg='steel blue', width=10)
        self.user_date.place(x=20, y=250)
        self.user_date_entry = Entry(self.login_frame, width=13, font=fonts, bg='white', show="*")
        self.user_date_entry.place(x=20, y=300)

        self.con_user_time = Label(self.login_frame, text='CONVENIENT TIME', font=fonts, fg='steel blue',width=20)
        self.con_user_time.place(x=20, y=350)
        self.con_user_time_entry = Entry(self.login_frame, width=13, font=fonts, bg='white', show="*")
        self.con_user_time_entry.place(x=20, y=400)

        self.enter_btn = Button(self.login_frame, text='ENTER', bg='white', fg='steel blue', font=fonts, cursor='hand2', activebackground='blue')
        self.enter_btn.place(x=400, y=250)


root.resizable(False,False)
login = Login(root)
root.mainloop()