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
    def __init__(self):
        raise RuntimeError("Not yet implemented")
        ## hihi Esther is tryingggg
        ## Esther trying branch
        ## max
    '''
        Select the payer of this cost
    '''
    def selectPayer():
        raise RuntimeError("Not yet implemented")

    '''
        Select the payees of this cost
    '''
    def selectPayee():
        raise RuntimeError("Not yet implemented")

    '''
        Calculate the interpersonal debt relationship
    '''
    def calculateCost():
        raise RuntimeError("Not yet implemented")

    '''
        Save the custom split costs with parameters
    '''
    def saveCustomCost():
        raise RuntimeError("Not yet implemented")

    '''
        Save the evenly split costs with parameters
    '''
    def saveSplitCost():
        raise RuntimeError("Not yet implemented")

    '''
        Get the tag of this cost event
    '''
    def getTag():
        raise RuntimeError("Not yet implemented")

    '''
        Set the tag of this cost event
    '''
    def setTag():
        raise RuntimeError("Not yet implemented")

    '''
        Get the description of this cost event
    '''
    def getDescription():
        raise RuntimeError("Not yet implemented")

    '''
        Set the description of this cost event
    '''
    def setDescription():
        raise RuntimeError("Not yet implemented")