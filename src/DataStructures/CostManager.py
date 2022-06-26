from Cost import *
from Member import *

'''
    Represent a cost manager (affiliated with a trip)
    that handles all the cost events including save, calculating,
    providing results access
'''

class CostManager:
    def __init__(self, listOfMembers):                        #completed as of now
        """ Cost Manager constructor
            Create initial balance sheet with 0 balance
            Create initial empty transaction sheet 

        Parameters
        ----------

        listOfMembers : {name : Member Object}
            dictionary of initial members                            

        Others
        ------
        balanceSheet : Dictionary of Dictionary
            Debtor(name) maps to Payer(name) maps to amount due
            Debtor A will get/give money from/to Payer B

            balanceSheet = {
                Debtor : Payer = {
                    Payer : amount due or owe
                    Payer : amount due or owe
                }
                Debtor : Payer = {
                    Payer : amount due or owe
                    Payer : amount due or owe
                }
            }

            xxx         Debtor 1    Debtor 2    Debtor 3    <- outer layer
            Payer 1         0       -amount A   +amount B
            Payer 2     +amount A        0      -amount C
            Payer 3     -amount B   +amount C        0
                ^ inner layer

            Debtor 2, Payer 1, negative amount: Person 2 pays xxx to    Person 1
            Debtor 1, Payer 2, positive amount: Person 1 gets xxx from Person 2
            
            
        transactionSheet : Cost[]
            A record of all transaction (Cost events), used to calculate / update balance sheet

        """

        balanceSheet = {}

        for debtorName in listOfMembers:                            
            
            payerList = {}
            for payerName in listOfMembers:
                payerList[payerName] = 0

            balanceSheet[debtorName] = payerList
    
        self.listOfMembers = listOfMembers
        self.balanceSheet = balanceSheet
        self.transactionSheet = []

    def getBalanceSheet(self):                                      #completed as of now
        """ Get the balance sheet to show interpersonal debt

        Returns
        -------
        Map of Map
            Returns the balance sheet

        """

        return self.balanceSheet

    def getTransactionSheet(self):                                  #completed as of now
        """ Get the transaction sheet to show all the previous cost events

        Returns
        -------
        Cost[]
            Returns the transaction sheet

        """    

        return self.transactionSheet

    def addMember(self, newMember):                                 #completed as of now
        """ Update balance sheet and list of members when new member is added to Trip

        Parameters
        ----------
        newMember : Member Object
            New member to add into balance sheet and list of member
        """
        
        newMemberName = newMember.getName()
        self.listOfMembers[newMemberName] = newMember

        #add new member as payer for each original debtor
        for debtorName in self.balanceSheet:
            payerList = self.balanceSheet[debtorName]
            payerList[newMemberName] = 0

        #create dict: new member as debtor with each original payer
        newMemberPayerList = {}
        for name in self.listOfMembers:
            newMemberPayerList[name] = 0

        #update balanceSheet and listOfMembers
        self.balanceSheet[newMemberName] = newMemberPayerList


    def deleteMember(self, unwantedMember):                         #incomplete
        None

    def addCost(self, newCost):                                        #completed as of now
        """ Record the new Cost event and adds to the transaction sheet

        Parameters
        ----------
        new_cost : Cost
            The new Cost event to be added

        """

        self.transactionSheet.append(newCost)

    def deleteCost(self, unwantedCost):                             #completed as of now
        """ Delete Cost event from transaction sheet

        Parameters
        ----------
        unwantedCost : Cost
            Cost event to be deleted
        """

        self.transactionSheet.remove(unwantedCost)
        
    '''
        Calculate results

        ------Additional Note------
        I am wondering if this can be involved in the getBalanceSheet
    '''
    def calculateResult(self):                                             #completed as of now
        """ Calculate the results using transaction sheet
            Updates the balance sheet

            Subtract from debtor -> payer balance value
            Add to payer -> debtor balance value

        """

        #Clear balance first to recalculate
        self.clearBalance()

        for costEvent in self.transactionSheet:
            payerName = costEvent.getPayer()
            calculated_cost = costEvent.calculateCost()

            # subtract from debtor and add to payer
            for debtorName in calculated_cost:
                self.balanceSheet[debtorName][payerName] -= calculated_cost[debtorName]
                self.balanceSheet[payerName][debtorName] += calculated_cost[debtorName]

    def clearBalance(self):                                     #completed as of now
        """ Clear the balance sheet by creating blank balance sheet

        """

        newBalanceSheet = {}

        for debtorName in self.listOfMembers:
            
            payerList = {}
            for payerName in self.listOfMembers:
                payerList[payerName] = 0

            newBalanceSheet[debtorName] = payerList

        self.balanceSheet = newBalanceSheet
        
    def printBalance(self):                                 #completed as of now
        """ Print out balance sheet
            For testing and visual purposes

        """
        debtorAxis = "xxx\t"

        for debtorName in self.balanceSheet:
            debtorAxis += f"{debtorName}\t"

        print(debtorAxis)

        for debtorName in self.balanceSheet:
            payerAmountDict = self.balanceSheet[debtorName]        
            payerAxis = debtorName + "\t"
            for payerName in payerAmountDict:
                amount = payerAmountDict[payerName]
                payerAxis += f"{amount}\t"

            print(payerAxis)


