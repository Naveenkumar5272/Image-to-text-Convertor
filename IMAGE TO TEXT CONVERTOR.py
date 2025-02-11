from ast import Delete
from cProfile import label
from email import message
from importlib.machinery import PathFinder
from pydoc import text
from tkinter import *
from tkinter import messagebox
from turtle import width
from tkinter import filedialog
from unittest import result
from PIL import Image
from pytesseract import pytesseract
import random
from PIL import ImageTk , Image
global a , results
a = random.randint(100,999)
root = Tk()
root.configure(background="orange")
root.geometry("1200x600")
root.resizable(False,False)
def process():
    global text
    path_of_file = filedialog.askopenfilename()
    path_to_image = 'images/sampletext1-ocr.png'
    pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    img = Image.open(path_of_file)

    #Extract text from image
    text = pytesseract.image_to_string(img)
    results = text
    print(text)
    txtfld.insert(1.0 , text)
    imggen(path_of_file)    


def clear():
    txtfld.delete(1.0, END)

def save():
    with open(str(a)+".txt","w") as file:
        file.write(text)
    messagebox.showinfo("sucess",f"file {a}.txt saved successfuly")    


heading = Label(root , text="IMAGE TO TEXT EXTRACTION",padx=10 , font=("times new roan",20,"bold"), fg="black",bg="orange").pack()


btn_frame = Frame(bg="black")
btn_frame.place(x=0,y=50,width=1200,height=50)
img_frame = Frame(bg="black" , bd=15 , relief=GROOVE )
img_frame.place(x=0,y=100,width=600,height=500)


def imggen(path):
    images= ImageTk.PhotoImage(Image.open(path))
    lbl11 = Label(img_frame , image= images)                    
    lbl11.place( x=0 , y=0 ,width=570 , height=470 )


img_lbl = Label(btn_frame , text="IMAGE FIELD" , font=("times new roaman",15,"bold"), fg="white",bg="black")
img_lbl.place(y = 5 , x=250)

txt_lbl = Label(btn_frame , text="TEXT FIELD" , font=("times new roan",15,"bold"), fg="white",bg="black")
txt_lbl.place(y = 5 , x=850)






text_frame = Frame(bg="grey")
text_frame.place(x=600,y=100,width=600,height=600)

txtfld = Text(text_frame , bd=15 , relief=SUNKEN, bg="black" , fg="white" , font=("",13,"bold"))
txtfld.place(x=10,y=10,width=580,height=400)

savebtn = Button(text_frame , command= save ,text="Save",bg="green" , fg="white" , font=("goudy old style",15,"bold") )
savebtn.place(x=460, y=415 , width=80 , height=50)

clsbtn = Button(text_frame ,command=clear,text="Clear",bg="red" , fg="white" , font=("goudy old style",15,"bold") )
clsbtn.place(x=50, y=415 , width=80 , height=50)

btn = Button(text_frame , command=process ,text="choose image",bg="white" , fg="black" , font=("goudy old style",15,"bold"))
btn.place(x=150,y=420 ,  width=300 , height=50)

root.mainloop()