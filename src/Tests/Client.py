from src.DataStructures import Trip, Event
## After implementation, we could fill in additional parameters
def main():
    trip = Trip()
    trip.addMember()
    trip.addEvent()
    trip.addEvent()
    event = trip.getEvent()
    ## getEvent not yet implemented so event manipulation is not allowed yet
    # event.getTime()....

    ## Cost manager manipulation is to be decided



if __name__ == "__main__":
    main()