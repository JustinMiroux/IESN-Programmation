""""Main file with menu"""
# pylint: disable=W0401

import sqlite3
from dbFunctions.dbaddnew import db_add_new_summary
from dbFunctions.dbprintsummaries import *

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))

    cur = conn.cursor()

    try:
        cur.execute("CREATE TABLE stationsinfo(id, date, windspeed, winddirection, temp);")
    except sqlite3.DatabaseError:
        print("Database already exist")
        #pass #NEVER leave pass alone (no silent errors)

    RUNNING = 1

    while RUNNING == 1:
        print("\n Menu de la base de donnée Stations info : \n")
        print("Créer un nouveau relevé pour une station :                                   1")
        print("Afficher tous les relevés d'une station :                                    2")
        print("Afficher tous les relevés d'une date :                                       3")
        print("Afficher tous les relevés avec un vent allant dans une/des direction :       4")
        print("Afficher tous les relevés avec une température supérieur à celle donnée :    5\n")
        print("Quitter :                                                                    Q")

        CHOICE = str(input("\n: "))

        if CHOICE == "1":
            db_add_new_summary()

        elif CHOICE == "2":
            db_print_all_from_station()

        elif CHOICE == "3":
            db_print_all_from_date()

        elif CHOICE == "4":
            db_print_all_from_wind_direction()

        elif CHOICE.lower() == "q":
            RUNNING = 0
            cur.close()

        else:
            print("\n Choix Invalide !")
