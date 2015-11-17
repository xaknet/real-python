import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""
    CREATE TABLE orders
    (make TEXT, model TEXT, order_date TEXT)
    """)

    orders = [
        ('Ford', 'Focus', '2015-01-21'),
        ('Ford', 'Focus', '2012-04-12'),
        ('Ford', 'Focus', '2010-09-13'),
        ('Ford', 'Fiesta', '2015-02-01'),
        ('Ford', 'Fiesta', '2015-09-05'),
        ('Ford', 'Fiesta', '2013-04-09'),
        ('Ford', 'Fusion', '2015-06-05'),
        ('Ford', 'Fusion', '2009-04-08'),
        ('Ford', 'Fusion', '2013-07-11'),
        ('Honda', 'CR-V', '2014-03-04'),
        ('Honda', 'CR-V', '2012-02-25'),
        ('Honda', 'CR-V', '2014-11-29'),
        ('Honda', 'Accord', '2012-10-22'),
        ('Honda', 'Accord', '2011-09-23'),
        ('Honda', 'Accord', '2015-04-18')
    ]

    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)

