#   GETTERS AND SETTERS ARE USED TO ACCESS THE PROTECTED VARIABLE OR METHOD AS THEY CANNOT BE ACCESSED DIRECTLY

class Bank:

    def Account(self, accNo, balance, name):
        self.name = name
        self._accNo = accNo
        self.__balance = balance

    
    def displayDetails(self):
        return f'{self.name} with account number {self._accNo}'

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if(amount<=self.__balance):
            self.__balance -= amount

        else:
            return 'INVALID AMOUNT'

    def CheckBalance(self):
        return f'BALANCE: {self.__balance}'

person1 = Bank()

person1.Account(123, 200, 'abcd')
person1.deposit(230)
person1.withdraw(100)
print(person1.displayDetails())
print(person1.CheckBalance())