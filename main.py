#! /media/root/persistence/Code/gedeon/Python/VituralEnv/bin/python

#By toutpuissantged

import zipfile
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import font
from random import randrange
from pygame import mixer
import json
import time

mixer.init()
#mixer.music.load("assets\sounds\click.ogg")
#mixer.music.play()
#help(zipfile)
global lab2,p1open,defaultdir,version,lang,userLang
version='1.0'
p1open=0
SIDEX=100
SIDEY=120
userLang="fr"
defaultdir="/media/root/persistence/Code/gedeon/Python/trash/"
jsonDir="public\lang\\"+userLang+"\config.json"

root = Tk()
root.size()
#root.iconbitmap('assets\alien.png')



def langInit(jsonDir):
    fop=open(jsonDir,'r')
    lang=fop.read()
    fop.close()
    lang=json.loads(lang)
    #print(lang)
    return lang


def ext_here(filedir):
    clickSon()
    global err_msg,lab2,top
    decomp(filedir,'')
    
def ext_to(filedir):
    clickSon()
    root.filename =filedialog.askdirectory(title="select folder")
    filedir2=root.filename
    print(filedir2)
    decomp(filedir,filedir2)
    

def decomp(filedir,filedir2):
    global lab2,p1open
    not_err=0
    try:
        myzip=zipfile.PyZipFile(filedir)
        myzip.extractall(path=filedir2)
    except:
        not_err=1

    if  not_err==0:
        finish(1)
        sucSon()
    else:
        finish(0)
        errorSon()
    p1open+=1
    if p1open>=3:
        #lab2.destroy()
        pass
    
    


def ext():
    clickSon()
    global lab2,err_msg,top
    err_msg=''
    root.filename = filedialog.askopenfilename(initialdir=defaultdir,title="select files",filetypes=(('zip files','*.zip'),('all','*.*')))
    filedir=root.filename
    top=Toplevel(root)
    dirList=filedir.split('/')
    top.title('zip :  {}'.format(dirList[-1]))
    
    #print(dirList)
    Label(top,text=lang['tools']['dir']+" : "+filedir+'\n '+lang['tools']['name']+' : '+dirList[-1],bg='darkblue',fg='white',pady=10,padx=40 ).pack()
    btn2=Button(top,text=lang['tools']['here'],pady=10,padx=40,fg="white",bg="royalblue",command=lambda:ext_here(filedir))
    btn2.pack(padx=10,pady=10)
    btn=Button(top,text=lang['tools']['to'],pady=10,padx=40,fg="white",bg="royalblue",command=lambda:ext_to(filedir))
    btn.pack(padx=10,pady=10)
    btn=Button(top,text=lang['tools']['close'],pady=10,padx=40,fg="white",bg="crimson",command=top.destroy)
    btn.pack(padx=10,pady=10)
    
    
def clickSon():
    mixer.music.load("asset/sound/click.ogg")
    mixer.music.play()

def errorSon():
    mixer.music.load("asset/sound/over.ogg")
    mixer.music.play()

def sucSon():
    mixer.music.load("asset/sound/tir.ogg")
    mixer.music.play()

def langPop():
    top3=Toplevel(root)
    top3.title('Langues')
    fg='white'
    bg='crimson'
    langList=["francais","anglais","espagnol","allemand"]
    langAcr=["fr","en","es","de"]
    clicked=StringVar()
    clicked.set(langList[0])
    Label(top3,text='Choisir votre langues',bg=bg,fg=fg,pady=10,padx=40).pack()
    drop=OptionMenu(top3,clicked,*langList)
    drop.pack()
    btn3=Button(top3,text='choisir',pady=10,padx=40,fg="white",bg="royalblue",command=lambda:langValid(clicked.get()))
    btn3.pack(padx=10,pady=10)
    btn3=Button(top3,text=lang['popup']['close'],pady=10,padx=40,fg="white",bg="crimson",command=top3.destroy)
    btn3.pack(padx=10,pady=10)
    async def rol (top3):
        await asyncio.sleep(2)
        top3.destroy()
    rol(top3)

def langValid(choix):
    langList=["francais","anglais","espagnol","allemand"]
    langAcr=["fr","en","es","de"]
    lock=0
    for i in langList:
        if i==choix:
            lock=langList.index(i)
            break
    lang=langInit("public/lang/"+langAcr[lock]+"/config.json")
    print("{} choisi ".format(langList[lock]))

def finish(msg):
    top2=Toplevel(root)
    fg='white'
    if msg==1:
        errText=lang['popup']['success']['text']
        bg='green'
        titre=lang['popup']['success']['title']

    elif msg==0:
        errText=lang['popup']['error']['text']
        bg='crimson'
        titre=lang['popup']['error']['title']
    else:
        pass
    top2.title(titre)
    Label(top2,text=errText,bg=bg,fg=fg,pady=10,padx=40).pack()
    btn3=Button(top2,text=lang['popup']['close'],pady=10,padx=40,fg="white",bg="crimson",command=top2.destroy)
    btn3.pack(padx=10,pady=10)


lang=langInit(jsonDir)
root.title(lang['main']['title'])
print('terminer')
cnv = Canvas(root, width=SIDEX, height=SIDEY, bg='ivory')
cnv.grid(row=2,column=1,padx=1,pady=1)
logo = PhotoImage(file="asset/img/main.jpg")
center=(50,60)
cnv.create_image(center, image=logo)

Label(root,text=lang['main']['description'].format(version),fg="white",bg="royalblue",padx=20,pady=20).grid(row=1,column=1,padx=1,pady=1)
btn2=Button(root,text=lang['main']['choose'],pady=10,padx=40,fg="white",bg="blue",command=ext)
btn2.grid(row=0,column=0,padx=10,pady=10)
btn=Button(root,text=lang['main']['exit'],pady=10,padx=40,fg="white",bg="crimson",width=8, command=root.quit)
btn.grid(row=1,column=0,padx=10,pady=10)
Button(root,text="langue",fg="white",bg="crimson",width=15,padx=10,pady=10, command=langPop).grid(row=2,column=0,padx=10,pady=10)
Button(root,text="login",fg="white",bg="darkblue",width=15,padx=10,pady=10, command=langPop).grid(row=3,column=0,padx=10,pady=10)

root.mainloop()