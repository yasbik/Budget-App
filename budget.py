import string

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
            total += transaction["amount"]
        return total
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            transfer_to = "Transfer to " + destination.name
            transfer_from = "Transfer from " + self.name
            self.withdraw(amount, transfer_to)
            destination.deposit(amount, transfer_from)
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True
    
    def __str__(self):
        num_stars = 30 - len(self.name)
        title = ""
        transaction = ""
        total = 0

        for i in range(num_stars//2):
            title += "*"
        title += self.name
        for i in range(num_stars//2):
            title += "*"
        
        for item in self.ledger:
            # transaction_description += str(item["description"]) + "\t"
            # transaction_amount += str(item["amount"]) + "\n"
            transaction += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item["amount"]


        return title + "\n" + transaction + "Total: " + str(total)
    




# def create_spend_chart(categories):