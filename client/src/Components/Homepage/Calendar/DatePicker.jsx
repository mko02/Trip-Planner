import React from "react";

import TextField from "@mui/material/TextField";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";

import { DesktopDatePicker } from "@mui/x-date-pickers/DesktopDatePicker";

export default function MaterialUIPickers({ label }) {
  //const [value, setValue] = React.useState(new Date("04/01/2022 12:00:00"));
  const [value, setValue] = React.useState(new Date());

  return (
    <>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DesktopDatePicker
          label={label}
          inputFormat="MM/DD/YYYY" //depends on date lib
          value={value}
          onChange={setValue}
          renderInput={(params) => {
            return <TextField {...params} />;
          }}
          views={["day", "month"]}
          showDaysOutsideCurrentMonth //very useful
          //@ts-ignore
          clearable //Typing seems to be missing for this
        />
      </LocalizationProvider>
    </>
  );
}
