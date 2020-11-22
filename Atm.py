class atmcode:
    def __init__(self, bal): # constructor comes here!
        self.balance = bal  #account's balance
        self.pin = input("What is your four digit bank account pin?: ")
    def withdraw(self):
        wdraw = int(input("How much money would you like to withdraw?: "))
        if wdraw> self.balance:
            print("You don't have that much money, bye!")
        else:
            self.balance=self.balance-wdraw
            print("You have ",self.balance,"$'s in the account with the pin number ",self.pin,sep='')

account = atmcode(12000)
print(account.balance)
account.withdraw()

print("-------------------------------------")

acnt = atmcode(5000)
print(acnt.balance)
acnt.withdraw()
