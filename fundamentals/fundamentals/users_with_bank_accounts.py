class BankAccount:
    
    def __init__(self, int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print('Insufficient Funds: Charging a $5 fee')
            self.balance -= 5
            return self
    
    def display_account_info(self):
        print('Balance: $' + str(self.balance))
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
            return self
        else:
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self

bob = User('Bob', 'bbuilder1945@gmail.com')
mickey = User('Mickey', 'mmouse1928@gmail.com')

bob.make_deposit(100).make_deposit(200).make_withdrawal(150).display_user_balance()
mickey.make_deposit(100).make_withdrawal(150).display_user_balance()