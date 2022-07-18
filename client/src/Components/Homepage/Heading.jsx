import React from 'react'
import { Link } from "react-router-dom";

import {Box, Stack, Typography, Button, IconButton} from '@mui/material'
import AddIcon from '@mui/icons-material/Add';

function Heading() {
  return (
    <Box bgcolor="white" padding={2}>
        <Stack direction="row" justifyContent="space-between" spacing={2}>
            <Typography>MY TRIPS</Typography>
            {/* <IconButton component={Link} to="/addtrip"> */}
            <IconButton component={Link} to="/addtrip">
                <AddIcon></AddIcon>
            </IconButton>
        </Stack>
       
    </Box>
  )
}

export default Heading