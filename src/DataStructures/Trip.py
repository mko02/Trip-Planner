'''
    Represent a mutable trip with event manipulation, and a cost manager to
    handle all costs in this trip
'''
class Trip:
    def __init__():
        raise RuntimeError("Not yet implemented")

    '''
        Get the list of events that are currently in this trip
    '''
    def getEventList():
        raise RuntimeError("Not yet implemented")

    '''
        Get the list of members that are currently in this trip
    '''
    def getMemberList():
        raise RuntimeError("Not yet implemented")

    '''
        Get an event specifically by a tag
        Could be overloaded or just one kind of tag(e.g. name, ID, ...)
    '''
    def getEvent():
        raise RuntimeError("Not yet implemented")

    '''
        Get a member specifically by a name or ID
    '''
    def getMember():
        raise RuntimeError("Not yet implemented")

    '''
        Create a new event in this trip
    '''
    def addEvent():
        raise RuntimeError("Not yet implemented")

    '''
        Delete an existing event in this trip
    '''
    def deleteEvent():
        raise RuntimeError("Not yet implemented")

    '''
        Add a new member to this trip
    '''
    def addMember():
        raise RuntimeError("Not yet implemented")

    '''
        Delete a member in this trip
    '''
    def deleteMember():
        raise RuntimeError("Not yet implemented")


