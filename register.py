from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Detail")
        self.root.geometry("900x600")

        self.bg=ImageTk.PhotoImage(file="Image/reg.jpg")
        self.bg_image= Label(self.root, image=self.bg).place(x=0,y=0)

        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=200,y=60, height=500,width=550)

        title= Label(Frame_login,text="Registration Details",font=("Bold",20),bd=0,bg="White",fg="red").place(x=130,y=10)

        name= Label(Frame_login,text="Name:",font=("Bold",15),bd=0,bg="White").place(x=30,y=60)
        self.txt_name=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_name.place(x=220,y=60,width=300,height=25)

        password= Label(Frame_login,text="Password:",font=("Bold",15),bd=0,bg="White").place(x=30,y=100)
        self.txt_pass=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_pass.place(x=220,y=100,width=300,height=25)

        gender= Label(Frame_login,text="Gender:",font=("Bold",15),bd=0,bg="White").place(x=30,y=140)
        # self.txt_user=Entry(Frame_login,bg="lightgray",bd=0).place(x=220,y=140,width=300,height=25)
        self.txt_gen=ttk.Combobox(Frame_login,state="readonly")
        self.txt_gen['values']=("Male","Female")
        self.txt_gen.place(x=220,y=140,width=300,height=25)

        email= Label(Frame_login,text="EmailID:",font=("Bold",15),bd=0,bg="White").place(x=30,y=180)
        self.txt_email=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_email.place(x=220,y=180,width=300,height=25)

        contact= Label(Frame_login,text="Contact No.",font=("Bold",15),bd=0,bg="White").place(x=30,y=220)
        self.txt_contact=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_contact.place(x=220,y=220,width=300,height=25)

        idt= Label(Frame_login,text="Id Proof Type:",font=("Bold",15),bd=0,bg="White").place(x=30,y=260)
        # self.txt_user=Entry(Frame_login,bg="lightgray",bd=0).place(x=220,y=260,width=300,height=25)
        self.txt_idt=ttk.Combobox(Frame_login,state="readonly")
        self.txt_idt['values']=("Aadhar Card","Pan Card","Licence","Passport")
        self.txt_idt.place(x=220,y=260,width=300,height=25)

        idnum= Label(Frame_login,text="ID Number:",font=("Bold",15),bd=0,bg="White").place(x=30,y=300)
        self.txt_id=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_id.place(x=220,y=300,width=300,height=25)

        address= Label(Frame_login,text="Address:",font=("Bold",15),bd=0,bg="White").place(x=30,y=340)
        self.txt_add=Entry(Frame_login,bg="lightgray",bd=0)
        self.txt_add.place(x=220,y=340,width=300,height=25)

        reg_button = Button(Frame_login,text="Register",command=self.register_func,bg="red",font=("Bold",15)).place(x=200,y=400,width=100,height=50)

    def register_func(self):
        if self.txt_add.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_gen.get()=="" or self.txt_id.get()=="" or self.txt_idt.get()=="" or self.txt_name.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All Fields are Required!")
        else:
            try:
                con = pymysql.Connect(host="localhost",user="root",password="",database="airline")
                cur = con.cursor()
                cur.execute("insert into user (name,password,gender,email,contact,id_type,id_num,address) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.txt_name.get(),self.txt_pass.get(),self.txt_gen.get(),self.txt_email.get(),
                    self.txt_contact.get(),self.txt_idt.get(),self.txt_id.get(),self.txt_add.get()
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Welcome","You have successfully registered")
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to {str(es)}", parent=self.root)
                
            # messagebox.showinfo("Welcome","You have successfully registered")
        


root = Tk()
obj = Register(root)
root.mainloop()