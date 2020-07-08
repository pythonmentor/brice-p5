import mysql.connector


class Drop:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='enurox123', host='localhost', database='mydb')

    def drop_all(self):
        cursor = self.cnx.cursor()
        clean_product = "TRUNCATE TABLE Product"
        clean_cat = " TRUNCATE Category"
        clean_sub = "TRUNCATE TABLE substitute"
        cursor.execute(clean_product, clean_cat, clean_sub)
        self.cnx.commit()
        cursor.close()


use = Drop()
use.drop_all()
