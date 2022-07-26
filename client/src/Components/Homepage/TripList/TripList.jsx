import React from 'react'
import Trip from './Trip'
import './TripList.css'

export default function TripList({ trips }) {
  return (
    <div className='trip_grid'>
        {trips.map(trip => {
            return (
                <Trip trip={trip} key={trip.title}/>
            )
        })}
    </div>
  )
}
