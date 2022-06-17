class Cost:
    """
    Represent a single cost event with two types of split
        1. Custom split with customized individual cost
        2. Evenly split with a total cost and number of payees
    Include details like tags, description, ... for this cost event
    """
    # __expected_cost: a dict where (k, v) = (payer, amount they have to pay)
    __expected_cost = {}
    # __actual_cost: a tuple where (a, b) = (payer, amount he/she actually paid)
    __actual_cost = ()
    # "Evenly Split" or "Custom Split"
    __payment_method = ""
    __description = ""
    __tag = ""

    def __init__(self, payment_method, actual_cost, expected_cost, description="", tag=""):
        """
        Construct a new cost per action

        Parameters
        ----------
        payment_method : str
            The payment method in a string of "Evenly Split" or "Custom Split"
        actual_cost : tuple
            A tuple where (elt_0, elt_1) = (payer, amount the payer paid)
        expected_cost : dict
            A dict where (k, v) = (payer, amount they have to pay)
        description : str
            The description of this cost (default: empty string)
        tag : str
            The tag of this cost (default: empty string)
        """
        self.__payment_method = payment_method
        self.__actual_cost = actual_cost
        self.__expected_cost = expected_cost
        self.__description = description
        self.__tag = tag

    def calculate_cost(self):
        """
        Calculate the interpersonal debt relationship
        Return it as a dict

        Returns
        -------
        dict
            Represented as (k, v) = (Every payee in this cost, Another dict_2)
            dict_2 represents (k, v) = (Every person that the payee owes money,
                The amount he/she owes the person(k))
            Example:
                {A : {B : 200, C : 200}, B : {C : 100}}
                A has to pay B 200 dollars, and C 200 dollars
                B has to pay C 100 dollars
        """
        result = {}
        payer = self.__actual_cost[0]
        for payee in self.__expected_cost.keys():
            if payee != payer:
                result[payee] = {payer: self.__expected_cost.get(payee)}
        return result

    def get_tag(self):
        """
        Get the tage of this cost event

        Returns
        -------
        str
            The tag of this cost
        """
        return self.__tag

    def set_tag(self, tag):
        """
        Set the tag of this cost event

        Parameters
        ----------
        tag : str
            The tag being set to this cost
        """
        self.__tag = tag

    def get_description(self):
        """
        Get the description of this cost event

        Returns
        -------
        str
            The description of this cost event
        """
        return self.__description

    def set_description(self, description):
        """
        Set the description of this cost event

        Parameters
        ----------
        description : str
            The description being set to this cost event
        """
        self.__description = description

    def __str__(self):
        """
        Return the details of this cost event as a string

        Returns
        -------
        str
            The details of this cost event
        """
        if self.__payment_method:
            method = "Evenly Split"
        else:
            method = "Custom Split"
        total = self.__actual_cost[1]
        payer = self.__actual_cost[0]
        payees = ""
        for payee in self.__expected_cost.keys():
            payees += "\t \t \t {payee} should pay {amount} \n".format(payee=payee,
                                                                       amount=self.__expected_cost.get(payee))
        string = '''
        Payment Method: {method}
        Total Cost: {total}
        Payer: {payer}, who paid {amount}
        Payees: \n {payees}
        Description: {description}
        Tag: {tag} \n'''.format(method=method, total=total, payer=payer, amount=total,
                                payees=payees, description=self.__description, tag=self.__tag)
        return string
