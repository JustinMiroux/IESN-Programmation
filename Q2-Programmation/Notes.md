# Programmation 4

## Les environements virtuel

* ``python3 -m venv .venv`` : Créer un nouvelle environement virtuel dans le dossier .venv
* ``source .venv/bin/activate`` : Active l'environement virtuel (Linux)
* ``.\.venv\script\activate.ps1`` : Active l'environement virtuel (Windows Powershell) ! Ne pas lancer python3 dans le venv (ne trouve pas les modules importer)
* ``.\.venv\script\activate.bat`` : Active l'environement virtuel (Windows CMD)
* ``deactivate`` : Désactive l'environement
* ``pip3 install matplotlib`` : Installer les libraries
* ``pip3 freeze > requirements.txt`` : Créer une liste des packets installer dans le venv
* ``pip3 install -r requirements.txt`` : Retelecharge les librairies dans la liste de texte

## Les bases de données

* Créer une base de donnéer et si (de)connecter avec python
```python
import sqlite3

conn = squlite3.connect("db.sqlite") #créer la db si n'existe pas

print(type(conn))

conn.close() #ferme la connection

#encore mieux : with
with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))
```
* Pour créer une table
```python
import sqlite3

with sqlite3.connect("db.sqlite") as conn:

    with conn.cursor() as cur:
        cur.execute("CREATE TABLE videogames(name, year, rating);")
```
* Pour créer insérer des données
```python
import sqlite3

with sqlite3.connect("db.sqlite") as conn:

    with conn.cursor() as cur:
        cur.execute("INSERT INTO videogames('fortnite', 2017, 4)")
        cur.execute("INSERT INTO videogames('BG3', 2023, 9)")

        conn.commit() # Validation des modifications des données

        cur.execute("INSERT INTO videogames('Skyrim', 2011, 8)")
        conn.commit() # Auto commit si close (with too) 

        cur.execute("INSERT INTO videogames('Diablo 2', 1999, 8)")
        conn.rollback() # Annule l'insertion
```
* Pour récupérer/selectioner des données
```python
import sqlite3

with sqlite3.connect("db.sqlite") as conn:

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM videogames")
        print(cur.fetchone())
        print(cur.fetchone())
        print(cur.fetchone())
        print(cur.fetchone())

        cur.execute("SELECT * FROM videogames")
        print(cur.fetchall())

        for row in cur.execute("SELECT * FROM videogames"):
            print(row)
```
* Pour changer les données
```python
import sqlite3

with sqlite3.connect("db.sqlite") as conn:

    with conn.cursor() as cur:
        cur.execute("UPDATE videogames SET rating = 3 WHERE name = 'fortnite'")
        conn.commit()
        print(cru.rowcount)
        print(cur.execute("SELECT * FROM videogames WHERE name = 'fortnite'").fetchone())
```
* Pour la suppression de données
```python
import sqlite3

with sqlite3.connect("db.sqlite") as conn:

    with conn.cursor() as cur:
        cur.execute("DELETE FROM videogames WHERE name = 'Skyrim'")
        conn.commit()
        print(cru.rowcount)
        print(cur.execute("SELECT * FROM videogames WHERE name = 'Skyrim'").fetchone())
```
* Pour récupérer le nom des colones
```python
import sqlite3

with sqlite3.connect("db.sqlite") as conn:

    conn.row_factory = sqlite3.Row

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM videogames")
        row = cur.fetchone()
        print(row.keys())
        print(row["name"])
```

### ! PARTIES MANQUANTE ! (Postgresql, ...)

## DOTENV

Sert a mettre des mdp et compte utilisateur / paramètre dans un fichier autre que le code source.

```dotenv
DB_HOST=localhost
DB_USER=pythonapp
```

Utiliser le fichier d'environnement

```python
import psycopg
import dotenv # Nécessaire pour lire le fichier d'environement
import os # Même chose

dotenv.load_dotenv()

host = os.getenv('DB_HOST')
user = os.getevn('DB_USER')

with psycopg.connect(f"host={host} user{user}")
```

## La sérialisation

Comment on sérialise en python / Comment on deserialise (DANS LE MÊME FICHIER)

```python
import json

a = [1, 'abc', {'x': 5, 'y': None}]
print(type(a))
json_text = json.dumps(a)
print(json_text)

a_from_json = json.loads(json_text)
print(type(a_from_json))
print(a_from_json)
```

! Attention au tableau d'encodage si le type n'est pas dans le tableau pas sérialisable. Donc impossible de sérialiser ces propres objets.

Si on a pas besoin de sérialiser en texte claire on peux le faire en binaire (pickle)

```python
import pickle # serialisation en binaire

a = [1, 'abc', {'x': 5, 'y': None}]
a_bytes = pickle.dumps(a)
print(type(a_bytes))
print(a_bytes)

a_from_bytes = pickle.loads(a_bytes)
print(a_from_bytes)
```
! Attention ne jamais déserialiser des données de provenances inconnue (risque d'execution de code arbitraire) !

Attention pickle ne fonctionne qu'avec python contrairement à JSON. Mais il peux serialiser les objets que l'on a créer.

On va essayer de sauvegarder ça en DB

```python
import psycopg
import dotenv # Nécessaire pour lire le fichier d'environement
import os # Même chose

class MyClass:
    # parties manquante

dotenv.load_dotenv()

host = os.getenv('DB_HOST')
user = os.getevn('DB_USER')
password = os.getenv('DB_PASSWD')
dbname = os.getenv('DB_NAME')

with psycopg.connect(f"host={host} user{user} password{password} dbname{dbname}")
print("Connection established")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS pickles(blob_bytes);""")

custom_object = MyClass(value: "toto", integer:69)
bytes_to_save = pickle.dumps(custom_object)

cur.execute("INSERT INTO pickles VALUES (%s);", [bytes_to save])

bytes_from_db = cur.execute("SELECT * FROM pickles;").fetchone()[0]
object_deserialised = pickles.loads(bytes_from_db)
```

Il faut que les deux coté ais la définition.

## La concurrence (concurrent.futures)

Même chose que les threads en plus poussé pour gérer les erreur et voir l'utilisation
Exemple avec les thread et la concurrence

```python
import concurrent.futures

import time

def wait(s):
    time.sleep(s)
    print(f"Waited {s} seconds,")

# On créer un executor dans un environement with

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(5):
        executor.submit(wait, i) # On soumet une tache : la fonction wait avec le paramètres i
    print ("Task submitted")
    # avec l'environement with, on ne sort pas tant qu'il reste des taches non terminées.

# ici, les taches sont terminées
print ("Finished")
```

Sans with le thread principal continue d'executer la suite du code sans attendre la fin des autres taches.

```python
import concurrent.futures

import time

def wait(s):
    time.sleep(s)
    return f"Waited {s} seconds,"

# On créer un executor dans un environement with

executor = concurrent.futures.ThreadPoolExecutor()
futures = []
for i in range(5):
    future = executor.submit(wait, i)# On soumet une tache : la fonction wait avec le paramètres i
    # on récupère l'objet future associé au thread
    futures.append(future)
print ("Task submitted")

#au fur et a mesure de la completion des threads on affiche le résultat
for future in concurrent.futures.as_completed(futures):
    print(future.result())

print ("Finished")
```

pour les insertion en db il faut des '' autour des ? qui sont des string