import React from "react";

import TextField from "@mui/material/TextField";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DateTimePicker } from "@mui/x-date-pickers/DateTimePicker";
import CalendarMonthIcon from "@mui/icons-material/CalendarMonth";
import ArrowLeftIcon from "@mui/icons-material/ArrowLeft";
import ArrowRightIcon from "@mui/icons-material/ArrowRight";

export default function MaterialUIPickers() {
  //const [value, setValue] = React.useState(new Date("04/01/2022 12:00:00"));
  const [value, setValue] = React.useState(new Date());

  const handleChange = (newValue) => {
    setValue(newValue);
  };

  const popperSx = {
    "& .MuiPaper-root": {
      backgroundColor: "rgba(120, 120, 120, 0.2)",
    },
    "& .MuiCalendarPicker-root": {
      backgroundColor: "rgba(45, 85, 255, 0.4)",
    },
    "& .MuiPickersDay-dayWithMargin": {
      color: "rgb(229,228,226)",
      backgroundColor: "rgba(50, 136, 153)",
    },
    "& .MuiTabs-root": { backgroundColor: "rgba(120, 120, 120, 0.4)" },
  };

  return (
    <>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateTimePicker
          label="Date And Time Picker"
          value={value}
          onChange={handleChange}
          components={{
            OpenPickerIcon: CalendarMonthIcon,
            LeftArrowIcon: ArrowLeftIcon,
            RightArrowIcon: ArrowRightIcon,
          }}
          InputProps={{ sx: { "& .MuiSvgIcon-root": { color: "blue" } } }}
          PopperProps={{
            sx: popperSx,
          }}
          renderInput={(params) => <TextField {...params} />}
        />
      </LocalizationProvider>
    </>
  );
}
