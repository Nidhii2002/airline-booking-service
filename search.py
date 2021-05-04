from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


class Search:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Flight")
        self.root.geometry('1000x540')
        #self.root.resizable(False,False)

        #====BG IMG=====#
        self.bg=ImageTk.PhotoImage(file="Image/search.jpg")
        self.bg_image= Label(self.root, image=self.bg).place(x=0,y=0)

        title= Label(self.root,text="Enter Boarding:",font=("Bold",15),bd=0,bg="lightblue").place(x=50,y=80)
        self.txt_board=Entry(self.root,bg="lightgray",bd=0)
        self.txt_board.place(x=50,y=110,width=300,height=25)


        title= Label(self.root,text="Select Destination:",font=("Bold",15),bd=0,bg="lightblue").place(x=500,y=80)
        # self.txt_user=Entry(self.root,bg="lightgray",bd=0).place(x=500,y=110,width=300,height=25)
        self.txt_dest=ttk.Combobox(self.root,state="readonly")
        self.txt_dest['values']=("Delhi","Kolkatta","Banglore","Punjab")
        self.txt_dest.place(x=500,y=110,width=300,height=25)

        title= Label(self.root,text="Enter Departure Date:",font=("Bold",15),bd=0,bg="lightblue").place(x=50,y=160)
        self.txt_date=Entry(self.root,bg="lightgray",bd=0)
        self.txt_date.place(x=50,y=190,width=300,height=25)

        title= Label(self.root,text="Enter No. of Passenger:",font=("Bold",15),bd=0,bg="lightblue").place(x=500,y=160)
        self.txt_pass=Entry(self.root,bg="lightgray",bd=0)
        self.txt_pass.place(x=500,y=190,width=300,height=25)

        title= Label(self.root,text="Enter the Class:",font=("Bold",15),bd=0,bg="lightblue").place(x=50,y=240)
        # self.txt_user=Entry(self.root,bg="lightgray",bd=0)
        self.txt_class=ttk.Combobox(self.root,state="readonly")
        self.txt_class['values']=("Bussiness","First","Economy")
        self.txt_class.place(x=50,y=270,width=300,height=25)


        search_button = Button(self.root,text="Search",bg="blue",command=self.show,font=("Bold",15)).place(x=400,y=300,width=100,height=50)

    def datepick(self,root):
        pass

    def search(self):
        con = pymysql.Connect(host="localhost",user="root",password="",database="airline")
        cur = con.cursor()
        cur.execute("select *  from search where boarding=%s and dest=%s and class=%s",
                    (self.txt_board.get(),self.txt_dest.get(),self.txt_class.get()
                    ))
        row = cur.fetchall()
        
        if row=="None":
            messagebox.showerror("Error","Cann't Search the flight",parent=self.root)
        else:
            list = Listbox(root)
            list.place(x=50,y=330)

        con.close()
        
    def show(self):
        con = pymysql.Connect(host="localhost",user="root",password="",database="airline")
        cur = con.cursor()
        cur.execute("select *  from search")
        
        # rows = cur.fetchall()
        # print(rows)

        # for row in rows:
        #     insertData = str(row[1]) + '     '+ row[2]
        #     list.append(insertData)
        i = 0
        for serch in cur:
            for j in range(len(serch)):
                e = Entry(root, width=500, fg='blue') 
                e.place(x=50, y=330) 
                e.insert(serch[j])
            i=i+1
        
        con.close()



       

        # messagebox.showinfo("Welcome","You have successfully registered")
    # def search_func(self):
    #     if self.txt_board=="" or self.txt_dest="":
    #         messagebox.showerror("Error","Enter Information")


root = Tk()
obj = Search(root)
root.mainloop()