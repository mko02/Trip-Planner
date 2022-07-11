class Cost:
    """
    Represent a mutable Cost event
    The amount of expected cost and total are immutable
    """
    def __init__(self, payer, total, expected_cost, title, description=None, tag=None):
        """
        Constructs a new Cost event

        Parameters
        ----------
        payer : Member
            The person who pays the total in this cost event
        total : float
            The total amount in this cost event
        expected_cost : dict
            (k, v) = (person, the amount he/she has to pay)
        title : str
            The title of this cost
        description : str
        tag : str
        """
        self.payer = payer
        self.total = total
        self.expected_cost = expected_cost
        self.title = title
        self.description = description
        self.tag = tag

    def get_payer(self):
        """
        Return the payer of the cost event

        Returns
        -------
        Member
            the payer of the cost event
        """
        return self.payer

    def get_total(self):
        """
        Return the total of the cost event

        Returns
        -------
        float
            the total of the cost event
        """
        return self.total

    def get_title(self):
        """
        Return the title of the cost event

        Returns
        -------
        str
            the title of the cost event
        """
        return self.title

    def get_description(self):
        """
        Return the description of the cost event

        Returns
        -------
        str
            the description of the cost event
        """
        return self.description

    def get_tag(self):
        """
        Return the tag of the cost event

        Returns
        -------
        str
            the tag of the cost event
        """
        return self.tag

    def calculate_debt(self):
        """
        Calculate the interpersonal debt relationship within this cost event

        Returns
        -------
        dict : (Member, float)
            (k, v) = (debtor, the amount they have to pay the payer)

        Examples
        --------
        expected_cost : {A : 20, B : 30, C : 50}
        payer : A

        The result would be {B : 30, C : 50} because A is the payer
        """
        result = {}
        for debtor in self.expected_cost.keys():
            if debtor != self.payer:
                result[debtor] = self.expected_cost[debtor]
        return result

    def set_title(self, title):
        """
        Set the title of this cost event

        Parameters
        ----------
        title : str
            the new title of this cost event
        """
        self.title = title

    def set_description(self, description):
        """
        Set the description of this cost event

        Parameters
        ----------
        description : str
            the new description of this cost event
        """
        self.description = description

    def set_tag(self, tag):
        """
        Set the tag of this cost event
        Parameters
        ----------
        tag : str
            the new tag of this cost event
        """
        self.tag = tag

    def __eq__(self, other):
        return self.payer == other.payer and self.total == other.total and self.title == other.title \
                and self.description == other.description and self.expected_cost == other.expected_cost

    def __hash__(self):
        return self.total
