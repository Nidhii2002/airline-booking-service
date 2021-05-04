from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

class  Cancel:
    def __init__(self, root):
        self.root = root
        self.root.title("Cancel Flight")
        self.root.geometry('640x500')
        #self.root.resizable(False,False)

        #====BG IMG=====#
        self.bg=ImageTk.PhotoImage(file="Image/cancel.jpg")
        self.bg_image= Label(self.root, image=self.bg).place(x=0,y=0)

        title= Label(self.root,text="Enter Seat No:",font=("Bold",15),bd=0,bg="White").place(x=50,y=80)
        self.txt_seat=Entry(self.root,bg="lightgray",bd=0)
        self.txt_seat.place(x=50,y=110,width=300,height=25)

        title= Label(self.root,text="Enter Date of your Travel:",font=("Bold",15),bd=0,bg="White").place(x=50,y=160)
        self.txt_date=Entry(self.root,bg="lightgray",bd=0)
        self.txt_date.place(x=50,y=190,width=300,height=25)

        title= Label(self.root,text="Enter Boarding:",font=("Bold",15),bd=0,bg="White").place(x=50,y=240)
        self.txt_board=Entry(self.root,bg="lightgray",bd=0)
        self.txt_board.place(x=50,y=270,width=300,height=25)

        title= Label(self.root,text="Enter Class:",font=("Bold",15),bd=0,bg="White").place(x=50,y=320)
        # self.txt_user=Entry(self.root,bg="lightgray",bd=0).place(x=50,y=350,width=300,height=25)
        self.txt_class=ttk.Combobox(self.root,state="readonly")
        self.txt_class['values']=("Bussiness","First","Economy")
        self.txt_class.place(x=50,y=350,width=300,height=25)

        cancel_button = Button(self.root,text="Cancel",bg="red",command=self.cancel_func,font=("Bold",15)).place(x=250,y=400,width=100,height=40)

    def cancel_func(self):
        if self.txt_board.get()=="" or self.txt_date.get()=="":
            messagebox.showerror("Error","All Fields are Required!")
        else:
            try:
                con = pymysql.Connect(host="localhost",user="root",password="",database="airline")
                cur = con.cursor()
                cur.execute("select * from booking where boarding=%s and date=%s",
                    (self.txt_board.get(),self.txt_date.get()
                    ))
                row = cur.fetchone()

                if row=="None":
                    messagebox.showerror("Error","Cann't cancel the booking",parent=self.root)
                else:
                    messagebox.showinfo("Welcome","You have successfully cancelled your booking",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to {str(es)}", parent=self.root)
            con.close()
                


root = Tk()
obj = Cancel(root)
root.mainloop()
