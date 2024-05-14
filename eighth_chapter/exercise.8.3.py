
class BankAccount(object):
    
    balance: float = 0
    
    def deposit(self, value: float):
        self.balance += value
        return True 

    def withdraw(self, value: float):
        if self.balance > 0 and self.balance >= value:
            self.balance -= value 
            return True 
        return False
    
    def show(self):
        print('A conta tem %.2f' % (self.balance))
        
account = BankAccount()

account.deposit(value=1000)
account.withdraw(value=500)
account.show()