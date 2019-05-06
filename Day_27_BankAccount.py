"""
Day 27 - Bank Account

Exercism


Simulate a bank account supporting opening/closing, withdrawals, and deposits of money. Watch out for concurrent transactions!

A bank account can be accessed in multiple ways. Clients can make deposits and withdrawals using the internet, mobile phones, etc. Shops can charge against the account.

Create an account that can be accessed from multiple threads/processes (terminology depends on your programming language).

It should be possible to close an account; operations against a closed account must fail.

Instructions
Run the test file, and fix each of the errors in turn. When you get the first test to pass, go to the first pending or skipped test, and make that pass as well. When all of the tests are passing, feel free to submit.

Remember that passing code is just the first step. The goal is to work towards a solution that is as readable and expressive as you can make it.

requires additional modules
"""

class BankAccount(object):
    def __init__(self):
        self._balance = 0
        self._status = False
        self._error = ".+"

    def get_balance(self):
        if self._status:
            return self._balance
        else:
            raise ValueError(self._error)

    def open(self):
        if not self._status:
            self._status = True
        else:
            raise ValueError(self._error)

    def deposit(self, amount):
        if self._status and amount >= 0:
            self._balance += amount
        else:
            raise ValueError(self._error)

    def withdraw(self, amount):
        if not self._status or (amount < 0 or amount > self._balance):
            raise ValueError(self._error)
        elif self._balance >= amount:
            self._balance -= amount

    def close(self):
        if self._status:
            self._status = False
            self._balance = 0
        else:
            raise ValueError(self._error)

