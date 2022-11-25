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
            transaction += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item["amount"]


        return title + "\n" + transaction + "Total: " + str(total)
    
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded



def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10

    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)
    
    maxi = max(names, key = len)

    for x in range(len(maxi)):
        nameStr = "     "
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        
        if(x != len(maxi) - 1):
            nameStr += "\n"

        x_axis += nameStr
    
    res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis

    return res