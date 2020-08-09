from db_mangement import Dbmanagement
from Api import Api

if __name__ == '__main__':
    ap = Api()
    ap.clean_product()
    data = Dbmanagement()
    data.insert_categories()


