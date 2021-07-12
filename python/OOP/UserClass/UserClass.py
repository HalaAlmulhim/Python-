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
layan = User("layan", 0)
zaid = User("zaid", 0)

hala.deposit(100)
hala.deposit(100)
hala.deposit(100)
# hala's new balance is 400
hala.make_withdrawal(50)
# hala's new balance is 350
hala.display_user_balance()

layan.deposit(100)
layan.deposit(100)
# layan's new balance is 200
layan.make_withdrawal(50)
# layan's new balance is 150
layan.display_user_balance()

zaid.deposit(500)
# zaid's new balance is 500
zaid.make_withdrawal(50)
zaid.make_withdrawal(50)
zaid.make_withdrawal(50)
# zaid's new balance is 350
zaid.display_user_balance()

hala.transfer_money(zaid,100)
# hala's new balance should be 250
# zaid's new balance should be 450



