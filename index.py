#! /media/root/persistence/Code/gedeon/Python/VituralEnv/bin/python

#By toutpuissantged

from loader import *

mixer.init()

global lab2,p1open,defaultdir,version,lang,userLang
global music,props



root = Tk()
root.size()
#root.iconbitmap('assets\alien.png')

lang=langInit(jsonDir,json)
root.title(lang['main']['title'])
print('terminer')
cnv = Canvas(root, width=SIDEX, height=SIDEY, bg='ivory')
cnv.grid(row=2,column=1,padx=1,pady=1)
logo = PhotoImage(file="asset/img/main.jpg")
center=(50,60)
cnv.create_image(center, image=logo)

props={
    'root':root,
    'music':music,
    'filedialog':filedialog,
    'defaultdir':defaultdir,
    'lang':lang,
    'finish':finish,
    'zipfile':zipfile,
    'extractor':{
        'here':ext_here,
        'to':ext_to
    },
    'ext_ui':{
        'filedir':'',
        'filedir2':'',
        'finishswetch':0
    },
    'loader':{
        'version':'1.0',
        'p1open':0,
        'SIDEX':100,
        'SIDEY':120,
        'userLang':"fr",
        'defaultdir':"/media/root/persistence/Code/gedeon/Python/trash/",
        'jsonDir':"public\\lang\\"+userLang+"\\config.json",
    }

}

Label(root,text=lang['main']['description'].format(version),fg="white",bg="royalblue",padx=20,pady=20).grid(row=1,column=1,padx=1,pady=1)
btn2=Button(root,text=lang['main']['choose'],pady=10,padx=40,fg="white",bg="blue",command=lambda:ext(props))
btn2.grid(row=0,column=0,padx=10,pady=10)
btn=Button(root,text=lang['main']['exit'],pady=10,padx=40,fg="white",bg="crimson",width=8, command=root.quit)
btn.grid(row=1,column=0,padx=10,pady=10)
Button(root,text="langue",fg="white",bg="crimson",width=15,padx=10,pady=10, command=langPop).grid(row=2,column=0,padx=10,pady=10)
Button(root,text="login",fg="white",bg="darkblue",width=15,padx=10,pady=10, command=langPop).grid(row=3,column=0,padx=10,pady=10)

root.mainloop()