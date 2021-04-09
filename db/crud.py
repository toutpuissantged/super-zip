def creation(DATABASE,login,password,email):

    import hashlib,sqlite3

    if 1:    
        login=login
        password=hashlib.sha224((bytes(password,'utf8'))).hexdigest()
        conn=sqlite3.connect(DATABASE)
        cur=conn.cursor()
        cur.execute(" select id from auth ")
        for l in cur:
            id_old=l
        id_old=id_old[0]
        #login valiation
        cur.execute(" select login from auth ")
        ps=cur.fetchall()
        pseudo_olds=[]
        for l in ps:
            pseudo_olds.append(l)
            if l[0] ==login :
                cur.close()
                conn.close()
                return " username deja utilser " 
        #mail validation
        cur.execute(" select email from auth ")
        pe=cur.fetchall()
        mail_olds=[]
        for l in pe:
            mail_olds.append(l)
            if l[0] ==email :
                cur.close()
                conn.close()
                return " adresse mail deja utiliser"  
        #not empty validation
        if " "  in (login or password or email) :
            cur.close()
            conn.close()
            return " un champ etait vide  "

        elif  ' ' not in (login and password  and email):
            donnee=(id_old+1, login,password,email)
            cur.execute("insert into auth (id ,login ,password ,email) values( ?,?,?,?)",donnee)
            conn.commit()
            cur.close()
            conn.close()
            return " creation reussi"

    else:
        return 'erreur de interne veillez recharger votre page'


def connexion(DATABASE,login ,password):
    import hashlib,sqlite3
    booli=False
    if 1:
        indexor,indexor2,indexor3,indexor4=0,0,0,0
        login=login
        password=hashlib.sha224((bytes(password,'utf8'))).hexdigest()
        conn=sqlite3.connect(DATABASE)
        cur=conn.cursor()
        cur.execute(" select login from auth ")
        ps=cur.fetchall()
        pseudo_olds=[]
        for l in ps:
            pseudo_olds.append(l)
            if l[0] ==login:
                booli=True
                indexor2=indexor
            indexor+=1
        cur.execute(" select id from auth ")
        for l in cur:
            
            if indexor3==indexor2:
                id_old=l
            indexor3+=1
        id_old=id_old[0]
        if " " in (login or password ) :
            cur.close()
            conn.close()
            return " login ou password  vide ",''

        elif  ' ' not in (login and password ):
            pass 

        if booli==False :
            cur.close()
            conn.close()
            return " login incorect",''
        elif booli==True:
            cur.execute(" select password from auth ")
            for l in cur:
                if indexor4==indexor2:
                    pass_clef=l
                indexor4+=1
            pass_clef=pass_clef[0]
            if pass_clef != password:
                return " password erronee ",''
            elif pass_clef == password:
                return " connexion validee id = {} ,login ={} et password = {}".format(id_old,login,pass_clef),id_old
    else:
        return 'error'
