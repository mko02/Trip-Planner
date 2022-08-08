import React, { useState } from "react";
import { Link } from "react-router-dom";
import NewTripModal from "./Modal/NewTripModal";

import { Box, Stack, Typography, Button, IconButton } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

function Heading() {
  const [open, setOpen] = useState(false);

  const addTrip = () => {
    console.log("click, addTrip action!");
    setOpen(true);
  };

  const modalClose = (e) => {
    e.stopPropagation();
    setOpen(false);
  }; //e = event
  //prevent dubbed bubbling
  //Modal to be close at default

  return (
    <Box bgcolor="white" padding={4}>
      <Stack direction="row" justifyContent="space-between" spacing={2}>
        <Typography fontSize={25}>MY TRIPS</Typography>
        {/* <IconButton component={Link} to="/addtrip"> */}
        <IconButton onClick={addTrip}>
          <AddIcon></AddIcon>
        </IconButton>
      </Stack>
      <NewTripModal open={open} onClose={modalClose} />
    </Box>
  );
}

export default Heading;
