import React from "react";
import BasicModal from "../Homepage/Modal/BasicModal";
import DateTimePicker from "../Homepage/Calendar/DateTimePicker";

import styled from "styled-components";
import Stack from "@mui/material/Stack";
import { Box, TextField } from "@mui/material";

function NewEventModal({ open, onClose }) {
  const modalStyles = {
    inputFields: {
      display: "flex",
      flexDirection: "column",
      marginTop: "20px",
      marginBottom: "15px",
    },
  };

  const getContent = () => (
    <Box sx={modalStyles.inputFields}>
      <Stack spacing={3}>
        <TextField
          placeholder="New Event Name"
          name="NewEventName"
          label="NewEventName"
        />
        <DateTimePicker label="Start Date" />
        <DateTimePicker label="End Date" />
        <TextField
          placeholder="Description this is my description"
          name="EventDescription"
          label="EventDescription"
          multiline
          rows={4}
          type="text"
                  sx={{
                      minHeight: '100px',
                  }}
        />
      </Stack>
      <SubmitButton
      // onClick={console.log("submit new trip form and data, post to server")}
      //now the onclick doesn't work as expected
      >
        Create
      </SubmitButton>
    </Box>
  );

  return (
    <BasicModal
      open={open}
      onClose={onClose}
      title="New Event"
      subTitle="Enter title, date, and time for your new Event then hit save!"
      content={getContent()}
    ></BasicModal>
  );
}

export default NewEventModal;

const SubmitButton = styled.button`
  background-color: rgba(224, 224, 224, 0.05);
  margin-top: 2em;
  border-radius: 5px;
  border: "2px";
  display: center;
  width: 20%;
  color: black;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  padding: 10px 12px;
  text-align: center;
  vertical-align: baseline;
  white-space: nowrap;
  position: relative;
`;
