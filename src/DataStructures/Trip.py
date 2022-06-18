'''
    Represent a mutable trip with event manipulation, and a cost manager to
    handle all costs in this trip
'''
from CostManager import * 
from Event import *
from Member import * 

class Trip:
    def __init__(self, events, memberids, costmanager):
        self.events = [] #empty list of events, in which we will append event object later 
        self.memberids = []
        self.costmanager = CostManager(self.memberids)
        raise RuntimeError("Not yet implemented")

    '''
        Get the list of events that are currently in this trip
    '''
    def getEventList(self):
        return self.events
        raise RuntimeError("Not yet implemented")

    '''
        Get the list of members that are currently in this trip
    '''
    def getMemberList(self):
        return self.memberids
        raise RuntimeError("Not yet implemented")

    '''
        Get an event specifically by a tag
        Could be overloaded or just one kind of tag(e.g. name, ID, ...)
    '''
    def getEvent(self):
        raise RuntimeError("Not yet implemented")

    '''
        Get a member specifically by a name or ID
    '''
    def getMember(self, queryname=None, queryid = None):
        self.memberids
        for member in self.memberids:
            if member.id == queryid or member.name == queryname:
                return member
             #not sure if i should import member class 
             # can they search by both query?
             # if yes, what if queryname does not match queryid 
             # raise error of member not found?
        raise RuntimeError("Not yet implemented")

    '''
        Create a new event in this trip
    '''
    def addEvent(self, add_time, add_date, add_label, add_location, add_description):
        self.events.append((Event(add_time, add_date, add_label, add_location, add_description)))
        #do we need an event id?  -- unresolved 
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


