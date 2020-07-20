import requests


class Api:

    def __init__(self):
        self.parameters = {'action': 'process',
                           'json': 1,
                           'countries': 'France',
                           'sort_by': 'unique_scans_n',
                           'page_size': 100,
                           'page': 1
                           }
        self.product_list = []
        self.categories_list = []

    def get_product(self):
        products = []
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=self.parameters)
        result = r.json()
        products.append(result['products'])
        return products

    def filter_data(self):
        products = self.get_product()
        for product in products:
            for attribute in product:
                try:
                    attributes = {'product_name': attribute['product_name_fr'],
                                  'nutriscore': attribute['nutrition_grades_tags'][0],
                                  'link': 'https://world.openfoodfacts.org/product/{}'.format(attribute['code']),
                                  'id': attribute['code'],
                                  'details': attribute['generic_name_fr'],
                                  'stores': attribute['stores_tags'][0].strip(),
                                  'categories': self.filter_category(attribute)
                                  }

                except (IndexError, KeyError):
                    continue

                self.product_list.append(attributes)

    def filter_category(self, attribute):
        categories = attribute['categories'].split(',')
        for category_to_add in categories:
            category = category_to_add.strip().capitalize()
            return category

    def clean_product(self):
        self.filter_data()
        dict_keys = self.product_list[0].keys()
        for detail in self.product_list:
            for keys in dict_keys:
                if not detail[keys]:
                    self.product_list.remove(detail)


d = Api()
d.clean_product()

