from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

GUI = Tk() # หน้าจอหลัก
GUI.title('Bekery') # ชื่อโปรแกรม
GUI.geometry('600x700') # ขนาดโปรแกรม
L1 = Label(GUI,text='Bread & Cake',font=('angsana New',30),fg='black')
L1.place(x=210,y=20)
L2 = Label(GUI,text='ปิดรับออเดอร์ 2 ทุ่ม',font=('angsana New',15),fg='black')
L2.place(x=55,y=100)
L3 = Label(GUI,text='เมนูประจำวัน',font=('angsana New',15),fg='black')
L3.place(x=55,y=150)
##############
import csv
from datetime import datetime

def writecsv(datalist):
    with open('Order.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) # fw = file write
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']

def readcsv():
    with open('Oder.csv',encoding='utf-8',newline='') as file:
       fr = csv.reader(file) # fr = file reader
       data = list(fr)
    return data
###################
def Button1():
    text = 'Banoffee , Tiramisu'
    messagebox.showinfo('Menu',text)

FB1 = Frame(GUI)# คล้ายกระดาน
FB1.place(x=55,y=200)
B1 = ttk.Button(FB1,text='วันจันทร์',command=Button1)# ชื่อปุ่ม
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'Brownie LAVA'
    messagebox.showinfo('Menu',text)

FB2 = Frame(GUI) 
FB2.place(x=55,y=300)
B2 = ttk.Button(FB1,text='วันอังคาร',command=Button2)# ชื่อปุ่ม
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = ' <Cheesecake> \n\n Strawberry\n Blueberry\n Mango'
    messagebox.showinfo('Menu',text)

FB3 = Frame(GUI) 
FB3.place(x=55,y=400)
B3 = ttk.Button(FB1,text='วันพุธ',command=Button3)# ชื่อปุ่ม
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'ไม่มี'
    messagebox.showinfo('Menu',text)

FB4 = Frame(GUI)
FB4.place(x=55,y=500)
B4 = ttk.Button(FB1,text='วันพฤหัส',command=Button4)# ชื่อปุ่ม
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'ไม่มี'
    messagebox.showinfo('Menu',text)

FB5 = Frame(GUI) 
FB5.place(x=55,y=600)
B5 = ttk.Button(FB1,text='วันศุกร์',command=Button5)# ชื่อปุ่ม
B5.pack(ipadx=20,ipady=20)

def Button6():
    text = 'ไม่มี'
    messagebox.showinfo('Menu',text)

FB6 = Frame(GUI) 
FB6.place(x=55,y=700)
B6 = ttk.Button(FB1,text='วันเสาร์',command=Button6)# ชื่อปุ่ม
B6.pack(ipadx=20,ipady=20)

def Button7():
    text = 'ไม่มี'
    messagebox.showinfo('Menu',text)

FB7 = Frame(GUI) 
FB7.place(x=55,y=800)
B7 = ttk.Button(FB1,text='วันอาทิตย์',command=Button7)# ชื่อปุ่ม
B7.pack(ipadx=20,ipady=20)

############## section right ###############
L4 = Label(GUI,text='กรอกข้อมูล',font=('angsana New',20),fg='black')
L4.place(x=420,y=100)

L5 = Label(GUI,text='ชื่อ',font=('angsana New',15),fg='black')
L5.place(x=350,y=150)
v_name = StringVar()
E5 = ttk.Entry(GUI,textvariable=v_name,font=('Angsana New',15))
E5.place(x=400,y=150)

L6 = Label(GUI,text='เมนู',font=('angsana New',15),fg='black')
L6.place(x=350,y=200)
v_menu = StringVar()
E6 = ttk.Entry(GUI,textvariable=v_menu,font=('Angsana New',15))
E6.place(x=400,y=200)

L7 = Label(GUI,text='จำนวน',font=('angsana New',15),fg='black')
L7.place(x=350,y=250)
v_quantity = StringVar()
E7 = ttk.Entry(GUI,textvariable=v_quantity,font=('Angsana New',15))
E7.place(x=400,y=250)

def Savedata():
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = v_name.get() #ดึงข้อมูลจากตัวแปร v_ มาใช้งาน  
    menu = v_menu.get()
    quantity = v_quantity.get()
    text = [t,name,menu,quantity] # [เวลาที่ข้อมูลที่ได้จากการกรอก]
    writecsv(text) # บันทึกลง csv
    v_name.set('') # เคลียร์ข้อมูลที่อยู่ในช้องกรอก
    v_menu.set('')
    v_quantity.set('')

B8 = ttk.Button(GUI,text='บันทึก',command=Savedata)# ชื่อปุ่ม
B8.pack(ipadx=20,ipady=20)
B8.place(x=420,y=310)

GUI.mainloop()
