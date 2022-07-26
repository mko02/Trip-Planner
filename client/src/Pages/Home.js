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
    
  )
}

export default Home