#optimisation des indexation de base de donnee
def dbSelect(id,colom,DATABASE,table):
        import sqlite3
        conn=sqlite3.connect(DATABASE)
        cur=conn.cursor()
        cur.execute("SELECT "+str(colom)+" FROM "+str(table)+" WHERE id="+str(id))
        result=cur.fetchone()[0]
        cur.close()
        conn.close()
        return result

def dbUpdate(id,colom,DATABASE,table,data):
        import sqlite3
        conn=sqlite3.connect(DATABASE)
        cur=conn.cursor()
        print(" UPDATE "+str(table)+" set "+str(colom)+" = "+str(data)+" WHERE id="+str(id)+"")
        cur.execute(" UPDATE "+str(table)+" set "+str(colom)+" = '"+str(data)+"' WHERE id="+str(id)+"")
        conn.commit()
        cur.close()
        conn.close()
        return 'done'
