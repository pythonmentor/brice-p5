import requests


class Api:

    def __init__(self):
        self.parameters = {'action': 'process',
                           'json': 1,
                           'countries': 'France',
                           'sort_by': 'unique_scans_n',
                           'page_size': 1000,
                           'page': 1
                           }

    def get_product(self):
        products = []
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=self.parameters)
        result = r.json()
        products.append(result['products'])
        return products

    def filter_data(self):
        products = self.get_product()
        product_details = []
        for product in products:
            for attribute in product:
                try:
                    attributes = {'product_name': attribute['product_name_fr'],
                                  'nutriscore': attribute['nutrition_grades_tags'][0],
                                  'link': 'https://world.openfoodfacts.org/product/{}'.format(attribute['code']),
                                  'id': attribute['code'],
                                  'details': self.filter_generic_name(attribute),
                                  'store:': attribute['stores']
                                  }

                except KeyError:
                    return 'Aucun'
                else:
                    product_details.append(attributes)
                finally:
                    return product_details

    def filter_generic_name(self, attribute):
        try:
            return attribute['generic_name_fr']

        except KeyError:
            return None

d = Api()
d.filter_data()
