#! python

#By toutpuissantged

from loader import *

mixer.init()

root = Tk()
root.size()
root.iconbitmap('asset/img/main.jpg')

lang=langInit("public/lang/"+env['userLang']+"/config.json",json)
root.title(lang['main']['title'])
logo = PhotoImage(file="asset/img/main.jpg")
global props

props={
    'root':root,
    'music':music,
    'filedialog':filedialog,
    'defaultdir':env['defaultdir'],
    'lang':lang,
    'finish':finish,
    'zipfile':zipfile,
    'ext':ext,
    'langPop':langPop,
    'extractor':{
        'here':ext_here,
        'to':ext_to
    },
    'ext_ui':{
        'filedir':'',
        'filedir2':'',
        'finishswetch':0
    },
    'db':{
        'name':'auth.db',
        'dir':'database/'
    },
    'auth':{
        'root':'',
        'Login':'',
        'Password':'',
        'ErrMsg':'',
        'valide':0,
        'conter':0,
    },
    'env':{
        'main':{

            'version':env['version'],
            'p1open':env['p1open'],
            'SIDEX':env['SIDEX'],
            'SIDEY':env['SIDEY'],
            'userLang':env['userLang'],
            'defaultdir':env['defaultdir'],
            'jsonDir':"public\\lang\\"+env['userLang']+"\\config.json",
            'logo':logo,

        }
        
    }

}

DATABASE=props['db']['dir']+props['db']['name']

result=connexion(DATABASE,'login' ,'password') 
print(result)
print('ok ca marche')
dbexist=True
try :
    conn=sqlite3.connect(DATABASE)
    print('connexion reussi')
except :
    print('connexion echouer')
    dbexist=False  

if dbexist:
    root_monted(props)
else:
    auth_valide=root_auth(props)
    
root.mainloop()