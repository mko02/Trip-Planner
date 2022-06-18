'''
    Represent a member with name and distinct ID
'''
class Member:
    def __init__(self, id, name, balance, color):
        self.id = id 
        self.name = name
        self.balance  = balance
        self.color = color
        raise RuntimeError("Not yet implemented")

    '''
        Get the ID of this member
    '''
    def getID(self):
        return self.id
        raise RuntimeError("Not yet implemented")

    '''
        Get the name of this member
    '''
    def getName(self):
        return self.name
        raise RuntimeError("Not yet implemented")

    '''
        Get the balance of this member
    '''
    def getBalance(self):
        return self.balance
        raise RuntimeError("Not yet implemented")

    '''
        Get the distince color of this member
    '''
    def getColor(self):
        return self.color
        raise RuntimeError("Not yet implemented")

    '''
        Set the balance of this member
    '''
    def setBalance(self, newBalance):
        self.balance = newBalance
        raise RuntimeError("Not yet implemented")

    '''
        Set the name of this member
    '''
    def setName(self,newName):
        self.name = newName
        raise RuntimeError("Not yet implemented")

    '''
        Set the color of this member
    '''
    def setColor(self, newColor):
        self.color = newColor
        raise RuntimeError("Not yet implemented")

