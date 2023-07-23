

class BankAccount:

    users = []

    def __init__(self, balance):
        self.int_rate = 0.02
        self.balance = balance
        BankAccount.users.append(self)

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'Your new balance is, ${self.balance}.')
        return self

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f'Your new balance is, ${self.balance}.')
        return self

    def display_account_info(self):
        print(f'Your interest rate is, {self.int_rate}%.')
        print(f'Your current balance is, ${self.balance}.')
        return self

    def yield_interest(self):
        rate = self.balance * self.int_rate * 12
        print(f'Your yield interest rate is ${rate}.')
        return self

    @classmethod
    def all_users(cls):
        for user in cls.users:
            user.display_account_info()

user1 = BankAccount(500)
user2 = BankAccount(2000)

user1.deposit(100).deposit(150).deposit(135).withdraw(50).yield_interest().display_account_info()
user2.deposit(150).deposit(350).withdraw(100).withdraw(500).withdraw(50).withdraw(150).yield_interest().display_account_info()

BankAccount.all_users()