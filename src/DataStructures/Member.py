'''
    Represent a member with name and distinct ID
'''
class Member:
    def __init__(self, name, color):
        self.name = name #notmutable
        self.balance  = 0
        self.color = color

    '''
        Get the name of this member
    '''
    def getName(self):
        return self.name

    '''
        Get the balance of this member
    '''
    def getBalance(self):
        return self.balance

    '''
        Get the distinct color of this member
    '''
    def getColor(self):
        return self.color

    '''
        Set the balance of this member
    '''
    def setBalance(self, newBalance):
        self.balance = newBalance

    '''
        Set the name of this member
    '''
    def setName(self,newName):
        self.name = newName

    '''
        Set the color of this member
    '''
    def setColor(self, newColor):
        self.color = newColor

