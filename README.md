# Problem Statement

Copy the following code into a file named `wallet.py`:

```
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# wallet.py

class InsufficientAmount(Exception):
    pass

class Wallet(object):
    def **init**(self, initial_amount=0):
    self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
```

Copy the following code into a file named `test_wallet.py`:

```
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
    wallet.spend_cash(100)
```

Run the tests using the command: `pytest -q test_wallet.py` .You should see the following output:

![before](https://github.com/user-attachments/assets/3ce53a45-ab97-420e-8c79-3b64d8421c14)

Amend the code so that the tests fail.

# Results

![after](https://github.com/user-attachments/assets/e260c91a-474b-4603-af4f-b4273e2f1767)

The changes are included in the `modified_wallet.py` file. The test failures and their reasons are listed below:

1. `test_default_initial_amount`: Fails because the default balance will be 1 instead of 0.
2. `test_setting_initial_amount`: Fails because the balance will be 99 instead of 100.
3. `test_wallet_add_cash`: Fails because add_cash() subtracts the amount.
4. `test_wallet_spend_cash`: Fails because spend_cash adds the amount.
5. `test_wallet_spend_cash_raises_exception_on_insufficient_amount`: Fails because the balance check condition is removed.
