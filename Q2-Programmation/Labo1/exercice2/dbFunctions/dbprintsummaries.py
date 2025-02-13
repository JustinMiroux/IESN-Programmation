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


    def db_print_all_from_wind_direction():
        """Print all summaries that have one or multiple specific wind directions"""

        cur = conn.cursor()
        query = 1
        search_list = []
        complete_query = []

        while query == 1:

            db_wind_direction = str(input("""Entrer la/les directions de vents
                                           (N-NE-E-SE-S-SO-O-NO) ou (Q pour quitter) : """))
            list_of_directions = ['n', 'ne', 'e', 'se', 's', 'so', 'o', 'no']

            if db_wind_direction.lower() in list_of_directions:
                search_list.append(db_wind_direction.lower())

            elif db_wind_direction.lower() == "q":
                query = 0

            else:
                print("Direction non conforme veuilliez utiliser N-NE-E-SE-S-SO-O-NO ou Q")

        for i in search_list:

            cur.execute("SELECT * FROM stationsinfo WHERE winddirection = ?", i)

            for row in cur.fetchall():

                complete_query.append(row)

        for line in complete_query:
            print(line)

        cur.close()


    def db_print_all_from_temp():
        """Print all summaries where the temperature is over the input"""

        cur = conn.cursor()

        db_temp = float(input("Entrer la température (°C) : "))
        cur.execute("SELECT * FROM stationsinfo WHERE temp > ?", db_temp)

        for row in cur.fetchall():
            print(row)

        cur.close()
