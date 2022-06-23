class Cost:
    """
    Represent a single cost event with two types of split
    Include details like tags, description, ... for this cost event
    """
    # expectedCost: a dict where (k, v) = (payer, amount they have to pay)
    expectedCost = {}
    actualCost = 0
    description = ""
    tag = ""

    def __init__(self, payer, actualCost, expectedCost, description="", tag=""):
        """
        Construct a new cost per action with given parameters

        Parameters
        ----------
        payer : Member
            The payer (Member Object) of this cost event
        actualCost : int
            The amount the payer paid
        expectedCost : dict
            A dict where (k, v) = (debtor (Member Object), amount they have to pay)
        description : str
            The description of this cost (default: empty string)
        tag : str
            The tag of this cost (default: empty string)
        """
        self.payer = payer
        self.actualCost = actualCost
        self.expectedCost = expectedCost
        self.description = description
        self.tag = tag

    def getPayer(self):
        """
        Return the payer (Member Object)

        Returns
        -------
        Member
            The payer of this cost event
        """
        return self.payer

    def calculateCost(self):
        """
        Calculate the interpersonal debt relationship
        Return it as a dict

        Returns
        -------
        dict
            (k, v) = (Every debtor in this cost, The amount they have to pay the payer)
            Amounts are kept positive
        """
        result = {}
        for debtor in self.expectedCost.keys():
            if debtor != self.payer:
                result[debtor] = self.expectedCost.get(debtor)
        return result

    def getTag(self):
        """
        Get the tage of this cost event

        Returns
        -------
        str
            The tag of this cost
        """
        return self.tag

    def setTag(self, tag):
        """
        Set the tag of this cost event

        Parameters
        ----------
        tag : str
            The tag being set to this cost
        """
        self.tag = tag

    def getDescription(self):
        """
        Get the description of this cost event

        Returns
        -------
        str
            The description of this cost event
        """
        return self.description

    def setDescription(self, description):
        """
        Set the description of this cost event

        Parameters
        ----------
        description : str
            The description being set to this cost event
        """
        self.description = description

    def __str__(self):
        """
        Return the details of this cost event as a string

        Returns
        -------
        str
            The details of this cost event
        """
        total = self.actualCost
        payer = self.payer
        payees = ""
        for payee in self.expectedCost.keys():
            payees += "\t \t \t {payee} should pay {amount} \n".format(payee=payee.getName(),
                                                                       amount=self.expectedCost.get(payee))
        string = '''
        Total Cost: {total}
        Payer: {payer}, who paid {amount}
        Payees: \n {payees}
        Description: {description}
        Tag: {tag} \n'''.format(total=total, payer=payer.getName(), amount=total,
                                payees=payees, description=self.description, tag=self.tag)
        return string
