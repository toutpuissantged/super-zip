from tkinter import *

def finish(msg,props):
    root=props['root']
    top2=Toplevel(root)
    lang=props['lang']
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

