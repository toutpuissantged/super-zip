def langPop():
    top3=Toplevel(root)
    top3.title('Langues')
    fg='white'
    bg='crimson'
    langList=["francais","anglais","espagnol","allemand"]
    langAcr=["fr","en","es","de"]
    clicked=StringVar()
    clicked.set(langList[0])
    Label(top3,text='Choisir votre langues',bg=bg,fg=fg,pady=10,padx=40).pack()
    drop=OptionMenu(top3,clicked,*langList)
    drop.pack()
    btn3=Button(top3,text='choisir',pady=10,padx=40,fg="white",bg="royalblue",command=lambda:langValid(clicked.get()))
    btn3.pack(padx=10,pady=10)
    btn3=Button(top3,text=lang['popup']['close'],pady=10,padx=40,fg="white",bg="crimson",command=top3.destroy)
    btn3.pack(padx=10,pady=10)

def langValid(choix):
    langList=["francais","anglais","espagnol","allemand"]
    langAcr=["fr","en","es","de"]
    lock=0
    for i in langList:
        if i==choix:
            lock=langList.index(i)
            break
    lang=langInit("public/lang/"+langAcr[lock]+"/config.json")
    print("{} choisi ".format(langList[lock]))
