#    USING PRIVATE AND PROTECTED FOR METHODS

class BankAccount:

    def __init__(self, account_pin):
        self.__account_balance = 0
        self.__account_pin = account_pin

    def __verify_pin(self, pin):
        return pin == self.__account_pin

    def _update_balance(self, amount, pin):
        if self.__verify_pin:
            
            self.__account_balance += amount

    def deposit(self, amount, pin):
        if self.__verify_pin:
            self._update_balance(amount, pin)
        else:
            return 'INVALID PIN'

    def withdraw(self, amount, pin):
        if self.__verify_pin:
            self._update_balance(-amount, pin)
        else:
            return 'INVALID PIN'

    def check_balance(self, pin):
        if self.__verify_pin:
            return self.__account_balance
        else:
            return 'INVALID PIN'

account = BankAccount('bharani')
account.deposit(100, 'bharani')
print(account.check_balance('bharani'))
account.withdraw(20, 'bharani')
print(account.check_balance('bharani'))

account._update_balance(23, 'bharani')
print(account.check_balance('bharani'))