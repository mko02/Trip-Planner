import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from src.DataStructures.Trip import *
from src.DataStructures.Event import *
from src.DataStructures.Member import *

class testTrip:
    def createTrip(self):
        t1 = Trip()
        t2 = Trip()
        assert t1 != t2

    def getEventList(self):
        t1 = Trip()
        assert t1.getEventList() == {} #0
        t1.addEvent("e1", "1:00", "Jun. 24", "Meal", "Loc1", "None")
        eventList = {"e11:00Jun. 24" : Event("e1", "1:00", "Jun. 24", "Meal", "Loc1", "None")}
        assert t1.getEventList() == eventList #1
        t1.addEvent("e2", "2:00", "Jun. 24", "Walk", "Loc2", "None")
        eventList["e22:00Jun. 24"] = Event("e2", "2:00", "Jun. 24", "Walk", "Loc2", "None")
        assert t1.getEventList() == eventList #2
        # Report: Inconsistent number of parameters in addEvent()
        # Expected: 6, title, time, date, label, location, description
        # Actual: 5, time, date, label, location, description

    def getEvent(self):
        t1 = Trip()
        assert t1.getEvent("e11:00Jun. 24") == "QueryNotFound" #0
        t1.addEvent("e1", "1:00", "Jun. 24", "Meal", "Loc1", "None")
        e1 = Event("e1", "1:00", "Jun. 24", "Meal", "Loc1", "None")
        assert t1.getEvent("e11:00Jun. 24") == e1 #1
        t1.addEvent("e2", "2:00", "Jun. 24", "Walk", "Loc2", "None")
        e2 = Event("e2", "2:00", "Jun. 24", "Walk", "Loc2", "None")
        assert t1.getEvent("e22:00Jun. 24") == e2 #2

    def getMember(self):
        t1 = Trip()
        m1 = Member("m1", "red")
        m2 = Member("m2", "blue")
        assert t1.getMember("m1") == "QueryNotFound" #0
        t1.addMember("m1", "red")
        assert t1.getMember("m1") == m1 #1
        t1.addMember("m2", "blue")
        assert t1.getMember("m2") == m2 #2

    def getMemberList(self):
        t1 = Trip()
        m1 = Member("m1", "red")
        m2 = Member("m2", "blue")
        memberList = {}
        assert t1.getMemberList() == {}
        t1.addMember("m1", "red")
        memberList["m1"] = m1
        assert t1.getMemberList() == memberList
        t1.addMember("m2", "blue")
        memberList["m2"] = m2
        assert t1.getMemberList() == memberList

    def deleteEvent(self):
        t1 = Trip()
        eventList = {}
        t1.deleteEvent("e22:00Jun. 24")
        # Report:
        # Expected behavior:
        #   Do nothing when deleting a non-existing event
        #   Suggestion: catch the possible exceptions in the function
        t1.addEvent("e1", "1:00", "Jun. 24", "Meal", "Loc1", "None")
        t1.deleteEvent("e11:00Jun. 24")
        assert t1.getEventList() == {}
        t1.addEvent("e1", "1:00", "Jun. 24", "Meal", "Loc1", "None")
        t1.addEvent("e2", "2:00", "Jun. 24", "Walk", "Loc2", "None")
        eventList["e22:00Jun. 24"] = Event("e2", "2:00", "Jun. 24", "Walk", "Loc2", "None")
        t1.deleteEvent("e11:00Jun. 24")
        assert t1.getEventList() == eventList

    def deleteMember(self):
        t1 = Trip()
        memberList = {}
        t1.deleteMember("m1")
        # Report:
        # Expected behavior:
        #   Do nothing when deleting a non-existing member
        #   Suggestion: catch the possible exceptions in the function
        t1.addMember("m1", "red")
        t1.deleteMember("m1")
        assert t1.getMemberList() == {}
        t1.addMember("m1", "red")
        t1.addMember("m2", "blue")
        memberList["m2"] = Member("m2", "blue")
        t1.deleteMember("m1")
        assert t1.getMemberList() == memberList

def main():
    testTrip.createTrip()
    testTrip.getEvent()
    testTrip.getEventList()
    testTrip.deleteEvent()
    testTrip.getMember()
    testTrip.getMemberList()
    testTrip.deleteMember()

if __name__ == "__main__":
    main()
