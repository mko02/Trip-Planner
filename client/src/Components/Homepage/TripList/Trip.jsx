import React from 'react'
import './Trip.css'
import {Box, Typography, IconButton} from '@mui/material'
import MoreVertIcon from '@mui/icons-material/MoreVert';

export default function Trip({ trip }) {
  return (
    <div className='trip'>
        <Box bgcolor='gray' borderRadius='6px'>
            <Typography className='pic'>Pic</Typography>
        </Box>
        <div className='trip_title_time'>
            <IconButton className='button'>
                <MoreVertIcon></MoreVertIcon>
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
