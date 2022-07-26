import { Typography } from '@mui/material';
import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar';
import './calendar.css';



export const ReactCalendar = (props) => {
    const [date, setDate] = useState(new Date());
  
    const onChange = date => {
      setDate(date)
    }
    
    const mark = [
      'Jul 15 2022',
      'Jul 16 2022',
      'Jul 17 2022'
    ] 
    //props.tripDate

    const today = new Date()
  
    return (
      <div>
        <Typography class="monthTitle">{today.toLocaleString('default', { month: 'long', year: 'numeric'})}</Typography>

         <Calendar 
            tileClassName={({ date, view }) => {
              // date will return every date visible on calendar and view will view type (eg. month)
              if(date.toDateString().substring(4) === mark.at(0)) {
                return 'first-block';
              } else if (date.toDateString().substring(4) === mark.at(-1)) {
                return 'last-block'
              } else if (mark.includes(date.toDateString().substring(4)))
                return 'center-block';

              if (view === 'month' && date.toDateString() === (today).toDateString()) {
                return 'fc-today';
              }
       
            }}
          calendarType="US"
          locale="en"

          //access dates/events
          onChange={onChange}
          onClickDay={(day) => console.log('Date Clicked: ', day) } //click date and link to event

          //remove navbar function (can't change to year-view ect)
          minDetail="month"
          maxDetail="month"
          defaultView="month"
          showNavigation={false}
          
          
          //limit month view
          //maxDate={new Date(today.getFullYear, today.getMonth + 1, 1)}
          //minDate={new Date(today.getFullYear, today.getMonth, 1)}
          
          //remove nav (function not removed)
          
          prevLabel=''
          prev2Label=''
          nextLabel=''
          next2Label='' 

          showNeighboringMonth={false}

        />
      </div> 
    );
  }