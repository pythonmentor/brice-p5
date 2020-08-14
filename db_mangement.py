import mysql.connector
from Api import *
from Setup import CATEGORIES_LIST


class Dbmanagement:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='myuser',
            password='daPython.2020',
            host='localhost',
            database='mydb',
        )
        self.cursor = self.cnx.cursor()

    def insert_categories(self):
        cursor = self.cnx.cursor()
        sql_insert_cat = "INSERT INTO Category (name) VALUES (%(category)s)"
        for category in CATEGORIES_LIST:
            category_to_add = {'category': category}
            cursor.execute(sql_insert_cat, category_to_add)
        self.cnx.commit()
        cursor.close()

    def insert_product(self):
        cursor = self.cnx.cursor()
        sql_insert_prod = (
            "INSERT IGNORE INTO Product (id, name, description, store, link, nutriscore, category_id)"
            "VALUES(%(code)s, %(product_name)s, %(details)s, %(stores)s, %(link)s, %(nutriscore)s, (SELECT id from Category WHERE name = %(categories)s))"
        )
        prod = Api()
        prod.clean_product()
        for item in prod.product_list:
            cursor.execute(sql_insert_prod, item)
        self.cnx.commit()
        cursor.close()
        print('fini')


Db = Dbmanagement()
Db.insert_categories()
Db.insert_product()

