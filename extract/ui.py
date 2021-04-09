from tkinter import *

def ext(props):

    props['music'].clickSon()
    global lab2,err_msg,top
    err_msg=''
    root =props['root']
    lang=props['lang']
    ext_here=props['extractor']['here']
    ext_to=props['extractor']['to']

    root.filename = props['filedialog'].askopenfilename(initialdir=props['defaultdir'],title="select files",filetypes=(('zip files','*.zip'),('all','*.*')))
    filedir=root.filename
    if filedir=='':
        return 0
    top=Toplevel(root)
    dirList=filedir.split('/')
    top.title('zip :  {}'.format(dirList[-1]))
    props['ext_ui']['filedir']=filedir
    
    #print(dirList)
    Label(top,text=lang['tools']['dir']+" : "+filedir+'\n '+lang['tools']['name']+' : '+dirList[-1],bg='darkblue',fg='white',pady=10,padx=40 ).pack()
    btn2=Button(top,text=lang['tools']['here'],pady=10,padx=40,fg="white",bg="royalblue",command=lambda:ext_here(props))
    btn2.pack(padx=10,pady=10)
    btn=Button(top,text=lang['tools']['to'],pady=10,padx=40,fg="white",bg="royalblue",command=lambda:ext_to(props))
    btn.pack(padx=10,pady=10)
    btn=Button(top,text=lang['tools']['close'],pady=10,padx=40,fg="white",bg="crimson",command=top.destroy)
    btn.pack(padx=10,pady=10)
 