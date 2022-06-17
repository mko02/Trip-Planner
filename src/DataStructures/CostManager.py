from Cost import *

'''
    Represent a cost manager (affiliated with a trip)
    that handles all the cost events including save, calculating,
    providing results access
'''

class CostManager:
    def __init__(self, list_of_members):                        #completed as of now
        """ Cost Manager constructor
            Create initial balance sheet with 0 balance
            Create initial empty transaction sheet 

        Parameters
        ----------

        list_of_members : Member[]
            list of initial members                             #What to do if added an additional member?

        Others
        ------
        balance_sheet : Dictionary of Dictionary
            Debtor maps to Payer maps to amount due
            Debtor A will get/give money from/to Payer B

            balance_sheet = {
                Debtor ID : Payer = {
                    Payer ID : amount due or owe
                    Payer ID : amount due or owe
                }
                Debtor ID : Payer = {
                    Payer ID : amount due or owe
                    Payer ID : amount due or owe
                }
            }

            xxx         Debtor 1    Debtor 2    Debtor 3    <- outer layer
            Payer 1         0       -amount A   +amount B
            Payer 2     +amount A        0      -amount C
            Payer 3     -amount B   +amount C        0
                ^ inner layer

            Debtor 2, Payer 1, negative amount: Person 2 pays xxx to    Person 1
            Debtor 1, Payer 2, positive amount: Person 1 gets xxx from Person 2
            
        transaction_sheet : Cost[]
            A record of all transaction (Cost events), used to calculate / update balance sheet

        Raises
        ------
        RuntimeError
            _description_
        """
    
        #raise RuntimeError("Not yet implemented")

        balance_sheet = {}

        for debtorID in list_of_members:
            
            payer_list = {}
            for payerID in list_of_members:
                payer_list[payerID] = 0

            balance_sheet[debtorID] = payer_list
    
        self.list_of_members = list_of_members
        self.balance_sheet = balance_sheet
        self.transaction_sheet = []

    '''
        Get the balance sheet to show interpersonal debt
    '''

    def getBalanceSheet(self):                                      #completed as of now
        """ Get the balance sheet to show interpersonal debt

        Returns
        -------
        Map of Map
            Returns the balance sheet

        Raises
        ------
        RuntimeError
            _description_
        """

        raise RuntimeError("Not yet implemented")

        return self.balance_sheet

    '''
        Get the transaction sheet to show all the previous
        cost events
    '''
    def getTransactionSheet(self):                                  #completed as of now
        """ Get the transaction sheet to show all the previous cost events

        Returns
        -------
        Cost[]
            Returns the transaction sheet

        Raises
        ------
        RuntimeError
            _description_
        """
        raise RuntimeError("Not yet implemented")
    
        return self.transaction_sheet

    '''
        Add a new cost event
    '''
    def addCost(self, new_cost):
        """ Record the new Cost event and adds to the transaction sheet

        Parameters
        ----------
        new_cost : Cost
            The new Cost event to be added

        Raises
        ------
        RuntimeError
            _description_
        """

        raise RuntimeError("Not yet implemented")

        self.transaction_sheet.append(new_cost)                             #use getter?
        
    '''
        Calculate results

        ------Additional Note------
        I am wondering if this can be involved in the getBalanceSheet
    '''
    def calculateResult(self):                                             #need testing
        """ Calculate the results using transaction sheet
            Updates the balance sheet

        Raises
        ------
        RuntimeError
            _description_
        """
        #raise RuntimeError("Not yet implemented")

        #Assuming calculateCost() returns 
        # [
        # Payer ID,
        # { Debtor1 ID : amount due,
        # Debtor2 ID : amount due,
        # Debtor3 ID : amount due, }
        # ]


        for cost_event in self.transaction_sheet:                           #use getter?
            calculated_cost = cost_event.calculateCost()
            payerID = calculated_cost[0]
            debtorDict = calculated_cost[1]

            # subtract from debtor and add to payer
            for debtorID in debtorDict:
                self.balance_sheet[debtorID][payerID] -= debtorDict[debtorID]   #use getter?
                self.balance_sheet[payerID][debtorID] += debtorDict[debtorID]

        




    '''
        Clear the balance sheet
    '''
    def clearBalance(self):                                     #completed as of now
        """ Clear the balance sheet by creating blank balance sheet

        Raises
        ------
        RuntimeError
            _description_
        """
        #raise RuntimeError("Not yet implemented")

        new_balance_sheet = {}

        for debtorID in self.list_of_members:                   #maybe make a getter for list_of_members?
            
            payer_list = {}
            for payerID in self.list_of_members:
                payer_list[payerID] = 0

            new_balance_sheet[debtorID] = payer_list

        self.balance_sheet = new_balance_sheet
        