import React from 'react'
import Stack from 'react-bootstrap/Stack'

function EventList(props) {
    let events_jsx = []
    for (let e of props.events) {
        let time_obj = new Date(e.start_time)
        let date = time_obj.getDate() + " " + time_obj.toString().split(" ")[1]
        events_jsx.push(<Stack direction={"horizontal"} gap = {5}>
            <div className={"Date-title"}>{date}</div>
            <Stack>
                <div className={"Event-title"}>{e.title}</div>
                <div className={"Start-time-title"}>{time_obj.toString()}</div>
                <div className={"Description"}>{e.description}</div>
            </Stack>
        </Stack>)
    }

    return (
        <div>
            {events_jsx}
        </div>
    )
}

export default EventList