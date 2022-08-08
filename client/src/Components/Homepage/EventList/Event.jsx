import React from 'react';
import './Event.css'

export default function Event({ event, index }) {
    const month ={
        '01' : 'Jan',
        '02' : 'Feb',
        '03' : 'Mar',
        '04' : 'Apr',
        '05' : 'May',
        '06' : 'Jun',
        '07' : 'Jul',
        '08' : 'Aug',
        '09' : 'Sep',
        '10' : 'Oct',
        '11' : 'Nov',
        '12' : 'Dec',
    }

    const time = event.start_time;
    const start_month = month[time.substring(5,7)];
    const start_day = time.substring(8,10);
    const start_time = time.substring(11,16)


    return (
        <div className='events_home'>
            <div className='title_home'>
                <div className='index_home'>
                    {index}
                </div>
                <div className='event-title_home'>
                    {event.title}
                </div>
            </div>
            <div className='time_home'>
                {`${start_month} ${start_day}, ${start_time}`}
            </div>
        </div>
    )
}
