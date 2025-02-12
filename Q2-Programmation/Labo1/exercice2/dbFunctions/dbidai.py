"""File for auto incrementation"""

import sqlite3

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))


    def db_id_auto_incrementation():
        """"Auto increment from size of list"""

        cur = conn.cursor()
        cur.execute("SELECT * FROM stationsinfo")

        entirelist = []
        entirelist += cur.fetchall()

        dbid = len(entirelist)
        dbid = dbid + 1

        cur.close()

        return dbid


#if __name__ == "__main__":
#    print(db_id_auto_incrementation())
#    print(type(db_id_auto_incrementation()))
