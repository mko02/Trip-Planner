import { Typography } from '@mui/material'
import React from 'react'
import Event from './Event'
import './EventList.css'

export default function EventList({ events }) {
    const firstEvent = events[0]
    const firstEventList = firstEvent.event
    const counter = 0
  
    return (
    //can implement event-grid css for auto-sizing
    <div> 
        
        <Typography className='event_title'>Events</Typography>
        <Typography className='trip_name'>{firstEvent.title}</Typography>

        <div className='event_grid'>
            {firstEventList.map((event, index) => {
                return (
                    <div>
                        <Event event={event} key={event.title} index={index+1} />      
                    </div>     
                )
                
            })}
        </div>
    </div>
  )
}
