import sqlite3
from dbIdAI import dbIdautoincrementation

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))

    cur = conn.cursor()

    try:
        cur.execute("CREATE TABLE stationsinfo(id, date, windspeed, winddirection, temp);")
    except sqlite3.DatabaseError:
        print("Database already exist")
        pass # NEVER leave pass alone (no silent errors)

    running = 1

    while running == 1:
        print("\n Menu de la base de donnée Stations info : \n")
        print(" Créer un nouveau relevé pour une station :                                              1")
        print(" Afficher tous les relevés d'une station :                                               2")
        print(" Afficher tous les relevés d'une date :                                                  3")
        print(" Afficher tous les relevés avec un vent allant dans une/des direction :                  4")
        print(" Afficher tous les relevés avec une température supérieur à une température donnée :     5\n")
        print(" Quitter :                                                                               Q")

        choice = str(input("\n: "))

        if choice == "1":

            dbId = dbIdautoincrementation()
            dbDate = str(input("Date du relevé (dd/mm/yyyy) : "))
            dbWindSpeed = int(input("Vitesse du vent (Km/H) : "))
            directionChoice = 1

            while directionChoice == 1:
                dbWindDirection = input("Direction du vent (N-NE-E-SE-S-SO-O-NO) : ")
                listOfDirections = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO']

                if dbWindDirection in listOfDirections:
                    directionChoice = 0
                else:
                    print("Direction non conforme veuilliez utiliser N-NE-E-SE-S-SO-O-NO")

            dbTemp = int(input("Temprérature (°C) : "))

            cur.execute("INSERT INTO stationsinfo (id, date, windspeed, winddirection, temp) VALUES (?, ?, ?, ?, ?)", (dbId, dbDate, dbWindSpeed, dbWindDirection, dbTemp))
                
        elif choice.lower() == "q":
            running = 0
        
        else:
            print("\n Choix Invalide !")