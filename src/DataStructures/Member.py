class Member:
    """
    Represent a Member with name, color, and balance

    Attributes
    ----------
    name : str
        The name of this member
    color : str
        The color of this member
    balance : float
        The current balance of this member
    """
    def __init__(self, name, color):
        """
        Construct an instance of Member

        Parameters
        ----------
        name : str
        color : str
        """
        self.name = name
        self.color = color
        self.balance = 0.0

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_balance(self):
        return self.balance

    def set_color(self, color):
        """
        Set the color of this member with a given color

        Parameters
        ----------
        color : str
            The new color set to this member
        """
        self.color = color

    def set_balance(self, balance):
        """
        Set the balance of this member with a given balance

        Parameters
        ----------
        balance : float
            The new balance set to this member
        """
        self.balance = balance

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()