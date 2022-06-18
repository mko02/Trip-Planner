class Cost:
    """
    Represent a single cost event with two types of split
    Include details like tags, description, ... for this cost event
    """
    # expected_cost: a dict where (k, v) = (payer, amount they have to pay)
    expected_cost = {}
    # actual_cost: a tuple where (a, b) = (payer, amount he/she actually paid)
    actual_cost = ()
    payer_id = ""
    description = ""
    tag = ""

    def __init__(self, payer_id, actual_cost, expected_cost, description="", tag=""):
        """
        Construct a new cost per action with given parameters

        Parameters
        ----------
        payer_id : str
            The payer's ID of this cost event
        actual_cost : int
            The amount the payer paid
        expected_cost : dict
            A dict where (k, v) = (debtors' id, amount they have to pay)
        description : str
            The description of this cost (default: empty string)
        tag : str
            The tag of this cost (default: empty string)
        """
        self.payer_id = payer_id
        self.actual_cost = actual_cost
        self.expected_cost = expected_cost
        self.description = description
        self.tag = tag

    def get_payer(self):
        """
        Return the payer's id

        Returns
        -------
        str
            The payer's id
        """
        return self.payer_id

    def calculate_cost(self):
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
        for payee_id in self.expected_cost.keys():
            if payee_id != self.payer_id:
                result[payee_id] = self.expected_cost.get(payee_id)
        return result

    def get_tag(self):
        """
        Get the tage of this cost event

        Returns
        -------
        str
            The tag of this cost
        """
        return self.tag

    def set_tag(self, tag):
        """
        Set the tag of this cost event

        Parameters
        ----------
        tag : str
            The tag being set to this cost
        """
        self.tag = tag

    def get_description(self):
        """
        Get the description of this cost event

        Returns
        -------
        str
            The description of this cost event
        """
        return self.description

    def set_description(self, description):
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
        total = self.actual_cost
        payer = self.payer_id
        payees = ""
        for payee in self.expected_cost.keys():
            payees += "\t \t \t {payee} should pay {amount} \n".format(payee=payee,
                                                                       amount=self.expected_cost.get(payee))
        string = '''
        Total Cost: {total}
        Payer: {payer}, who paid {amount}
        Payees: \n {payees}
        Description: {description}
        Tag: {tag} \n'''.format(total=total, payer=payer, amount=total,
                                payees=payees, description=self.description, tag=self.tag)
        return string
