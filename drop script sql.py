import mysql.connector


class Drop:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='enurox123', host='localhost', database='mydb')

    def drop_all(self):
        cursor = self.cnx.cursor()
        clean_product = "DROP TABLE Product"
        clean_cat = "DROP TABLE Category"
        clean_sub = "DROP TABLE substitute"
        cursor.execute(clean_product, clean_cat, clean_sub)
        self.cnx.commit()
        cursor.close()


use = Drop()
use.drop_all()
