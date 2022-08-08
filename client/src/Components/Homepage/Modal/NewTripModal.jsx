import React from "react";
import BasicModal from "./BasicModal";
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
      <TextField
        placeholder="New Trip Name"
        name="NewTripName"
        label="New Trip Name"
      />
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
