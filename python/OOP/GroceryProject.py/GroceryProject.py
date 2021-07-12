import math
class Grocery:
    def __init__(self):
        self.items = {
                'banana': {'price': 4,   'stock': 6, 'code':123 },
                'apple':  {'price': 2,   'stock': 0,'code':1231 },
                'orange': {'price': 1.5, 'stock': 32,'code':1233},
                'pear':   {'price': 3,   'stock': 15,'code':12335},
            } 
class Bill:
    def __init__(self, grocery):
        self.grocery = grocery
        self.price = []
        self.products = []
    def buy(self, quantity, code):
        for key in self.grocery.items:
            if self.grocery.items[key]['code'] == code:
                print("item found")
                print (key)
                print ("price: %s" % self.grocery.items[key]['price'])
                print ("stock: %s" % self.grocery.items[key]['stock'])
                print ("Barcode: %s" % self.grocery.items[key]['code'])
                self.price.append(self.grocery.items[key]['price'])
                self.products.append(key)
                print(self.price)
                print(self.products)
        print("..............................................")
store = Grocery()
bill1 = Bill(store)
bill1.buy(3, 1231)