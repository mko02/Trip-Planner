import React from 'react'
import Heading from './Heading'
import {Box} from '@mui/material'
import TripList from '../TripList';

function Main() {
  return (
    <Box bgcolor="skyblue" padding={2} flex={2}>
      <Heading/>
      <TripList/>
    </Box>
  )
}

export default Main


const SAMPLE_TRIP = [
  
]