# -*- coding: utf-8 -*-                
"""
Created on Wed Sep 15 13:42:17 2021

@author: Manoj
"""

from tkinter import *
root=Tk()
root.title("Driving licence")
root.geometry("300x400")
root.configure(bg="#0095ff")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0,0,300,55,fill="#07f52b")
canvas.create_rectangle(0,345,300,55,fill="#07f52b")
label_heading=canvas.create_text(150,90,font=('Times','24','bold italic'),text="Driving licence")
label_name_tag=canvas.create_text(40,165,font=('Times','16','bold'),text="Name:")
label_grade_tag=canvas.create_text(40,205,font=('Times','16','bold'),text="Date of birth:")
label_subject_tag=canvas.create_text(50,250,font=('Times','16','bold'),text="Pin:")
label_name=Label(root)
label_grade=Label(root)
label_subject=Label(root)
def Drivinglicenc():
    name="Siddharth"
    print(type(name))
    dateofbirth="30/11/2010"
    print(type(dateofbirth))
    pin=(type(400030))
    print(type(pin))
    label_name['text']=name
    label_grade['text']=dateofbirth
    label_subject['text']=pin
button1=Button(root,text="SHOW MY DRVING LICENCE",command=Drivinglicenc)
button1_window = canvas.create_window(150,330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90,205, anchor=CENTER, window=label_grade)
label_subject_window = canvas.create_window(155,252, anchor=CENTER, window=label_subject)
canvas.pack()
root.mainloop() 