class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self):
        d=int(input('Top up your balance: '))
        self.balance+=d
        print('current balance: '+str(self.balance))
    def withdraw(self):
        w=int(input('Enter the sum of withdraw: '))
        if self.balance>=w:
            self.balance-=w
            print('current balance: '+str(self.balance))
        else:
            print("Not accepted ")


owner=str(input('Name of the owner: '))
balance=int(input('Your balance is: '))
x=Account(owner,balance)
x.deposit()
x.withdraw()