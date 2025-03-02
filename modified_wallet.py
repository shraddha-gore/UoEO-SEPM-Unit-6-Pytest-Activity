class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount - 1  # Change 1: Incorrect initialization

    def spend_cash(self, amount):
       # Change 2: Removed balance check
        self.balance += amount  # Change 3: Addition instead of subtraction

    def add_cash(self, amount):
        self.balance -= amount  # Change 4: Subtraction instead of addition
