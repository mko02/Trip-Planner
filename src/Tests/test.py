import random

class Trip:

    def __init__(self):
        self.event_list = []
        self.member_IDs = []
        self.cost_manager = CostManager()
    
class CostManager:

    def __init__(self):
        self.balance_sheet = [[]]
        self.transaction_sheet = []
    
    def getBalancesSheet(self):
        return self.balance_sheet

    def getTransactionSheet(self):
        return self.transaction_sheet

    def addCost(self, new_cost):
        self.transaction_sheet.append(new_cost)

    def calculateResult(self):
        None
    

class Member:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.ID = random.randint(10)
        self.balance = 0

    def add_to_balance(self, add_value):
        self.balance += add_value

    def subtract_from_balance(self, sub_value):
        self.balance -= sub_value


