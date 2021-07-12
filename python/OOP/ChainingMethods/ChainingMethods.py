class User:
    def __init__(self, name, balance ):
        self.name = name
        self.balance = balance
        print(name, balance)

    def deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount > self.balance:
            return "non sufficient funds"
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(self.balance)
        return self.balance

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.deposit(amount)
        print(other_user.name+"'s new balance:", other_user.balance,"\n" + self.name+"'s my current balance:", self.balance)
        return self


hala = User("hala", 100)
hala.deposit(100).deposit(100).deposit(100)