class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance



account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob")  # default balance = 0

print("Account 1 owner:", account1.owner, "Balance:", account1.balance)
print("Account 2 owner:", account2.owner, "Balance:", account2.balance)