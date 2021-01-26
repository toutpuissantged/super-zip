#! /media/root/persistence/Code/gedeon/Python/VituralEnv/bin/python

#By toutpuissantged

from loader import *

mixer.init()

root = Tk()
root.size()
root.iconbitmap('asset/img/main.jpg')

lang=langInit("public\\lang\\"+env['userLang']+"\\config.json",json)
root.title(lang['main']['title'])

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
    'env':{
        'main':{

            'version':env['version'],
            'p1open':env['p1open'],
            'SIDEX':env['SIDEX'],
            'SIDEY':env['SIDEY'],
            'userLang':env['userLang'],
            'defaultdir':env['defaultdir'],
            'jsonDir':"public\\lang\\"+env['userLang']+"\\config.json",

        }
        
    }

}

root_monted(props)
root.mainloop()