""""File for adding a new station summary"""

import sqlite3
from dbidai import db_id_auto_incrementation

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))


    def db_add_new_summary():
        """Add a new seummary in the DB"""

        cur = conn.cursor()

        db_id = db_id_auto_incrementation()
        db_date = str(input("Date du relevé (dd/mm/yyyy) : "))
        db_wind_speed = int(input("Vitesse du vent (Km/H) : "))
        direction_choice = 1

        while direction_choice == 1:
            db_wind_direction = input("Direction du vent (N-NE-E-SE-S-SO-O-NO) : ")
            list_of_directions = ['n', 'ne', 'e', 'se', 's', 'so', 'o', 'no']

            if db_wind_direction.lower() in list_of_directions:
                direction_choice = 0
            else:
                print("Direction non conforme veuilliez utiliser N-NE-E-SE-S-SO-O-NO")

        db_temp = int(input("Temprérature (°C) : "))

        cur.execute("""INSERT INTO stationsinfo (id, date, windspeed, winddirection, temp)
                     VALUES (?, ?, ?, ?, ?)""",
                     (db_id, db_date, db_wind_speed, db_wind_direction, db_temp))

        run_confirmation = 0

        while run_confirmation == 0:

            confirmation = input("Confirmer ? (Y/N) : ")

            if confirmation.lower() == "y":
                conn.commit()
                run_confirmation = 1
                cur.close()

            elif confirmation.lower() == "n":
                conn.rollback()
                run_confirmation = 1
                cur.close()

            else:
                print("Choix non comforme veuilliez utiliser Y/N")
                run_confirmation = 0
