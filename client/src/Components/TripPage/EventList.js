import React from 'react'
import Stack from 'react-bootstrap/Stack'
import {Box, Typography} from '@mui/material'
import "./EventList.css"

function EventList(props) {
    // props.title -> the title of the trip
    // Retrieve data from the backend
    let events_jsx = []
    for (let e of props.events) {
        let time_obj = new Date(e.start_time)
        events_jsx.push(
            <div className={"event"}>
                <Box bgcolor={"gray"} borderRadius={'6px'} className={"time-title"}>
                    <div className={"date-title"}>{time_obj.getDate()}</div>
                    <div className={"month-title"}>{time_obj.toString().split(" ")[1]}</div>
                </Box>
                <div className={"event-info"}>
                    <div className={"event-title"}>{e.title}</div>
                    <div className={"start-time-title"}>{time_obj.toString().substring(0, 34)}</div>
                    <div className={"description"}>{e.description}</div>
                </div>
            </div>
        )
    }

    return (
        <div className={"event-list"}>
            {events_jsx}
        </div>
    )
}

export default EventList