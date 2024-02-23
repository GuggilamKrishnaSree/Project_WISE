from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
root = Tk()

root.geometry('500x400+550+100')
class details():
    
    def __init__(self,root):
        self.root=root
        self.root.title("Problem details window")

        self.bg_img = Image.open('logo.png')
        self.bg_img = self.bg_img.resize((500,400))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x = 0 , y = 0)

        self.l1=Label(root,text="PROBLEM DETAILS",bg="DodgerBlue2",fg="white",font=("Calibri",20),borderwidth=1,relief="solid")
        self.l1.pack(fill='x')

        self.name = Label(root, text = "Student name", fg = "black", bg = "white", font = ("Calibri", 10),borderwidth=1,relief="solid")
        self.name.place(x = 10, y = 60,width=130)
        self.e1 = Entry(root)
        self.e1.place(x = 150, y = 60,width=250)

        self.regno = Label(root, text = "Register no", fg = "black", bg = "white", font = ("Calibri", 10),borderwidth=1,relief="solid")
        self.regno.place(x = 10, y = 100, width=130)
        self.e2 = Entry(root)
        self.e2.place(x = 150, y = 100,width=150)

        self.hostel = Label(root, text = "Hostel name, Room no", fg = "black", bg = "white", font = ("Calibri", 10),borderwidth=1,relief="solid")
        self.hostel.place(x = 10, y = 140,width=130)
        self.e3 = Entry(root)
        self.e3.place(x = 150, y = 140,width=250,height=50)

        self.descrip = Label(root,text = "Problem Description",fg = "black", bg = "white", font = ("Calibri", 10),borderwidth=1,relief="solid")
        self.descrip.place(x = 10, y = 220,width=130)
        self.e4 = Entry(root)
        self.e4.place(x = 150, y = 200,width=300,height=100)
        

        self.submit_btn = Button(root, text='SUBMIT', font=('Calibri',15, 'bold'), bd = 4,command=self.save_data)
        self.submit_btn.place(x = 205, y =  350)

    def save_data(self):
        n = self.e1.get()
        r = self.e2.get()
        h = self.e3.get()
        d = self.e4.get()
        with open("data.txt", "a") as file:
            file.write(f"Name : {n}\n")
            file.write(f"Reg no : {r}\n")
            file.write(f"Hostel, room no : {h}\n")
            file.write(f"Description: {d}\n")
    
        self.l1.destroy()
        self.name.destroy()
        self.regno.destroy()
        self.hostel.destroy()
        self.descrip.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.e4.destroy()
        self.submit_btn.destroy()
        self.l2=Label(root,text="your details are saved",bg="DodgerBlue2",fg="white",font=("Calibri",20),borderwidth=1,relief="solid")
        self.l2.pack()
        self.l2.place(x=150 , y=150 , width=250)


obj = details(root)
root.mainloop()
