from datetime import datetime as dt
from Event import Event
from Member import Member


class Trip:
    """
    Represent a Trip containing mutable events and immutable members

    Attributes
    ----------
    events : dict
        (k, v) = (ID of the event, Event object)
    members : dict
        (k, v) = (name of the member, Member object)
    """
    def __init__(self):
        self.events = {}
        self.members = {}

    def get_event_list(self):
        """
        Return an immutable list of events in this trip

        Returns
        -------
        tuple
            The events in this trip
        """
        return tuple(self.events.values())

    def get_member_list(self):
        """
        Return an immutable list of members in this trip

        Returns
        -------
        tuple
            The members in this trip
        """
        return tuple(self.members.values())

    def get_event(self, ID):
        """
        Return the event with the given ID

        Parameters
        ----------
        ID : str
            The ID of the target event

        Returns
        -------
        Event
            The target event

        Warnings
        --------
        Make sure the ID exists in this trip using .contains_event()
        """
        return self.events[ID]

    def get_member(self, name):
        """
        Return the member with the given name

        Parameters
        ----------
        name : str
            The name of the target member

        Returns
        -------
        Member
            The target member

        Warnings
        --------
        Make sure the name exists in this trip using .contains_member()
        """
        return self.members[name]

    def contains_event(self, ID):
        """
        Check if the given ID is an event in this event

        Parameters
        ----------
        ID : str
            The ID of the event checked

        Returns
        -------
        bool
            true if the event exists, false otherwise
        """
        return ID in self.events.keys()

    def contains_member(self, name):
        """
        Check if the given name is a member in this event

        Parameters
        ----------
        name : str
            The name of the member checked

        Returns
        -------
        bool
            true if the member exists, false otherwise
        """
        return name in self.members.keys()

    def add_event(self, title, year, month, date, hour, minute, label, location, description):
        """
        Add a new event with given parameters
        If duplicate event exists in the trip, then no behavior is performed

        Parameters
        ----------
        title : str
        year : int
        month : int
        date : int
        hour : int
        minute : int
        label : str
        location : str
        description : str
        """
        time = dt(year, month, date, hour, minute)
        e = Event(title, time, label, location, description)
        if not self.contains_event(e.get_id()):
            self.events[e.get_id()] = e

    def delete_event(self, ID):
        """
        Delete an event in this trip with given ID
        If no such event exists, no behavior is performed

        Parameters
        ----------
        ID : str
            The ID of the target event to be deleted
        """
        if self.contains_event(ID):
            self.events.pop(ID)

    def add_member(self, name, color):
        """
        Add a new member to this trip
        No behavior if the name exists in this trip

        Parameters
        ----------
        name : str
        color : str
        """
        if not self.contains_member(name):
            self.members[name] = Member(name, color)

    def delete_member(self, name):
        """
        Delete an existing member in this trip
        No behavior if the name does not exist in this trip

        Parameters
        ----------
        name : str
        """
        if self.contains_member(name):
            self.members.pop(name)