import React, { useState } from 'react'
import { Stack, IconButton, Button } from '@mui/material';
import EventList from "../Components/TripPage/EventList"
import { Add } from "@mui/icons-material"
import { sample_package_data } from "../DummyInfo/sample_package_data"
import Member from "../Components/TripPage/Members/Member"
import MemberList from '../Components/TripPage/Members/MemberList'
import NewEventModal from '../Components/TripPage/NewEventModal';

function Trip(props) {
  const [open, setOpen] = useState(false);

  const addEvent = () => {
    console.log("click, addEvent action!");
    setOpen(true);
  };

  const modalClose = (e) => {
    e.stopPropagation();
    setOpen(false);
  }; //e = event
  //prevent dubbed bubbling
  //Modal to be close at default
  // props.title -> the title of the trip
  // retrieve data from the backend
  let trip = sample_package_data[props.title]
  const header_style = {
    fontSize: "60px",
    alignContent: "center",
    margin: "30px",
    marginTop: "0px",
    display: "grid",
    gridTemplateColumns: "5fr 1fr",

  }

  const transaction_sheet_style = {
    backgroundColor: "#EEEEEE",
    color: "black",
    fontFamily: 'Roboto',
    fontWeight: "300",
    fontSize: "30px",
    paddingTop: "50px",
    paddingBottom: "50px",
    marginTop: "100px",
  }

  return (
    <div>
      <Stack direction={"row"} sx={{
        display: "grid",
        gap: "10",
        gridTemplateColumns: "8fr 2fr",
        margin: "30px"
      }}>
        <Stack sx={{
          margin: "30px"
        }}>
          <div className={"header"} style={header_style}>
            <div>{trip.title}</div>
            <div style={{ marginLeft: "auto", marginRight: 0 }}>
              <IconButton onClick={addEvent}>
                <Add />
              </IconButton>
              <NewEventModal open={open} onClose={modalClose} />
            </div>
          </div>
          <EventList events={trip.event}></EventList>
        </Stack>
        <Stack className={"sidebar"}>
          <Button sx={transaction_sheet_style}>Transaction Sheet</Button>
          <MemberList members={trip.member} />
        </Stack>
      </Stack>
    </div>
  )
}

export default Trip