import React, {useState} from 'react'
import {Box} from '@mui/material'
import { ReactCalendar } from "./Calendar/ReactCalendar"
import EventList from './EventList/EventList'


import {sample_trip} from '../../DummyInfo/sample_trip'
import {sample_package_data} from '../../DummyInfo/sample_package_data'


function Sidebar() {
  const [events] = useState(sample_package_data)

  return (
    <Box bgcolor="#EEEEEE" flex={1} padding={2}>
        
        <ReactCalendar tripDate = {sample_trip} />

        <EventList events={events} />
          
    </Box>

  )
}

export default Sidebar