import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""
     UPDATE inventory SET Quantity = 10
     WHERE Make='Ford' AND Model='Focus'
     """)

    c.execute("""UPDATE inventory SET Quantity = 1
     WHERE Make='Honda' AND Model='Accord'
     """)

    c.execute(""" SELECT * FROM inventory
    ORDER by Make
    """)

    rows = c.fetchall()

    print "\nNew Updated Data is : \n"

    for r in rows:
        print "{0} | {1} | {2}".format(r[0], r[1], r[2])