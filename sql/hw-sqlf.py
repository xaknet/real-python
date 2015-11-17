import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()


    sql = {'Focus count'    : "SELECT count(make) FROM orders WHERE model = 'Focus'",
            'Civic count'   : "SELECT count(make) FROM orders WHERE model = 'Civic'",
            'Ranger count'  : "SELECT count(make) FROM orders WHERE model = 'Ranger'",
            'Accord count'  : "SELECT count(make) FROM orders WHERE model = 'Accord'",
            'Avenger count' : "SELECT count(make) FROM orders WHERE model = 'Avenger'",}


    for keys, values in sql.iteritems():
        c.execute(values)

        result = c.fetchone()

        print keys + ":", result[0]