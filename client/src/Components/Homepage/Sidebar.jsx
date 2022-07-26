import React from 'react'
import {Box} from '@mui/material'
import { ReactCalendar } from "./Calendar/ReactCalendar"

import {sample_trip} from "../DummyInfo/sample_trip"


function Sidebar() {
  return (
    <Box bgcolor="yellow" flex={0.5} padding={2}>
        Sidebar
         <ReactCalendar 
        //Dates to be highlighted
            tripDate = {sample_trip}
          />
    </Box>

  )
}

export default Sidebar