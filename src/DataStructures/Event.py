from datetime import datetime

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
    label : str
        The label of this event
    location : str
        The location of this event
    description : str
        The description of this event
    """
    def __init__(self, title, start_time, end_time, label, location, description):
        """
        Construct a new Event with given parameters

        Parameters
        ----------
        title : str
        time : datetime.datetime
        label : str
        location : str
        description : str
        """
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.label = label
        self.location = location
        self.description = description

    def get_id(self):
        return self.title + self.start_time.strptime("%y, %m, %d, %H:%M")

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
