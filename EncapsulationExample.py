class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance  # protected variable
        self.__pin = pin  # private variable

    # Public methods to access the variables
    def print_public_owner_Name(self):
        print(f"The owner of the bank account is {self.owner} ")

    def print_protected_balance(self):
        print(f"The Balance in the bank account is {self._balance} ")

    def print_private_pin(self):
        print(f"The Pin of the bank account is {self.__pin} ")


class SavingsAcount(BankAccount):
    def __init__(self, owner, balance, pin, interest_rate):
        super().__init__(owner, balance, pin)
        self.interest_rate = interest_rate

    def print_interest_rate(self):
        print(f"Intereest rate is : {self.interest_rate}")


class CallingClass:
    ba = BankAccount("Akhilesh",10000,1234)

    # access the attributes directy
    print("Acess variables without method")
    print(ba.owner)
    print(ba._balance)
    print(ba.__pin)
    
'''
    # access the attributes using public method
    print("Acess variables without method")
    ba.print_public_owner_Name()
    ba.print_protected_balance()
    ba.print_private_pin()
    '''
'''
    sa  = SavingsAcount("Aishwarya",20000,12345,9.5)

    # access the attributes directy
    print("Acess variables without method")
    print(sa.owner)
    print(sa._balance)
    print(sa.__pin)
    # access the attributes using public method
    print("Acess variables with method")
    sa.print_public_owner_Name()
    sa.print_protected_balance()
    sa.print_private_pin()
'''


