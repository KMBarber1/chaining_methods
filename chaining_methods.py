class User:

    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

Sanoma = User("Sanoma")
Trinity = User("Trinity")
Alexander = User("Alexander")

Sanoma.make_deposit(1000).make_deposit(2000).make_deposit(5000).make_withdrawal(3000).display_user_balance()

Trinity.make_deposit(600).make_deposit(200).make_withdrawal(100).make_withdrawal(300).display_user_balance()

Alexander.make_deposit(300).make_withdrawal(20).make_withdrawal(50).make_withdrawal(30).display_user_balance()