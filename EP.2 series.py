from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import ImageTk,Image

GUI = Tk() # หน้าจอหลัก
GUI.title('ประวัติการรับชมซีรีส์และภาพยนต์') # ชื่อโปรแกรม
GUI.geometry('400x600') # ขนาดโปรแกรม
L1 = Label(GUI,text='ซีรีส์ ภาพยนต์ รายการทีวี',font=('angsana New',30),fg='black')
L1.place(x=55,y=20)



########################
def Button1():
    text = 'Running Man EP.646 , Shadow and Bone SS2 EP.8'
    messagebox.showinfo('ประวัติการรับชม',text)

FB1 = Frame(GUI)# คล้ายกระดาน
FB1.place(x=140,y=80)
B1 = ttk.Button(FB1,text='วันจันทร์',command=Button1)# ชื่อปุ่ม
B1.pack(ipadx=20,ipady=20)



def Button2():
    text = 'ใต้ร่มราชินี EP.15-16'
    messagebox.showinfo('ประวัติการรับชม',text)

FB2 = Frame(GUI) 
FB2.place(x=140,y=400)
B2 = ttk.Button(FB1,text='วันอังคาร',command=Button2)# ชื่อปุ่ม
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'Mask Singer 12 EP.4'
    messagebox.showinfo('ประวัติการรับชม',text)

FB3 = Frame(GUI) 
FB3.place(x=140,y=500)
B3 = ttk.Button(FB1,text='วันพุธ',command=Button3)# ชื่อปุ่ม
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'The wall Song EP.135'
    messagebox.showinfo('ประวัติการรับชม',text)

FB4 = Frame(GUI)
FB4.place(x=140,y=600)
B4 = ttk.Button(FB1,text='วันพฤหัส',command=Button4)# ชื่อปุ่ม
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'Running Man EP.645 , Big Mommas House'
    messagebox.showinfo('ประวัติการรับชม',text)

FB5 = Frame(GUI) 
FB5.place(x=140,y=700)
B5 = ttk.Button(FB1,text='วันศุกร์',command=Button5)# ชื่อปุ่ม
B5.pack(ipadx=20,ipady=20)

def Button6():
    text = 'Premier League Man City VS Liverpool'
    messagebox.showinfo('ประวัติการรับชม',text)

FB6 = Frame(GUI) 
FB6.place(x=140,y=800)
B6 = ttk.Button(FB1,text='วันเสาร์',command=Button6)# ชื่อปุ่ม
B6.pack(ipadx=20,ipady=20)

def Button7():
    text = 'ไม่มี'
    messagebox.showinfo('ประวัติการรับชม',text)

FB7 = Frame(GUI) 
FB7.place(x=140,y=900)
B7 = ttk.Button(FB1,text='วันอาทิตย์',command=Button7)# ชื่อปุ่ม
B7.pack(ipadx=20,ipady=20)

GUI.mainloop()
