from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector as mysql
import pymysql

root = Tk()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry('602x381')
        #self.root.resizable(False,False)

        #====BG IMG=====#
        self.bg=ImageTk.PhotoImage(file="Image/login.jpg")
        self.bg_image= Label(self.root, image=self.bg).place(x=0,y=0,width=602, height=381)

        #===Frame===#
        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=250,y=180, height=190,width=340)

        title= Label(Frame_login,text="Login Here",font=("bold",18),bg="white",fg="Green").place(x=120,y=0)

        user= Label(Frame_login,text="Username:",font=("bold",10),bg="white").place(x=30,y=50)
        self.txt_user=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_user.place(x=150,y=50,width=130,height=30)

        password= Label(Frame_login,text="Password:",font=("bold",10),bg="white").place(x=30,y=100)
        self.txt_pass=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_pass.place(x=150,y=100,width=130,height=30)

        login_button = Button(Frame_login,text="Login",command=self.login_func,bg="green",font=("bold",15)).place(x=150,y=150,width=100,height=30)

    def login_func(self):

        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All Fields are Required!")
        else:
            con = pymysql.Connect(host="localhost",user="root",password="",database="airline")
            cur = con.cursor()
            cur.execute("select * from user where name=%s and password=%s",(self.txt_user,self.txt_pass))       
            row = cur.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("Error","Invalid USERNAME and PASSWORD!",parent=self.root)
            else:
                messagebox.showinfo("Welcome","You have successfully registered",parent=self.root)
            # messagebox.showinfo("Welcome","Welcome to Airline Booking Service")
            con.close()
        
obj = Login(root)
root.mainloop()
