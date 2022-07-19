import React from 'react'
import {Box} from '@mui/material'
import { ReactCalendar } from "./Calendar/ReactCalendar"



function Sidebar() {
  return (
    <Box bgcolor="yellow" flex={0.5} padding={2}>
        Sidebar
         <ReactCalendar 
        //Dates to be highlighted
            tripDate = {[
            'Jul 15 2022',
            'Jul 16 2022',
            'Jul 19 2022']
          }
          />
    </Box>

  )
}

export default Sidebar