def langInit(jsonDir,json):
    fop=open(jsonDir,'r')
    lang=fop.read()
    fop.close()
    lang=json.loads(lang)
    #print(lang)
    return lang

