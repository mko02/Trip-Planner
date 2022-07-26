import React, { useState } from 'react'
import {sample_trip} from "../DummyInfo/sample_trip"
import EventList from "../Components/TripPage/EventList"

function Trip(props) {
  // props: the whole package
  return (
    <div>
      <div className={"title"}>{props.trip.title}</div>
      <EventList events={props.trip.event}></EventList>
    </div>
  )
}

export default Trip