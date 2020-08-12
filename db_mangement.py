import mysql.connector
from Api import *
from Setup import CATEGORIES_LIST


class Dbmanagement:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='Enurox123', host='localhost', database='mydb')
        self.cursor = self.cnx.cursor()

    def insert_categories(self):
        sql_insert_cat = "INSERT INTO Category (name) VALUES (%(category)s)"
        for category in CATEGORIES_LIST:
            category_to_add = {'category': category}
            self.cursor.execute(sql_insert_cat, category_to_add)
        self.cnx.commit()
        self.cursor.close()

    def insert_product(self):
        sql_insert_prod = ("INSERT IGNORE INTO Product (name, description, store, link, nutriscore, barcode)"
                           "VALUES((%s), (%s), (%s), (%s), (%s), (%s))")
        prod = Api()
        prod.clean_product()
        for item in prod.product_list:
            add_prod = (item['product_name'],
                        item['details'],
                        item['stores'],
                        item['link'],
                        item['nutriscore'],
                        item['code'])

            self.cursor.execute(sql_insert_prod, add_prod)
        self.cnx.commit()
        self.cursor.close()
        print('fini')


Db = Dbmanagement()
Db.insert_product()

