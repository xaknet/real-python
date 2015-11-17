import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    data = [
        ('Boston', 'MA', 600000),
        ('Los Angeles', 'CA', 380000000),
        ('Houston', 'TX', 2100000),
        ('Philadelphia', 'PA', 15000000),
        ('San Antonio', 'TX', 14000000),
        ('San Diego', 'CA', 130000),
        ('Dallas', 'TX', 1200000),
        ('San Jose', 'CA', 900000),
        ('Jacksonville', 'FL', 800000),
        ('Indianapolis', 'IN', 800000),
        ('Austin', 'TX', 800000),
        ('Detroit', 'MI', 700000)
    ]

    c.executemany("INSERT INTO population VALUES(?, ?, ?)", data)

    c.execute("SELECT * FROM population WHERE population > 10000000")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]