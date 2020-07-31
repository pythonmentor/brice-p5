import mysql.connector
from Api import Api


class Dbmanagement:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='enurox123', host='localhost', database='mydb')
        self.data = Api()
        self.data.clean_product()

    def insert_categories(self):
        cursor = self.cnx.cursor()
        for item['categories'] in self.data.product_list:
            cursor.executemany("""Insert IGNORE INTO Category(name)
                              VALUES (%(item['categories'])s""")

        self.cnx.commit()
        cursor.close()

    def insert_product(self):
        pass


dat = Dbmanagement()
dat.insert_categories()






