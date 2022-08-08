import React from "react";
import BasicModal from "./BasicModal";
import DatePicker from "../Calendar/DatePicker";

import styled from "styled-components";
import Stack from "@mui/material/Stack";
import { Box, TextField } from "@mui/material";

function NewTripModal({ open, onClose }) {
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
          placeholder="New Trip Name"
          name="NewTripName"
          label="New Trip Name"
        />
        <DatePicker label="Start Date" />
        <DatePicker label="End Date" />
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
      title="New Trip"
      subTitle="Enter title and dates for your new trip then hit save!"
      content={getContent()}
    ></BasicModal>
  );
}

export default NewTripModal;

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
