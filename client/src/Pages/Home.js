import React from 'react'
import MainDisplay from "../Components/Homepage/MainDisplay"
import Sidebar from '../Components/Homepage/Sidebar.jsx'
import { ReactCalendar } from "../Components/Homepage/Calendar/ReactCalendar.js"
import {Box, Stack } from '@mui/material'

function Home() {
  return (
    <Box>
      <Stack direction="row" justifyContent="space-between" spacing={2}>
        <MainDisplay/>
        <Sidebar/>
      </Stack>
    </Box>
    // <><div>Home</div><div>
    //   <ReactCalendar 
    //     //Dates to be highlighted
    //     tripDate = {[
    //       'Jul 15 2022',
    //       'Jul 16 2022',
    //       'Jul 19 2022']
    //     }
    //   />
    // </div></>
  )
}

export default Home