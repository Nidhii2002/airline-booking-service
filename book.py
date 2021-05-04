from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

class  Book:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking")
        self.root.geometry('600x580')
        #self.root.resizable(False,False)

        #====BG IMG=====#
        self.bg=ImageTk.PhotoImage(file="Image/book.jpg")
        self.bg_image= Label(self.root, image=self.bg).place(x=0,y=0)

        title= Label(self.root,text="Flight Booking",font=("Bold",20),bd=0,fg="red").place(x=200,y=10)

        boarding= Label(self.root,text="Enter Boarding:",font=("Bold",15),bd=0).place(x=30,y=70)
        self.txt_board=Entry(self.root,bg="lightgray",bd=0)
        self.txt_board.place(x=320,y=70,width=200,height=25)

        destination= Label(self.root,text="Enter Destination:",font=("Bold",15),bd=0).place(x=30,y=140)
        # self.txt_user=Entry(self.root,bg="lightgray",bd=0)
        self.txt_dest=ttk.Combobox(self.root,state="readonly")
        self.txt_dest['values']=("Delhi","Kolkatta","Banglore","Punjab")
        self.txt_dest.place(x=320,y=140,width=200,height=25)

        cnum= Label(self.root,text="Enter your Citizenship Number:",font=("Bold",15),bd=0).place(x=30,y=210)
        self.txt_cnum=Entry(self.root,bg="lightgray",bd=0)
        self.txt_cnum.place(x=320,y=210,width=200,height=25)

        title= Label(self.root,text="Choose Class:",font=("Bold",15),bd=0).place(x=30,y=280)
        # self.txt_user=Entry(self.root,bg="lightgray",bd=0)
        self.txt_class=ttk.Combobox(self.root,state="readonly")
        self.txt_class['values']=("Bussiness","First","Economy")
        self.txt_class.place(x=320,y=280,width=200,height=25)

        day= Label(self.root,text="Choose Day of Travel:",font=("Bold",15),bd=0).place(x=30,y=350)
        self.txt_date=Entry(self.root,bg="lightgray",bd=0)
        self.txt_date.place(x=320,y=350,width=200,height=25)

        time= Label(self.root,text="Choose Time of Travel:",font=("Bold",15),bd=0).place(x=30,y=420)
        self.txt_time=Entry(self.root,bg="lightgray",bd=0)
        self.txt_time.place(x=320,y=420,width=200,height=25)

        book_button = Button(self.root,text="Save",font=("Bold",15),command=self.book_func,bg="pink",fg="red").place(x=200,y=480,width=100,height=40)

    def book_func(self):
        if self.txt_board.get()=="" or self.txt_dest.get()=="" or self.txt_cnum.get()=="" or self.txt_class.get()=="" or self.txt_date.get()=="" or self.txt_time.get()=="":
            messagebox.showerror("Error","All Fields are Required!")
        else:
            try:
                con = pymysql.Connect(host="localhost",user="root",password="",database="airline")
                cur = con.cursor()
                cur.execute("insert into booking (boarding,dest,cnum,class,date,time) values(%s,%s,%s,%s,%s,%s)",
                    (self.txt_board.get(),self.txt_dest.get(),self.txt_cnum.get(),self.txt_class.get(),
                    self.txt_date.get(),self.txt_time.get()
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Welcome","You have successfully booked Flight",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to {str(es)}", parent=self.root)
                




root = Tk()
obj = Book(root)
root=mainloop()
