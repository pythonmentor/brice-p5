from P5.Dbmanagement import Dbmanagement


class Openfoodfact:

    def __init__(self):
        self.data = Dbmanagement()

    def home(self):
        print('******BIENVENUE******')
        print('********SUR**********')
        print('****OPEN FOOD FACT****')
        self.data.return_categories()
        choice_cat = int(input("Veuillez entrer le numéro de la catégorie souhaitée."))
        print(choice_cat)
        self.data.return_product(choice_cat)


op = Openfoodfact()
op.home()

