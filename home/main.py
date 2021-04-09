from tkinter import *

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

    my_menu=Menu(root)
    root.config(menu=my_menu)
    file_menu=Menu(my_menu)
    my_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Open New",command=root.quit)
    file_menu.add_command(label="Open Recent",command=root.quit)
    file_menu.add_command(label="Exit",command=root.quit)   

    file_menu2=Menu(my_menu)
    my_menu.add_cascade(label="Option",menu=file_menu2)

    file_menu3=Menu(my_menu)
    my_menu.add_cascade(label="A propos",menu=file_menu3)

    cnv = Canvas(root, width=SIDEX, height=SIDEY, bg='ivory')
    cnv.grid(row=2,column=1,padx=1,pady=1)
    #logo = PhotoImage(file="main.jpg")
    logo=env['logo']
    center=(50,60)
    cnv.create_image(center, image=logo)
    Label(root,text=lang['main']['description'].format(version),fg="white",bg="royalblue",padx=20,pady=20).grid(row=1,column=1,padx=1,pady=1)
    btn2=Button(root,text=lang['main']['choose'],pady=10,padx=40,fg="white",bg="blue",command=lambda:ext(props))
    btn2.grid(row=0,column=0,padx=10,pady=10)
    btn=Button(root,text=lang['main']['exit'],pady=10,padx=40,fg="white",bg="crimson",width=8, command=root.quit)
    btn.grid(row=1,column=0,padx=10,pady=10)
    Button(root,text="langue",fg="white",bg="crimson",width=15,padx=10,pady=10, command=langPop).grid(row=2,column=0,padx=10,pady=10)
    Button(root,text="login",fg="white",bg="darkblue",width=15,padx=10,pady=10, command=langPop).grid(row=3,column=0,padx=10,pady=10)
#correctement commiter