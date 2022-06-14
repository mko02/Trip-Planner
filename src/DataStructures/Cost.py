'''
    Represent a single cost event with two types of split
        1. Custom split with customized individual cost
        2. Evenly split with a total cost and number of payees
    Include details like tags, description, ... for this cost event

    ------Additional Note------
    Originally, I was thinking prompting the user's input inside the save
    costs methods. However, this way would incorrectly involve controller(user
    interaction). Instead, maybe try save the costs with a parameter of all the
    costs information that would be given by the controller.
'''
class Cost:
    ## __expectedCost: a dictionary where (k, v) = (payer, amount they have to pay)
    __expectedCost = {}
    ## __actualCost: a tuple where (a, b) = (payer, amount he/she actually paid)
    __actualCost = ()
    ## True: paid by evenly split cost
    ## False: paid by custom split cost
    __paymentMethod = True
    __description = ""
    __tag = ""

    '''
        Construct a new cost per action


    '''
    def __init__(self, paymentMethod, actualCost, expectedCost, description="", tag=""):
        self.__paymentMethod = paymentMethod
        self.__actualCost = actualCost
        self.__expectedCost = expectedCost


    '''
        Calculate the interpersonal debt relationship
    '''
    def calculateCost(self):
        result = {}
        payer = self.__actualCost[0]
        for payee in self.__expectedCost.keys():
            if (payee != payer):
                result[payee] = {payer : self.__expectedCost.get(payee)}
        return result

    '''
        Get the tag of this cost event
    '''
    def getTag(self):
        return self.__tag

    '''
        Set the tag of this cost event
    '''
    def setTag(self, tag):
        self.__tag = tag

    '''
        Get the description of this cost event
    '''
    def getDescription(self):
        return self.__description

    '''
        Set the description of this cost event
    '''
    def setDescription(self, description):
        self.__description = description

    '''
        Return the details of the cost in string
    '''
    def __str__(self):
        method = ""
        if self.__paymentMethod:
            method = "Evenly Split"
        else:
            method = "Custom Split"
        total = self.__actualCost[1]
        payer = self.__actualCost[0]
        payees = ""
        for payee in self.__expectedCost.keys():
            if (payee != payer):
                payees += "\t {payee} should pay {amount} \n".format(payee=payee,
                    amount=self.__expectedCost.get(payee))
        string = '''Payment Method: {method} \n
            Total Cost: {total} \n
            Payer: {payer}, who paid {amount} \n
            Payees: \n {payees} \n
            Description: {description} \n
            Tag: {tag} \n'''.forma(method=method, total=total, payer=payer, amount=total,
                payees=payees, description=self.__description, tag=self.__tag)
        return string
