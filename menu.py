from tkinter import*
from PIL import Image,ImageTk

class Menu:
    def __init__(self,root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("600x400")

        self.bg=ImageTk.PhotoImage(file="Image/Menu.jpg")
        self.bg_image= Label(self.root, image=self.bg).place(x=0,y=0)

        book_button = Button(self.root,text="Book Flight",command=self.book_func,bg="orange",font=("Bold",15)).place(x=380,y=80,width=170,height=50)

        search_button = Button(self.root,text="Search Flight",bg="orange",command=self.search_func,font=("Bold",15)).place(x=380,y=160,width=170,height=50)

        cancel_button = Button(self.root,text="Cancel Flight",bg="orange",command=self.cancel_func,font=("Bold",15)).place(x=380,y=240,width=170,height=50)
    
    def book_func(self):
        self.root.destroy()
        import book

    def search_func(self):
        self.root.destroy()
        import search

    def cancel_func(self):
        self.root.destroy()
        import cancel

root = Tk()
obj = Menu(root)
root.mainloop()