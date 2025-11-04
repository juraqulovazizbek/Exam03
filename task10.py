class BankAccount:

    def __init__(self ,name , balance ):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} ning hisobiga {amount} ming pul qo'shildi. hozirgi balans: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Yetarli mablag' yo'q.")
        else:
            self.balance -= amount
            print(f"{self.name} ning hisobidan {amount} ming pul yechib olindi. hozirgi balans: {self.balance}")
account = BankAccount("Ali Aliyev", 1000)
account.deposit(500)
account.withdraw(200)