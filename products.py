"""Sets up Product Classes and actions"""

import json

class Product:
    """Create and list products"""

    def __init__(self): 
        pass
                
    def create_product(self, product_name, product_price, product_description):
        """Grab the instance variables, place them in a dict, pickle them, then store them in a file"""

        self.name = product_name
        self.price =  product_price
        self.description = product_description

        new_product = {'name': self.name, 'price': self.price, 'description': self.description}
        #str_product = pickle.dumps(new_product)
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
            new_res = res.rstrip('\n')
            data.append(json.loads(new_res))

        print '========================'
        print '========================'

        for d in data:
            print d['name'], d['price'], d['description']

        print '========================'
        print '========================'
