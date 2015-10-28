"""Sets up Product Classes and actions"""

import json

class Product:
    """Create and list products"""

    def __init__(self): 
        """Init is the constructor for Python classes"""
        pass
                
    def create_product(self, product_name, product_price, product_description):
        """Save variables as instance variables, place them in a dict, 
        parse with the JSON module, then store them in a file"""

        self.name = product_name
        self.price = product_price
        self.description = product_description

        new_product = {'name': self.name, 'price': self.price, 'description': self.description}
        str_product = json.dumps(new_product)
        str_product = str_product + '\n'

        with open('data.json', 'a') as f:
            f.write(str_product)

    def list_products(self):
        """"Reads everything from data.json"""
    
        results = []
        data = []

        with open('data.json', 'r') as f:
            for line in f:
                results.append(line)

        for res in results:
            data.append(json.loads(res))

        print '========================'
        print '========================'

        for d in data:
            print d['name'], d['price'], d['description']

        print '========================'
        print '========================'
