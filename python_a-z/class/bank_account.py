class Bank:
    def __init__(self, balance=0,account_number=None,account_holder=None):
        self.account_number = account_number
        self.account_holder = account_holder
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def get_balance(self):
        return self.balance
    
my_account = Bank(1000, "123456789", "John Doe")
print(f"Account Holder: {my_account.account_holder}")

my_account.deposit(50)
print(f"New Balance after deposit: {my_account.get_balance()}")