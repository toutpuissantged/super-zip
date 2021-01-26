from tkinter import *
from PIL import ImageTk,Image

def root_monted(props):
    root=props['root']
    ext=props['ext']
    env=props['env']['main']
    SIDEX=env['SIDEX']
    SIDEY=env['SIDEY']
    version=env['version']
    p1open=env['p1open']
    lang=props['lang']
    langPop=props['langPop']

    print('terminer')
    cnv = Canvas(root, width=SIDEX, height=SIDEY, bg='ivory')
    cnv.grid(row=2,column=1,padx=1,pady=1)
    logo = PhotoImage(file="main.jpg")
    center=(50,60)
    cnv.create_image(center, image=logo)
    Label(root,text=lang['main']['description'].format(version),fg="white",bg="royalblue",padx=20,pady=20).grid(row=1,column=1,padx=1,pady=1)
    btn2=Button(root,text=lang['main']['choose'],pady=10,padx=40,fg="white",bg="blue",command=lambda:ext(props))
    btn2.grid(row=0,column=0,padx=10,pady=10)
    btn=Button(root,text=lang['main']['exit'],pady=10,padx=40,fg="white",bg="crimson",width=8, command=root.quit)
    btn.grid(row=1,column=0,padx=10,pady=10)
    Button(root,text="langue",fg="white",bg="crimson",width=15,padx=10,pady=10, command=langPop).grid(row=2,column=0,padx=10,pady=10)
    Button(root,text="login",fg="white",bg="darkblue",width=15,padx=10,pady=10, command=langPop).grid(row=3,column=0,padx=10,pady=10)
