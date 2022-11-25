class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            total += transaction.split(" ")[1]
        return total
    
    def transfer(self, amount, to):
        if self.check_funds(amount):
            transfer_to = "Transfer to " + to.name
            transfer_from = "Transfer from " + self.name
            self.ledger.withdraw(amount, transfer_to)
            to.deposit(amount, transfer_from)
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.get_balance < amount:
            return False
        else:
            return True
    
    # def __str__(self):
    #     pass
    




# def create_spend_chart(categories):