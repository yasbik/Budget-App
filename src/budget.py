class Category:

    # initialize the class with a category name and a ledger
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    


    # method to diposit an amount with an optional description
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})



    # method to withdraw an amount with an optional description
    def withdraw(self, amount, description = ""):

        # check if there is enough money in the account for withdrawal
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        # not enough money
        else:
            return False



    # get the current balance of the account
    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            total += transaction["amount"]
        return total
    


    # transfer balance from one category to another
    def transfer(self, amount, destination):

        # check if there is enough balance for transfer
        if self.check_funds(amount):
            transfer_to = "Transfer to " + destination.name
            transfer_from = "Transfer from " + self.name

            # withdraw from one category and deposit into another
            self.withdraw(amount, transfer_to)
            destination.deposit(amount, transfer_from)
            return True
        # not enough balane for transfer
        else:
            return False
    


    # method to check if there is enough fund (for withdrawal)l
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True
    


    # string method to print the ledger
    def __str__(self):
        
        # create the category title centered among 30 spaces with stars on both sides
        num_stars = 30 - len(self.name)
        title = ""
        for i in range(num_stars//2):
            title += "*"
        title += self.name
        for i in range(num_stars//2):
            title += "*"
        
        transaction = ""
        total = 0

        # format the amount and descriptions for each transaction
        for item in self.ledger:
            transaction += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            # calculate the total amount
            total += item["amount"]

        return title + "\n" + transaction + "Total: " + str(total)
    


    # method to extract all withdrawals from the ledger
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total



# function to shorten duration
def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier



# function to get the total withdrawal amount for each category
def getTotals(categories):
    total = 0
    breakdown = []

    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())

    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded



# function to print the bar graph
def create_spend_chart(categories):

    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)

    # concatenate the spaces
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10

    # dashed lines for the x-axis
    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""

    # get the category names
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