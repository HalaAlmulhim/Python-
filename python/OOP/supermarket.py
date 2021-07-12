import pandas

class Data:
    """Creates a pandas dataframe out of a text file"""
    def __init__(self, datafile = "products.txt"):
        self.datafile = datafile

    def get_dataframe(self):
        df = pandas.read_csv("products.txt", index_col = "name")
        return df

    def save_to_csv(self):
        df = pandas.read_csv("products.txt", index_col = "name")
        df.to_csv(self.datafile)
        print(df)


class Product:
    """Represent a product from the dataframe table"""

    def __init__(self, name, dataframe = Data().get_dataframe()):
        self.name = name
        self.dataframe = dataframe

    def get_amount(self):
        """Return the available amount of the product object taken from the dataframe"""
        return self.dataframe.loc[self.name, "amount"]

    def add_amount(self, amount, password):
        """Changes the dataframe by adding an amount to the existing amount"""
        if password == 1234:
            self.dataframe.loc[self.name, "amount"] += amount
            data = Data()
            data.save_to_csv()
            print("Saved")
        else:
            return "You're not a manager"

    def remove_component(self, person):
        """Changes the dataframe by removing an amount from the existing amount"""
        if password == 1234:
            self.dataframe.loc[self.name, amount] -= 1
        else:
            return "You're not a manager"

    def __del__(self):
        """Delete the dataframe from memory when Product is destroyed"""
        del self.dataframe
        Data().save_to_csv()