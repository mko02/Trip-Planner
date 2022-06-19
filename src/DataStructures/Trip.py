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

    def getMember(self, queryname = None, queryid = None):
        self.memberids
        for member in self.memberids:
            if member.id == queryid or member.name == queryname: ## 大小寫有差嗎？
                return member
            #not sure if i should import member class 
            # can they search by both query?
            # if yes, what if queryname does not match queryid 
            # raise error of member not found?
            
            ## Esther's Ideas: 
            ## not sure how member.id and member.name works cuz I was thinking of memberids as a list of IDs 
            ## if we have a dictionary of id <-> member_object

            ## for id in self.memberids: 
            ##     name = queryid.get(queryid).getName()
            ##     if id == queryid and name == queryname: 
            ##          return queryid.get(queryid) ## returns a member object instead of his/ her ID 
            ##     elif (id == queryid and name != queryname) or (id != queryid and name == queryname): 
            ##          raise ??Error() 

    '''
        Create a new event in this trip
    '''
    def addEvent(self, add_time, add_date, add_label, add_location, add_description):
        self.events.append((Event(add_time, add_date, add_label, add_location, add_description)))
        #do we need an event id?  -- unresolved 

        ## oki i think we need event id in order to delete 
        ## so prob also a dictionary of id <-> event object
        ## new_event = Event(add_time, add_date, add_label, add_location, add_description)
        ## self.events.append(new_event.getID())
    '''
        Delete an existing event in this trip
    '''
    def deleteEvent(self, event_id):
        self.events.remove(event_id)
        ## do we care about this being slow? 
        ## what if we relate id to its index in the list 
        raise RuntimeError("Not yet implemented")

    '''
        Add a new member to this trip
    '''
    def addMember(self, name, balance, color):
        id = len(self.memberids) ## assuming ID for 1st member is 0, for 2nd is 1, and so on 
        new_member = Member(id, name, balance, color)
        self.memberids.append(id)       
        raise RuntimeError("Not yet implemented")

    '''
        Delete a member in this trip
    '''
    def deleteMember(self, id):
        self.memberids.remove(id)
        raise RuntimeError("Not yet implemented")


