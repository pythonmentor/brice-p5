import requests



class Api:

    def __init__(self):
        self.product = []
        self.paylod = {'action': 'process',
                       'json': 1,
                       'countries': 'France',
                       'sort_by':'unique_scans_n',
                       'page_size': 1000,
                       'page': 1
                       }

    def get_product(self):
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=self.paylod)
        result = r.json()
        self.product.append(result['products'])
        print(result)


    def filter_data(self):
        product_details = []
        for product in self.product:
            for attribute in product:
                attributes = { 'product_name': attribute['product_name_fr'],
                               'nutriscore': attribute['nutrition_grades_tags'][0],
                               'link': 'https://world.openfoodfacts.org/product/{}'.
                                   format(attribute['code']),
                               'id': attribute['code'],
                               'store': attribute['stores'],
                               'details': self.filter_generic_name(attribute),
                               'category': self.filter_category(attribute)
                            }
                product_details.append(attributes)

    def filter_generic_name(self, attribute):
        try:
            return attribute['generic_name_fr']
        except KeyError:
            return 'Aucun'


    def filter_category(self, attribute):
        category_name = []
        try:
            return attribute['categories'].split(',')
        except KeyError:
            return 'Aucun'