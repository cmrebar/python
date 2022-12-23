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

bob_account = BankAccount()
mickey_account = BankAccount()

bob_account.deposit(50).deposit(70).deposit(80).withdraw(150).yield_interest().display_account_info()
mickey_account.deposit(20).deposit(70).withdraw(10).withdraw(10).withdraw(10).withdraw(20).yield_interest().display_account_info()
