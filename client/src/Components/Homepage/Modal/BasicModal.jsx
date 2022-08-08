import React from "react";
import Typography from "@mui/material/Typography";
import { Modal, Box } from "@mui/material";

const BasicModal = ({ open, onClose, title, subTitle, content }) => {
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
        <Typography id="modal-modal-title" variant="h6" component="h2">
          {title}
        </Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }}>
          {subTitle}
        </Typography>
        {content}
      </Box>
    </Modal>
  );
};

export default BasicModal;
