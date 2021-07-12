class BankAccount:
	def __init__(self, int_rate=0.01, balance=0):
	# don't forget to add some default values for these parameters! your code here! 
	# (remember, this is where we specify the attributes for our class) don't worry about user info here;
	#  we'll involve the User class soon
		self.int_rate = int_rate
		self.balance = balance
	def deposit(self, amount):
		# your code here
		self.balance += amount
		return self
	def withdraw(self, amount):
		# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
		#  if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		if (amount > self.balance):
			self.balance-=5
			print("Insufficient funds: Charging a $5 fee")
		else:
			self.balance -= amount 
		return self


	def display_account_info(self):
		# display_account_info(self) - print to the console: eg. "Balance: $100"
		print("balance: $"+str(self.balance) )

	def yield_interest(self):
		# your code here
		if (self.balance>0):
			self.balance=self.balance+(self.balance*self.int_rate)

		return self

hala_account = BankAccount(balance= 500)
saja_account = BankAccount(balance= 200)
hala_account.deposit(100).deposit(100).deposit(100).withdraw(100)
# hala balance: $700
hala_account.yield_interest().display_account_info()

saja_account.deposit(50).deposit(50).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()