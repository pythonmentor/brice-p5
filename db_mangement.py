import mysql.connector

from Setup import CATEGORIES_LIST


class Dbmanagement:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='Enurox123', host='localhost', database='mydb')

    def insert_categories(self):
        sql_insert = "INSERT INTO Category (name) VALUES (%(category)s)"
        cursor = self.cnx.cursor()
        for category in CATEGORIES_LIST:
            category_to_add = {'category': category}
            cursor.execute(sql_insert, category_to_add)
        self.cnx.commit()
        cursor.close()

    def insert_product(self):
        pass







