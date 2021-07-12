import math
class Grocery:
    def __init__(self):
        self.items = {
                'Banana': {'price': 4,   'stock': 6, 'code':1 },
                'Apple':  {'price': 2,   'stock': 0,'code':2 },
                'Orange': {'price': 1.5, 'stock': 32,'code':3},
                'Pear':   {'price': 3,   'stock': 15,'code':4},
            }
    
    def print_items(self):
        counter = 1
        for key in self.items:
            print(f"{counter}- {key}")
            counter += 1



class Bill:
    def __init__(self, grocery):
        self.grocery = grocery # Contain Dictionary
        self.price = []
        self.products = []
    
    def buy(self, quantity, code):

        for key in self.grocery.items:
            if self.grocery.items[key]['code'] == code:
                if self.grocery.items[key]['stock'] < quantity:
                    print("Out of stock")
                    total = sum(self.price);
                else:
                    self.grocery.items[key]['stock'] -= quantity
                    print (key, "| price:", self.grocery.items[key]['price'], "| Stock:", self.grocery.items[key]['stock'], "| Barcode:", self.grocery.items[key]['code'])
                    self.price.append(self.grocery.items[key]['price'] * quantity)
                    self.products.append(key)
                    total = sum(self.price);
        print("..............................................")
        return total


store = Grocery() #contain the Dictionary
bill1 = Bill(store)


finish = True
while finish:
    store.print_items()
    item_number = int(input("Please Enter the number of the item: "))
    quantity = int(input("Please enter the quantity needed: "))
    total = bill1.buy(quantity, item_number)

    exit_statment = input("Do you need somthing else (y/n): ")
    if exit_statment == "n":
        finish = False

print("Your total is:", total)