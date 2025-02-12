"""Files for printing différent summaries"""

import sqlite3

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))


    def db_print_all_from_station():
        """Print all summaries from a specific station"""

        cur = conn.cursor()

        db_id = int(input("Entrer l'id de la station : "))
        cur.execute("SELECT * FROM stationsinfo WHERE id = ?", db_id)

        for row in cur.fetchall():
            print(row)

        cur.close()


    def db_print_all_from_date():
        """Print all summaries from a specific date"""

        cur = conn.cursor()

        db_date = str(input("Entrer la date (dd/mm/yyyy) : "))
        cur.execute("SELECT * FROM stationsinfo WHERE date = ?", db_date)

        for row in cur.fetchall():
            print(row)

        cur.close()
