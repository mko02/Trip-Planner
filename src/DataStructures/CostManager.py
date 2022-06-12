'''
    Represent a cost manager (affiliated with a trip)
    that handles all the cost events including save, calculating,
    providing results access
'''
class CostManager:
    def __init__(self):
        raise RuntimeError("Not yet implemented")

    '''
        Get the balance sheet to show interpersonal debt
    '''
    def getBalanceSheet():
        raise RuntimeError("Not yet implemented")

    '''
        Get the transaction sheet to show all the previous
        cost events
    '''
    def getTransactionSheet():
        raise RuntimeError("Not yet implemented")

    '''
        Add a new cost event
    '''
    def addCost():
        raise RuntimeError("Not yet implemented")

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
        