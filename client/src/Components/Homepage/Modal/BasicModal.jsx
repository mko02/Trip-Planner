import React from "react";
import Typography from "@mui/material/Typography";
import { Modal, Box, Input } from "@mui/material";

const BasicModal = ({ open, onClose }) => {
  const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 800,
    bgcolor: "background.paper",
    borderRadius: "5px",
    boxShadow: 50,
    padding: 8,
  };

  return (
    <Modal open={open} onClose={onClose}>
      <Box sx={style}>
        <Typography
          id="modal-modal-title"
          variant="h6"
          component="h2"
        ></Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }}>
          Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
        </Typography>
        <Input placeholder="Trip Title" />
        <Input placeholder="Date" />
      </Box>
    </Modal>
  );
};

export default BasicModal;
