#! /media/root/persistence/Code/gedeon/Python/VituralEnv/bin/python

import zipfile
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import font
from random import randrange
from pygame import mixer

mixer.init()
#mixer.music.load("assets/sounds/click.ogg")
#mixer.music.play()
#help(zipfile)
root = Tk()
root.title('Zip')
root.size()
#root.iconbitmap('assets/alien.png')
global lab2,p1open,defaultdir
p1open=0
SIDE=400
defaultdir="/media/root/persistence/Code/gedeon/Python/trash/"

def ext_here(filedir):
    global err_msg,lab2,top
    decomp(filedir,'')
    mixer.music.load("assets/sound/click.ogg")
    mixer.music.play()


def ext_to(filedir):
    root.filename =filedialog.askdirectory(title="select folder")
    filedir2=root.filename
    print(filedir2)
    decomp(filedir,filedir2)
    

def decomp(filedir,filedir2):
    global lab2,p1open
    myzip=zipfile.PyZipFile(filedir)
    myzip.extractall(path=filedir2)
    print('fichiers decompresser !!!')
    err_msg="fichiers decompresser !!!"
    p1open+=1
    if p1open>=3:
        #lab2.destroy()
        pass
    lab2=Label(top,text=err_msg,cnf="",bg='green',fg='white',pady=10,padx=40).pack(pady=10,padx=10)
    


def ext():
    global lab2,err_msg,top
    err_msg=''
    root.filename = filedialog.askopenfilename(initialdir=defaultdir,title="select files",filetypes=(('zip files','*.zip'),('all','*.*')))
    filedir=root.filename
    top=Toplevel(root)
    dirList=filedir.split('/')
    top.title('zip :  {}'.format(dirList[-1]))
    
    #print(dirList)
    Label(top,text="dir : "+filedir+'\n nom : '+dirList[-1],bg='darkblue',fg='white',pady=10,padx=40 ).pack()
    btn2=Button(top,text="extract here",pady=10,padx=40,fg="white",bg="royalblue",command=lambda:ext_here(filedir))
    btn2.pack(padx=10,pady=10)
    btn=Button(top,text="extrat to",pady=10,padx=40,fg="white",bg="royalblue",command=lambda:ext_to(filedir))
    btn.pack(padx=10,pady=10)
    btn=Button(top,text="close",pady=10,padx=40,fg="white",bg="crimson",command=top.destroy)
    btn.pack(padx=10,pady=10)
    


print('terminer')
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.grid(row=2,column=1,padx=1,pady=1)
logo = PhotoImage(file="assets/img/projectile.png")
center=(200,200)
cnv.create_image(center, image=logo)

Label(root,text="Zip est un logiciel de manipulation de fichiers compresser \n en version 1.0 par toutpuisaantged",fg="white",bg="royalblue",padx=20,pady=20).grid(row=1,column=1,padx=1,pady=1)
btn2=Button(root,text="choose file",pady=10,padx=40,fg="white",bg="blue",command=ext)
btn2.grid(row=0,column=0,padx=10,pady=10)
btn=Button(root,text="exit",pady=10,padx=40,fg="white",bg="red",width=8, command=root.quit)
btn.grid(row=1,column=0,padx=10,pady=10)

root.mainloop()