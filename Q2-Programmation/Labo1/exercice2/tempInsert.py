import sqlite3

with sqlite3.connect("db.sqlite") as conn:
    print(type(conn))

    cur = conn.cursor()

    cur.execute("INSERT INTO stationsinfo VALUES (1, '12/12/2012', 56, 'N', 2)")
    cur.execute("INSERT INTO stationsinfo VALUES (2, '10/10/2010', 68, 'S', 10)")
    cur.execute("INSERT INTO stationsinfo VALUES (3, '11/11/2011', 80, 'E', 6)")

    conn.commit()
