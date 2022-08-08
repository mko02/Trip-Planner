import React from 'react'
import './Trip.css'
import {Box, Typography, IconButton} from '@mui/material'
import MoreVertIcon from '@mui/icons-material/MoreVert';
import DropDown from './DropDown';
import DropDownMenu from './DropDownMenu';

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
            <div className='trip_title'>
                {trip.title}
            </div>
            <div className='trip_time_span'>
                {trip.time_span}
            </div>
        </div>
        <div className='dropdown'>
            <DropDown icon={<MoreVertIcon className='threeDots'/>}>
                <div className='dropDownMenu'>
                    <DropDownMenu></DropDownMenu>
                </div>
            </DropDown>
        </div>
    </div>
  )
}
