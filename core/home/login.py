from loader import *

def root_auth(props):
    auth=Toplevel(props['root'])
    props['auth']['root']=auth
    root=auth
    auth.title('login')
    ext=props['ext']
    env=props['env']['main']
    SIDEX=env['SIDEX']
    SIDEY=env['SIDEY']
    version=env['version']
    p1open=env['p1open']
    lang=props['lang']
    langPop=props['langPop']
    valide=0

    print('auth')

    Label(root,text='enregistrer vous ',fg="white",bg="royalblue",padx=20,pady=20,width=20).grid(row=1,column=1,padx=0,pady=0)
    Label(root,text=' pour continuer',fg="white",bg="royalblue",padx=20,pady=20,width=20).grid(row=1,column=2,padx=0,pady=0)
    Label(root,text='nom d\'utilisateur ').grid(row=2,column=1,padx=1,pady=10)
    Login=Entry(root)
    Login.grid(row=2,column=2,padx=1,pady=1)
    Label(root,text='mot de passe').grid(row=3,column=1,padx=10,pady=10)
    Password=Entry(root)
    Password.grid(row=3,column=2,padx=20,pady=10)
    Button(root,text='valider',fg="white",bg="royalblue",padx=20,pady=6,command=lambda:submit_auth(props)).grid(row=4,column=1,padx=1,pady=5)
    Button(root,text='annuler',fg="white",bg="crimson",padx=20,pady=6,command=root.quit).grid(row=4,column=2,padx=1,pady=5)
    props['auth']['Login']=Login
    props['auth']['Password']=Password
    return props['auth']['valide']
 
def submit_auth(props):
    #print('auth submit')
    root=props['auth']['root']
    Login=props['auth']['Login']
    Password=props['auth']['Password']
    
    Lget=Login.get()
    Pget=Password.get()
    if (Lget=='' or Pget==''):
        print('valeur empty')
        ErrMsg=Label(root,text='les champs doivent \n etre remplie',bg="crimson",fg="white",padx=20,pady=6)
        ErrMsg.grid(row=5,column=1,padx=1,pady=10)
        props['auth']['ErrMsg']=ErrMsg
        props['auth']['conter']+=1
        return 0
    else:
        if(props['auth']['conter']>0):
            props['auth']['ErrMsg'].destroy()
            print('objet detruit')
        print(Lget,Pget)
    props['auth']['valide']=1
    root_monted(props)
    def callback():
        time.sleep(0.01)
        props['auth']['root'].destroy()     
    callback()
    return 1
