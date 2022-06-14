'''
    Represent a cost manager (affiliated with a trip)
    that handles all the cost events including save, calculating,
    providing results access
'''
class CostManager:
    def __init__(self, balance_sheet, transaction_sheet):
        """ Cost Manager constructor

        Args:
            balance_sheet ( Map of Map : Debtor maps to Payer maps to amount due ): _description_
            transaction_sheet ( Cost[] ): A list of cost objects saved

        Raises:
            RuntimeError: _description_
        """
        self.balance_sheet = balance_sheet
        self.transaction_sheet = transaction_sheet
        raise RuntimeError("Not yet implemented")

    '''
        Get the balance sheet to show interpersonal debt
    '''

    
    def getBalanceSheet(self):
        raise RuntimeError("Not yet implemented")
        return self.balance_sheet

    '''
        Get the transaction sheet to show all the previous
        cost events
    '''
    def getTransactionSheet(self):
        raise RuntimeError("Not yet implemented")
        return self.transaction_sheet

    '''
        Add a new cost event
    '''
    def addCost(self, new_cost):
        """ adds new Cost to the transaction sheet

        Args:
            new_cost (Cost Object): _description_

        Raises:
            RuntimeError: _description_
        """
        raise RuntimeError("Not yet implemented")
        self.transaction_sheet.append(new_cost)
        
    '''
        Calculate results

        ------Additional Note------
        I am wondering if this can be involved in the getBalanceSheet
    '''
    def calculateResult():
        raise RuntimeError("Not yet implemented")

    '''
        Clear the balance sheet
    '''
    def clearBalance():
        raise RuntimeError("Not yet implemented")
        