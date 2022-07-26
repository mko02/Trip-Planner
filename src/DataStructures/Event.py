from datetime import *

class Event:
    """
    Represent a Event instance

    Attributes
    ----------
    title : str
        The title of this event
    start_time : datetime.datetime
        The start time of this event
    end_time : datetime.datetime
        The end time of this event
    location : str
        The location of this event
    label : tuple
        A tuple of labels in this event
    description : str
        The description of this event
    """
    def __init__(self, title, start_time, end_time, location, label=(), description=""):
        """
        Construct a new Event with given parameters

        Parameters
        ----------
        title : str
        start_time : datetime.datetime
        end_time : datetime.datetime
        location : str
        label : tuple (str)
        description : str
        """
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.label = label
        self.description = description

    def get_id(self):
        return self.title + self.start_time.strftime("%Y, %M, %d, %H:%M")

    # Check representation exposure
    def get_start(self):
        return self.start_time

    def get_end(self):
        return self.end_time

    def get_label(self):
        return self.label

    def get_description(self):
        return self.description

    def get_title(self):
        return self.title

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __hash__(self):
        return self.get_id().__hash__()
