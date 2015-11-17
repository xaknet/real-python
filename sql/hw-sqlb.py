import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    data = [
        ('Ford','Focus', 3),
        ('Ford', 'Fiesta', 10),
        ('Ford', 'Fusion', 2),
        ('Honda', 'CR-V', 20),
        ('Honda', 'Accord', 5)

    ]

    c.executemany("""INSERT INTO inventory
    VALUES (?,?,?)""", data)