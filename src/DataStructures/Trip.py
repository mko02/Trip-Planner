'''
    Represent a mutable trip with event manipulation, and a cost manager to
    handle all costs in this trip
'''

from CostManager import *
from Event import *
from Member import *

class Trip:
    def __init__(self):
        self.events = {} #id: event_object
        self.members = {}  #name: member_object
        self.costManager = CostManager(self.members)
 

    '''
        Get the list of events that are currently in this trip
    '''
    def getEventList(self):
        return self.events
 

    '''
        Get the list of members that are currently in this trip
    '''
    def getMemberList(self):
        return self.members
 

    '''
        Get an event specifically by id
    '''
    def getEvent(self, queryId):
        event  = self.events.get(queryId, "QueryNotFound")
        if event == "QueryNotFound":
            return "QueryNotFound"
        else:
            return event

    '''
        Get a member specifically by a name or ID
    '''

    def getMember(self, queryName = None):
        member = self.members.get(queryName, "QueryNotFound")
        if member == "QueryNotFound":
            return "QueryNotFound"
        else:
            return member

    '''
        Create a new event in this trip
    '''
    def addEvent(self, add_time, add_date, add_label, add_location, add_description):
        newEvent=Event(add_time, add_date, add_label, add_location, add_description)
        self.events[newEvent.getID()] = newEvent

    '''
        Delete an existing event in this trip
    '''
    def deleteEvent(self, event_id):
        deleteEvent = self.events.pop(event_id)
        del deleteEvent


    '''
        Add a new member to this trip
    '''
    def addMember(self, name, color):
        newMember = Member(name,color)
        self.members[newMember.getName()] = newMember

    '''
        Delete a member in this trip
    '''
    def deleteMember(self, name):
        deleteMember = self.members.pop(name)
        del deleteMember


