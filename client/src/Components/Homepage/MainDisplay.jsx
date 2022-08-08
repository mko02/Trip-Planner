import React, { useState } from "react";
import Heading from "./Heading";
import { Box } from "@mui/material";
import TripList from "./TripList/TripList";

import { sample_package_data } from "../../DummyInfo/sample_package_data";

function Main() {
  const [trips] = useState(sample_package_data);

  return (
    <Box bgcolor="white" padding={2} flex={2}>
      <Heading />

      <TripList trips={trips} />
    </Box>
  );
}

export default Main;
