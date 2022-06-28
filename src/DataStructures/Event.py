'''
    Represent a mutable event with details such as name, description, date ...
    Allow manipulations on details
'''
class Event:

    def __init__(self, title, time, date, label, location, description):
        self.title = title
        self.time = time
        self.date = date
        self.label = label
        self.location = location
        self.description = description
        self.id = str(title) + str(time) + str(date)    
    '''
        Get id of this event
    '''

    def getID(self):
        return self.id

    '''
        Get time of this event
    '''
    def getTime(self):
        return self.time

    '''
        Get date of this event
    '''
    def getDate(self):
        return self.date

    '''
        Get the label of this event
    '''
    def getLabel(self):
        return self.label

    '''
        Get the location of this event
    '''
    def getLocation(self):
        return self.location

    '''
        Get the description of this event
    '''
    def getDescription(self):
        return self.description

    '''
        Set the time of this event
    '''
    def setTime(self, newTime):
        self.time = newTime

    '''
        Set the date of this event
    '''
    def setDate(self, newDate):
        self.date = newDate

    '''
        Set the label of this event
    '''
    def setLabel(self, newLabel):
        self.label = newLabel

    '''
        Set the location of this event
    '''
    def setLocation(self, newLocation):
        self.location = newLocation

    '''
        Set the description of this event
    '''
    def setDescription(self, newDescription):
        self.description = newDescription
