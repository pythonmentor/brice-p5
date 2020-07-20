import mysql.connector
from Api import Api


class Dbmanagement:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='enurox123', host='localhost', database='mydb')
        self.data = Api()

    def insert_categories(self):
        self.data.clean_product()
        cursor_cat = self.cnx.cursor()
        for category in self.data.categories_list:
            cursor_cat.executemany("""Insert INTO Category
                                (name)
                                VALUES
                                (%(category)s""")
        self.cnx.commit()
        cursor_cat.close()

    def insert_data(self):
        self.data.clean_product()
        cursor = self.cnx.cursor()
        for item in self.data.product_list:
            cursor.executemany("""Insert IGNORE INTO Category
                                (name)
                              VALUES
                               (%(item['categories']);""")

        self.cnx.commit()
        cursor.close()


l = Dbmanagement
l.insert_data()






