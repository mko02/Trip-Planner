'''
    Represent a mutable event with details such as name, description, date ...
    Allow manipulations on details
'''
class Event:
    def __init__(self, time, date, label, location, description):
        self.time = time
        self.date = date
        self.label = label
        self.location = location
        self.description = description
        raise RuntimeError("Not yet implemented")

    '''
        Get time of this event
    '''
    def getTime():
        raise RuntimeError("Not yet implimented")

    '''
        Get date of this event
    '''
    def getDate():
        raise RuntimeError("Not yet implemented")

    '''
        Get the label of this event
    '''
    def getLabel():
        raise RuntimeError("Not yet implemented")

    '''
        Get the location of this event
    '''
    def getLocation():
        raise RuntimeError("Not yet implemented")

    '''
        Get the description of this event
    '''
    def getDescription():
        raise RuntimeError("Not yet implemented")

    '''
        Set the time of this event
    '''
    def setTime():
        raise RuntimeError("Not yet implemented")

    '''
        Set the date of this event
    '''
    def setDate():
        raise RuntimeError("Not yet implemented")

    '''
        Set the label of this event
    '''
    def setLabel():
        raise RuntimeError("Not yet implemented")

    '''
        Set the location of this event
    '''
    def setLocation():
        raise RuntimeError("Not yet implemented")

    '''
        Set the description of this event
    '''
    def setDescription():
        raise RuntimeError("Not yet implemented")