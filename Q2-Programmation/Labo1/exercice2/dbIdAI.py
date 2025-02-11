import sqlite3

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))

    cur = conn.cursor()

    def dbIdautoincrementation():
        cur.execute("SELECT * FROM stationsinfo")
        
        entirelist = []
        entirelist += cur.fetchall()
        
        dbId = len(entirelist)
        dbId = dbId + 1 
        return dbId

#if __name__ == "__main__":
#    print(dbIdautoincrementation())
#    print(type(dbIdautoincrementation()))