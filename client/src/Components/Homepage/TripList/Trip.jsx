import React from 'react'
import './Trip.css'
import {Box, Typography, IconButton} from '@mui/material'
import MoreVertIcon from '@mui/icons-material/MoreVert';
import DropDown from './DropDown';

export default function Trip({ trip }) {
    const clickTrip = () => {
        console.log("trip clicked: " + trip.title);
    }
  return (
    <div className='trip' onClick={clickTrip}>
        <Box bgcolor='gray' borderRadius='6px'>
            <Typography className='pic'>Pic</Typography>
        </Box>
        <div className='trip_title_time'>
            <IconButton className='button'>
                <DropDown className='dropdown' icon={<MoreVertIcon/>}>
                    <p>Share</p>
                    <p>Delete</p>
                </DropDown>
            </IconButton>
            <div className='trip_title'>
                {trip.title}
            </div>
            <div className='trip_time_span'>
                {trip.time_span}
            </div>
            

        </div>
    </div>
  )
}
