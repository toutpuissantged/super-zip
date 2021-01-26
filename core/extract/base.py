

def ext_here(props):
    props['ext_ui']['filedir2']=props['ext_ui']['filedir']
    props['music'].clickSon()
    #print(filedir2)
    decomp(props)
    
def ext_to(props):
    filedir=props['ext_ui']['filedir']
    root=props['root']
    filedialog=props['filedialog']

    props['music'].clickSon()
    root.filename =filedialog.askdirectory(title="select folder")
    filedir2=root.filename
    if filedir2=='':
        return 0
    #print(filedir2)
    props['ext_ui']['filedir2']=filedir2
    decomp(props)
    

def decomp(props):

    p1open=props['env']['main']['p1open']
    music=props['music']
    not_err=0
    finish=props['finish']
    try:
        myzip=props['zipfile'].PyZipFile(props['ext_ui']['filedir'])
        myzip.extractall(path=props['ext_ui']['filedir2'])
    except none:
        not_err=1

    if  not_err==0:
        finish(1,props)
        music.sucSon()
    else:
        finish(0,props)
        music.errorSon()
    p1open+=1
    if p1open>=3:
        #lab2.destroy()
        pass
    